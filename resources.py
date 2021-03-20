from flask import request, abort
from flask_restful import Resource, reqparse
import pymongo
from bson.objectid import ObjectId
from passlib.hash import sha256_crypt
from functools import wraps
import json, uuid, jwt, datetime, urllib.parse, time
import scrapeAirBnbNews,scrapeKitCollections, scrapeYoutube
# from pymongo import MongoClient

# DATABASE CONNECTION
# client = pymongo.MongoClient("mongodb+srv://justin123:justin123@cluster0-tonis.mongodb.net/test")
client = pymongo.MongoClient("mongodb://justin123:justin123@cluster0-shard-00-00-tonis.mongodb.net:27017,cluster0-shard-00-01-tonis.mongodb.net:27017,cluster0-shard-00-02-tonis.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
_blogposts = db.blogposts
_members = db.users
tubeStore = db.youtube
kitStore = db.kitcollections
newsStore = db.bnbnews
_comments = db.comments

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
			current_user = _members.find_one({ "user_id" : data['user_id'] })
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
		
		user = _members.find_one({ "email" : email })

		if not user:
			return makeJson({"message":'Invalid Credentials'})
		if not sha256_crypt.verify(password, user['password']):
			return makeJson({"message":'Error: Wrong password'})

		token = jwt.encode({"user_id": user['user_id'], "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=20)}, 'crazy')

		return makeJson({'token': token.decode('UTF-8')})

	
		# return makeJson(user)

# HANDLES USERS #############################################################################################################
class user(Resource):
	# CREATE USERS
	def post(self):
		if not request.json:
			abort(400)
		try:
			email = request.json['email']
			firstname = request.json['firstname']
			lastname = request.json['lastname']
			phone = request.json['phone']
			dateJoined = request.json['dateJoined']
			role = request.json['role']
			password = sha256_crypt.encrypt(request.json['password'])
			user_id=str(uuid.uuid4())

			user = _members.find_one({ "email" : email })

			if user:
				return makeJson({"message":'User email already exists. Please Login'})

			userObject = {
			"email":email, "firstname":firstname, "lastname":lastname, "phone":phone,  
			"dateJoined": dateJoined, "role":role, "password":password, "user_id":user_id
			}
			
			user = _members.insert_one(userObject)

			return makeJson(userObject)

		except Exception as e:
			return makeJson({"Error":str(e)})

	# GET USER(S)
	# @token_required
	# def get(current_user,self):
	def get(self):
		try:
			user_id = request.args.get('user_id')
			#VERFIY USER ID
			if not user_id:
				# WITH NO USER ID PARAMETER RETURN ALL USERS
				allusers = []
				[allusers.append(user) for user in _members.find()]
				return makeJson({'users':allusers})
			else:
				#QUERY THE DATABASE FOR USER WITH THAT ID
				one_member = _members.find_one(ObjectId(user_id))
				if not one_member:
					return makeJson({"message": "User does not exist" })
				else:
					return makeJson({"user" : one_member})

		except Exception as e:
			return makeJson({"Error":str(e)})


	# DELETE A USER
	# @token_required
	# def delete(current_user,self):
	def delete(self):
		# Get one user
		user_id = request.args.get('user_id')
		one_member = _members.find_one(ObjectId(user_id))

		if not one_member:
			return makeJson({"message": "User does not exist" })

		_members.delete_one(one_member)
		return "User deleted"

	# EDIT A USER
	# @token_required
	# def put(current_user,self):
	def put(self):
		# Get one user
		user_id = request.args.get('user_id')
		one_member = _members.find_one(ObjectId(user_id))

		if not one_member:
			return makeJson({"message": "User does not exist" })

		one_member['role'] = "Admin"
		_members.save(one_member)

		return makeJson({"user": one_member})

# HANDLES BLOGPOSTS #############################################################################################
class blogpost(Resource):
	# Create a blogpost
	# @token_required
	# def post(current_user,self):
	def post(self):
		# If there is no request body
		if not request.json:
			abort(400)

		title=request.json.get('title').lower()
		titleLink=request.json.get('titleLink')
		author=request.json.get("author")
		description=request.json.get("description")
		content=request.json.get("content")
		category=request.json.get("category")

		exists = _blogposts.find_one({"title": title})

		if exists:
			return makeJson({"message":'Title is a duplicate. Please Rename'})

		aPost = { "title":title,"titleLink":titleLink, "author":author, "description":description,"content":content, 
		"category":category, "dateCreated":time.time()}

		_blogposts.insert_one(aPost)
		return makeJson(aPost), 200
	
	def get(self):

		try:
			# GET ID PARAMETER
			post_id = request.args.get('id')

			if not post_id:
				alist =[]
				[alist.append(doc) for doc in _blogposts.find()] 
				return makeJson(alist)
			else:					
				# GET ONE POST
				one_post = _blogposts.find_one({"_id": ObjectId(post_id)})
				# VERIFY
				if not one_post:
					return makeJson({"message":'Post not Found'})

				return makeJson(one_post)
		except Exception as e:
			return makeJson({"Error":str(e)})

	# @token_required
	# def put(current_user,self):
	def put(self):
		post_id = request.args.get('id')
		# Verify post
		one_post = _blogposts.find_one({"_id": ObjectId(post_id)})
		# IF post does not exist
		if not one_post:
			return makeJson({"message":'Post not Found'})

		title=request.json.get('title')
		titleLink=request.json.get('titleLink')
		author=request.json.get("author")
		description=request.json.get("description")
		content=request.json.get("content")
		category=request.json.get("category")

		aPost = { "title":title,"titleLink":titleLink, "author":author, "description":description,"content":content, 
		"category":category, "dateCreated": makeJson(one_post).get("dateCreated")}

		_blogposts.replace_one({"_id": ObjectId(post_id)}, aPost)

		return makeJson(aPost), 200

	# @token_required
	# def delete(current_user,self):
	def delete(self):
		post_id = request.args.get('id')
		# Verify post
		one_post = _blogposts.find_one({"_id": ObjectId(post_id)})
		# IF post does not exist
		if not one_post:
			return makeJson({"message":'Post not Found'})
		
		# Delete post
		_blogposts.delete_one(one_post)

		return makeJson(one_post), 200

# HANDLES COMMENTS #####################################################################################################
class comment(Resource):
	def post(self):
		try:
			# If there is no request body
			if not request.json:
				return makeJson({"message":'Not Valid post format'})

			content=request.json.get('content')
			user_email=request.json.get('user_email')
			time_posted=request.json.get("time_posted")
			post_id=request.json.get("post_id")
			
			
			aComment = { "content":content, "user_email":user_email, "time_posted":time_posted, "post_id":post_id}

			_comments.insert_one(aComment)
			return makeJson(aComment)

		except Exception as e:
			return makeJson({"message":"Error -> " + str(e)}) 

	def get(self):

		try:
			listofcomments =[]
			
			if not request.args:
				[listofcomments.append(doc) for doc in _comments.find()] 
				return makeJson(listofcomments)
	
			post_id = request.args.get('post_id')
			comment_id = request.args.get('comment_id')

			if comment_id:
				one_comment = _comments.find_one({"_id":ObjectId(comment_id)})
				return makeJson(one_comment)

			elif post_id:				
				[listofcomments.append(doc) for doc in _comments.find({"post_id": post_id})] 
				if listofcomments == []:
					return makeJson({"message":'No Comments match this post ID'})
			
			return makeJson(listofcomments)

		except Exception as e:
			raise e
			# return makeJson({"Error":str(e)})

	def put(self):
		if not request.args:
			return makeJson({"message":'Not arguments sent'})

		try:
			# VERIFY POST
			# comment_id = request.args['post_id']
			comment_id = request.args.get('comment_id')
			one_comment = _comments.find_one(ObjectId(comment_id))	

			if not one_comment:
				return makeJson({"message":"Comment you're trying to edit does not exist"})


			content=request.json.get('content')
			user_email=request.json.get('user_email')
			time_posted=request.json.get('time_posted')
			post_id=request.json.get('post_id')
			
			aComment = { "content":content, "user_email":user_email, "time_posted":time_posted, "post_id":post_id}

			_comments.replace_one({"_id":ObjectId(comment_id)}, aComment)

			return makeJson(aComment), 200
		except Exception as e:
			return makeJson({"message":"Error -> " +str(e)})

	def delete(self):
		if not request.args:
			return makeJson({"message":'Not Valid request'})

		comment_id = request.args.get('comment_id')
		try:
		# Verify post
			aComment = _comments.find_one(ObjectId(comment_id))
		except Exception as e:
			# If Post does not exist
			return makeJson({"message":'Comment not Found', "Error":e})
			
		# Delete post
		_comments.delete_one(aComment)
		return makeJson(aComment), 200
		
