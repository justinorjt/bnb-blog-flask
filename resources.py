from flask import request, abort
from flask_restful import Resource, reqparse
import pymongo
from bson.objectid import ObjectId
from passlib.hash import sha256_crypt
# from models import UserModel, BlogPost
from functools import wraps
import json, uuid, jwt, datetime, urllib.parse
import scrapeAirBnbNews,scrapeKitCollections, scrapeYoutube
# from pymongo import MongoClient

# DATABASE CONNECTION
# client = pymongo.MongoClient("mongodb+srv://justin123:justin123@cluster0-tonis.mongodb.net/test")
client = pymongo.MongoClient("mongodb://justin123:justin123@cluster0-shard-00-00-tonis.mongodb.net:27017,cluster0-shard-00-01-tonis.mongodb.net:27017,cluster0-shard-00-02-tonis.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
blogposts = db.blogposts
members = db.users
tubeStore = db.youtube
kitStore = db.kitcollections
newsStore = db.bnbnews
comments = db.comments

def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = None

		if 'x-access-token' in request.headers:
			token = request.headers['x-access-token']

		if not token:
			return json.dumps({"message": "Token is Missing"})

		try:
			data = jwt.decode(token, 'crazy')
			current_user = members.find_one({ "user_id" : data['user_id'] })
		except Exception as e:
			return json.dumps({"message": "Token is Invalid"})
		
		return f(current_user, *args, **kwargs)

	return decorated

# SCRIPT STORAGE ######################################################################################################
def storeBnbnews():
	news = scrapeAirBnbNews.getArticles()
	newsStore.remove({})
	newsStore.insert(news)


def storeKits():
	kits = scrapeKitCollections.getKits()
	kitStore.remove({})
	kitStore.insert(kits)


def storeYoutube():
	videos = scrapeYoutube.getVideos()
	tubeStore.remove({})
	tubeStore.insert(videos)


# API RESOURCE BEGINS

# Retrieves scrapeAirBnbNews articles from google #######################################################################
class bnbnews(Resource):
	def get(self):
		allnews = []
		[allnews.append(news) for news in newsStore.find()] 
		return json.dumps(allnews, default=str)

# Retrieves Kit collections from Kit Account ############################################################################
class kitcollections(Resource):
	def get(self):
		allkits = []
		[allkits.append(kit) for kit in kitStore.find()] 
		return json.dumps(allkits, default=str)

# Retrieves Youtube Channel videos #######################################################################################
class youtube(Resource):
	def get(self):

		allvids = []
		[allvids.append(vid) for vid in tubeStore.find()] 
		return json.dumps(allvids, default=str)

# USERS
# HANDLES USER LOGIN ######################################################################################################
class login(Resource):
	def post(self):
		email = request.json['email']
		password = request.json['password']
		
		user = members.find_one({ "email" : email })

		if not user:
			return json.dumps({"message":'Invalid Credentials'}, default=str)
		if not sha256_crypt.verify(password, user['password']):
			return json.dumps({"message":'Error: Wrong password'}, default=str)

		token = jwt.encode({"user_id": user['user_id'], "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=20)}, 'crazy')

		return json.dumps({'token': token.decode('UTF-8')})

	
		# return json.dumps(user, default=str)

# HANDLES USERS #############################################################################################################
class user(Resource):
	# User Sign Up
	def post(self):
		if not request.json:
			abort(400)
		
		email = request.json['email']
		firstname = request.json['firstname']
		lastname = request.json['lastname']
		phone = request.json['phone']
		dateJoined = request.json['dateJoined']
		role = request.json['role']
		password = sha256_crypt.encrypt(request.json['password'])
		user_id=str(uuid.uuid4())

		user = members.find_one({ "email" : email })

		if user:
			return json.dumps({"message":'User email already exists. Please Login'})

		userObject = {
		"email":email, "firstname":firstname, "lastname":lastname, "phone":phone,  
		"dateJoined": dateJoined, "role":role, "password":password, "user_id":user_id
		}
		
		user = members.insert_one(userObject)

		return json.dumps(userObject, default=str)

	# Get User By Id
	# @token_required
	# def get(current_user,self, user_id):
	def get(self):
		# Get one user
		user_id = request.args['user_id']
		try:
			# Verify comment
			one_member = members.find_one(ObjectId(user_id))
		except Exception as e:
			# If comment does not exist
			return json.dumps({"message":'Member not Found', "Error":e}, default=str)
			
		# if not one_member:
		# 	return json.dumps({"message": "User does not exist" })

		return json.dumps({"user" : one_member}, default = str)

	# Delete a User
	# @token_required
	# def delete(current_user,self, user_id):
	def delete(self):
		# Get one user
		user_id = request.args['user_id']
		one_member = members.find_one(ObjectId(user_id))

		if not one_member:
			return json.dumps({"message": "User does not exist" })

		members.delete_one(one_member)
		return "User deleted"

	# Edit a User
	# @token_required
	# def put(current_user,self, user_id):
	def put(self):
		# Get one user
		user_id = request.args['user_id']
		one_member = members.find_one(ObjectId(user_id))

		if not one_member:
			return json.dumps({"message": "User does not exist" })

		one_member['role'] = "Admin"
		members.save(one_member)

		return json.dumps({"user": one_member}, default = str)

# GET ALL USERS ########################################################################################################
class allusers(Resource):
	# @token_required
	# def get(current_user ,self):
	def get(self):

		# if current_user['role'] != 'Admin':
		# 	return json.dumps({"message": "Need Admin to access this route"})

		allusers = []
		[allusers.append(user) for user in members.find()] 
		return json.dumps({'users':allusers}, default = str)

# HANDLES A SINGLE BLOGPOST #############################################################################################
class blogpost(Resource):
	# Create a blogpost
	# @token_required
	# def post(current_user,self):
	def post(self):
		# If there is no request body
		if not request.json:
			abort(400)

		title=request.json['title']
		titleLink=request.json['titleLink']
		author=request.json["author"]
		description=request.json["description"]
		content=request.json["content"]
		category=request.json["category"]

		exists = blogposts.find_one({"title": title})

		if exists:
			return json.dumps({"message":'Title is a duplicate. Please Rename'})

		aPost = { "title":title,"titleLink":titleLink, "author":author, "description":description,"content":content, 
		"category":category, "dateCreated":'July 21, 2019'}

		blogposts.insert_one(aPost)
		return json.dumps(aPost, default=str), 200
	
	def get(self):
		titleLink = request.args['titleLink']
		urlTitleLink = urllib.parse.quote_plus(titleLink)
		# Verify post
		one_post = blogposts.find_one({"titleLink": urlTitleLink})
		# IF post does not exist
		if not one_post:
			return json.dumps({"message":'Post not Found'}, default=str)

		return json.dumps(one_post, default = str)
		# return json.dumps(titleLink, default = str)

	# @token_required
	# def put(current_user,self):
	def put(self):
		titleLink = request.args['titleLink']
		urlTitleLink = urllib.parse.quote_plus(titleLink)
		# Verify post
		one_post = blogposts.find_one({"titleLink": urlTitleLink})
		# IF post does not exist
		if not one_post:
			return json.dumps({"message":'Post not Found'}, default=str)

		title=request.json['title']
		titleLink=request.json['titleLink']
		author=request.json["author"]
		description=request.json["description"]
		content=request.json["content"]
		category=request.json["category"]
		aPost = { "title":title,"titleLink":titleLink, "author":author, "description":description,"content":content, 
		"category":category, "dateCreated":'July 21, 2019'}
		blogposts.replace_one({"titleLink": urlTitleLink}, aPost)

		return json.dumps(aPost, default=str), 200

	# @token_required
	# def delete(current_user,self):
	def delete(self):
		titleLink = request.args['titleLink']
		urlTitleLink = urllib.parse.quote_plus(titleLink)
		# Verify post
		one_post = blogposts.find_one({"titleLink": urlTitleLink})
		# IF post does not exist
		if not one_post:
			return json.dumps({"message":'Post not Found'}, default=str)
		
		# Delete post
		blogposts.delete_one(one_post)

		return json.dumps(one_post, default=str), 200

# HANDLES A LIST OF BLOGPOSTS ##########################################################################################
class blogpostlist(Resource):
	# Get all blogposts
	def get(self):
		alist =[]
		[alist.append(doc) for doc in blogposts.find()] 
		return json.dumps(alist, default = str)

# HANDLES A COMMENT #####################################################################################################
class comment(Resource):
	def post(self):
		# If there is no request body
		if not request.json:
			return json.dumps({"message":'Not Valid post format'}, default=str)

		content=request.json['content']
		user_id=request.json['user_id']
		time_posted=request.json["time_posted"]
		post_id=request.json["post_id"]
		
		
		aComment = { "content":content, "user_id":user_id, "time_posted":time_posted, "post_id":post_id}

		comments.insert_one(aComment)
		return json.dumps({"message":'Comment Posted!', "data": aComment}, default=str), 200

	def get(self):
		if not request.args:
			return json.dumps({"message":'No request arguments'}, default=str)

		comment_id = request.args['comment_id']
		try:
		# Verify comment
			one_comment = comments.find_one(ObjectId(comment_id))
		except Exception as e:
			# If comment does not exist
			return json.dumps({"message":'Comment not Found', "Error":e}, default=str)
			
		
		return json.dumps(one_comment, default = str)


	def put(self):
		if not request.args:
			return json.dumps({"message":'Not Valid request'}, default=str)

		comment_id = request.args['comment_id']
		try:
		# Verify post
			one_post = comments.find_one(ObjectId(comment_id))
		except Exception as e:
			# If Post does not exist
			return json.dumps({"message":'Comment not Found', "Error":e}, default=str)
			

		content=request.json['content']
		user_id=request.json['user_id']
		time_posted=request.json["time_posted"]
		post_id=request.json["post_id"]
		
		aComment = { "content":content, "user_id":user_id, "time_posted":time_posted, "post_id":post_id}

		comments.replace_one(ObjectId(comment_id), aComment)

		return json.dumps(aComment, default=str), 200
		

	def delete(self):
		if not request.args:
			return json.dumps({"message":'Not Valid request'}, default=str)

		comment_id = request.args['comment_id']
		try:
		# Verify post
			aComment = comments.find_one(ObjectId(comment_id))
		except Exception as e:
			# If Post does not exist
			return json.dumps({"message":'Comment not Found', "Error":e}, default=str)
			
		# Delete post
		comments.delete_one(aComment)
		return json.dumps(aComment, default=str), 200

		
# HANDLES A LIST OF COMMENTS ############################################################################################
class commentlist(Resource):
	# Get all blogposts
	def get(self):
		listofcomments =[]

		if not request.args:
			[listofcomments.append(doc) for doc in comments.find()] 
		else:
			post_id = request.args['post_id']

			[listofcomments.append(doc) for doc in comments.find({"post_id": post_id})] 
			if listofcomments == []:
				return json.dumps({"message":'No Comments match this post ID'}, default=str)
			
		return json.dumps(listofcomments, default = str)