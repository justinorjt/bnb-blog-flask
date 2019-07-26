from flask import Flask, request, abort, jsonify
from flask_restful import Resource, Api, abort, reqparse
from pymongo import MongoClient
from passlib.hash import sha256_crypt
from models import UserModel, BlogPost
from functools import wraps
import scrapeAirBnbNews, pymongo, json, uuid, jwt, datetime, urllib.parse


# DATABASE CONNECTION
# client = pymongo.MongoClient("mongodb+srv://justin123:justin123@cluster0-tonis.mongodb.net/test")
client = pymongo.MongoClient("mongodb://justin123:justin123@cluster0-shard-00-00-tonis.mongodb.net:27017,cluster0-shard-00-01-tonis.mongodb.net:27017,cluster0-shard-00-02-tonis.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
# client = pymongo.MongoClient("mongodb+srv://justin123:zgZ9QTCQ8C!7sk-@cluster0-tonis.mongodb.net/test?retryWrites=true")
db = client.test
blogposts = db.blogposts
members = db.users

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


# API RESOURCE BEGINS

# Retrieves scrapeAirBnbNews articles from google
class bnbnews(Resource):
	def get(self):
		news = scrapeAirBnbNews.getArticles()
		return news

# USERS
# Handles user login
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


class user(Resource):
	# User Sign Up
	def post(self):
		if not request.json:
			abort(400)
		
		email = request.json['email']
		password = sha256_crypt.encrypt(request.json['password'])

		user = members.find_one({ "email" : email })

		if user:
			return json.dumps({"message":'User email already exists. Please Login'})

		newUser = UserModel(email=email, password=password, user_id=str(uuid.uuid4()))
		user = members.insert_one(newUser.__dict__)

		return json.dumps(newUser.__dict__, default=str)

	# Get User By Id
	@token_required
	def get(current_user,self, user_id):
		# Get one user
		one_member = members.find_one({"user_id": user_id})

		if not one_member:
			return json.dumps({"message": "User does not exist" })

		return json.dumps({"user" : one_member}, default = str)

	# Delete a User
	@token_required
	def delete(current_user,self, user_id):
		one_member = members.find_one({"user_id": user_id})

		if not one_member:
			return json.dumps({"message": "User does not exist" })

		members.delete_one(one_member)
		return "User deleted"

	# Edit a User
	@token_required
	def put(current_user,self, user_id):
		one_member = members.find_one({"user_id": user_id})

		if not one_member:
			return json.dumps({"message": "User does not exist" })

		one_member['role'] = "Admin"
		members.save(one_member)

		return json.dumps({"user": one_member}, default = str)



# Get All Users
class allusers(Resource):
	@token_required
	def get(current_user ,self):

		if current_user['role'] != 'Admin':
			return json.dumps({"message": "Need Admin to access this route"})

		allusers = []
		[allusers.append(user) for user in members.find()] 
		return json.dumps({'users':allusers}, default = str)

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

	@token_required
	def put(current_user,self, post_id):
		# Verify post
		one_post = blogposts.find_one({"post_id": post_id})
		# IF post does not exist
		if not one_post:
			return "Post not found"

	@token_required
	def delete(current_user,self, post_id):
		# Verify post
		one_post = blogposts.find_one({"post_id": post_id})
		# IF post does not exist
		if not one_post:
			return "Post not found"
		# Delete post
		members.delete_one(one_post)
		return "Post deleted"


class blogpostlist(Resource):
	# Get all blogposts
	def get(self):
		alist =[]
		[alist.append(doc) for doc in blogposts.find()] 
		return json.dumps(alist, default = str)

