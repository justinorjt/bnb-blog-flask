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
			return makeJson({"message": "Token is Missing"})

		try:
			data = jwt.decode(token, 'crazy')
			current_user = members.find_one({ "user_id" : data['user_id'] })
		except Exception as e:
			return makeJson({"message": "Token is Invalid"})
		
		return f(current_user, *args, **kwargs)

	return decorated

def makeJson(stuff):
	return json.loads(json.dumps(stuff, default=str))

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
		return makeJson(allnews)

# Retrieves Kit collections from Kit Account ############################################################################
class kitcollections(Resource):
	def get(self):
		allkits = []
		[allkits.append(kit) for kit in kitStore.find()] 
		return makeJson(allkits)

# Retrieves Youtube Channel videos #######################################################################################
class youtube(Resource):
	def get(self):

		allvids = []
		[allvids.append(vid) for vid in tubeStore.find()] 
		return makeJson(allvids)

# USERS
# HANDLES USER LOGIN ######################################################################################################
class login(Resource):
	def post(self):
		email = request.json['email']
		password = request.json['password']
		
		user = members.find_one({ "email" : email })

		if not user:
			return makeJson({"message":'Invalid Credentials'})
		if not sha256_crypt.verify(password, user['password']):
			return makeJson({"message":'Error: Wrong password'})

		token = jwt.encode({"user_id": user['user_id'], "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=20)}, 'crazy')

		return makeJson({'token': token.decode('UTF-8')})

	
		# return makeJson(user)

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
			return makeJson({"message":'User email already exists. Please Login'})

		userObject = {
		"email":email, "firstname":firstname, "lastname":lastname, "phone":phone,  
		"dateJoined": dateJoined, "role":role, "password":password, "user_id":user_id
		}
		
		user = members.insert_one(userObject)

		return makeJson(userObject)

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
			return makeJson({"message":'Member not Found', "Error":e})
			
		# if not one_member:
		# 	return makeJson({"message": "User does not exist" })

		return makeJson({"user" : one_member})

	# Delete a User
	# @token_required
	# def delete(current_user,self, user_id):
	def delete(self):
		# Get one user
		user_id = request.args['user_id']
		one_member = members.find_one(ObjectId(user_id))

		if not one_member:
			return makeJson({"message": "User does not exist" })

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
			return makeJson({"message": "User does not exist" })

		one_member['role'] = "Admin"
		members.save(one_member)

		return makeJson({"user": one_member})

# GET ALL USERS ########################################################################################################
class allusers(Resource):
	# @token_required
	# def get(current_user ,self):
	def get(self):

		# if current_user['role'] != 'Admin':
		# 	return makeJson({"message": "Need Admin to access this route"})

		allusers = []
		[allusers.append(user) for user in members.find()] 
		return makeJson({'users':allusers})

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
			return makeJson({"message":'Title is a duplicate. Please Rename'})

		aPost = { "title":title,"titleLink":titleLink, "author":author, "description":description,"content":content, 
		"category":category, "dateCreated":'July 21, 2019'}

		blogposts.insert_one(aPost)
		return makeJson(aPost), 200
	
	def get(self):
		titleLink = request.args['titleLink']
		urlTitleLink = urllib.parse.quote_plus(titleLink)
		# Verify post
		one_post = blogposts.find_one({"titleLink": urlTitleLink})
		# IF post does not exist
		if not one_post:
			return makeJson({"message":'Post not Found'})

		return makeJson(one_post)
		# return makeJson(titleLink)

	# @token_required
	# def put(current_user,self):
	def put(self):
		titleLink = request.args['titleLink']
		urlTitleLink = urllib.parse.quote_plus(titleLink)
		# Verify post
		one_post = blogposts.find_one({"titleLink": urlTitleLink})
		# IF post does not exist
		if not one_post:
			return makeJson({"message":'Post not Found'})

		title=request.json['title']
		titleLink=request.json['titleLink']
		author=request.json["author"]
		description=request.json["description"]
		content=request.json["content"]
		category=request.json["category"]
		aPost = { "title":title,"titleLink":titleLink, "author":author, "description":description,"content":content, 
		"category":category, "dateCreated":'July 21, 2019'}
		blogposts.replace_one({"titleLink": urlTitleLink}, aPost)

		return makeJson(aPost), 200

	# @token_required
	# def delete(current_user,self):
	def delete(self):
		titleLink = request.args['titleLink']
		urlTitleLink = urllib.parse.quote_plus(titleLink)
		# Verify post
		one_post = blogposts.find_one({"titleLink": urlTitleLink})
		# IF post does not exist
		if not one_post:
			return makeJson({"message":'Post not Found'})
		
		# Delete post
		blogposts.delete_one(one_post)

		return makeJson(one_post), 200

# HANDLES A LIST OF BLOGPOSTS ##########################################################################################
class blogpostlist(Resource):
	# Get all blogposts
	def get(self):
		alist =[]
		[alist.append(doc) for doc in blogposts.find()] 
		return makeJson(alist)

# HANDLES A COMMENT #####################################################################################################
class comment(Resource):
	def post(self):
		# If there is no request body
		if not request.json:
			return makeJson({"message":'Not Valid post format'})
		try:
			content=request.json.get('content')
			user_email=request.json.get('user_email')
			time_posted=request.json.get("time_posted")
			post_id=request.json.get("post_id")
			
			
			aComment = { "content":content, "user_email":user_email, "time_posted":time_posted, "post_id":post_id}

			comments.insert_one(aComment)
			return makeJson(aComment), 200

		except Exception as e:
			return makeJson({"message":"Error -> " + str(e)}) 

	def get(self):
		if not request.args:
			return makeJson({"message":'No request arguments'})

		comment_id = request.args['comment_id']
		try:
		# Verify comment
			one_comment = comments.find_one(ObjectId(comment_id))
		except Exception as e:
			# If comment does not exist
			return makeJson({"message":"Error -> "+ str(e)})
			
		
		return makeJson(one_comment)


	def put(self):
		if not request.args:
			return makeJson({"message":'Not arguments sent'})

		try:
			# VERIFY POST
			# comment_id = request.args['post_id']
			comment_id = request.args['comment_id']
			one_comment = comments.find_one(ObjectId(comment_id))	

			if not one_comment:
				return makeJson({"message":"Comment you're trying to edit does not exist"})


			content=request.json.get('content')
			user_email=request.json.get('user_email')
			time_posted=request.json.get('time_posted')
			post_id=request.json.get('post_id')
			
			aComment = { "content":content, "user_email":user_email, "time_posted":time_posted, "post_id":post_id}

			comments.replace_one({"_id":ObjectId(comment_id)}, aComment)

			return makeJson(aComment), 200
		except Exception as e:
			return makeJson({"message":"Error -> " +str(e)})

	def delete(self):
		if not request.args:
			return makeJson({"message":'Not Valid request'})

		comment_id = request.args['comment_id']
		try:
		# Verify post
			aComment = comments.find_one(ObjectId(comment_id))
		except Exception as e:
			# If Post does not exist
			return makeJson({"message":'Comment not Found', "Error":e})
			
		# Delete post
		comments.delete_one(aComment)
		return makeJson(aComment), 200
		
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
				return makeJson({"message":'No Comments match this post ID'})
			
		return makeJson(listofcomments)