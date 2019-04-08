from flask import Flask, request, render_template, jsonify, url_for
from flask_restful import Resource, Api, reqparse,abort
from requests import put, get, post, delete
from marshmallow import Schema, fields
from flask_cors import CORS
from pymongo import MongoClient
import pymongo
import json
import dns
import scrapeAirBnbNews


client = pymongo.MongoClient("mongodb+srv://justin123:justin123@cluster0-tonis.mongodb.net/test?retryWrites=true")
db = client.test
blogposts = db.blogposts
articles = {}

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

parser = reqparse.RequestParser()

@app.route('/')
def index():
	return render_template('index.html')

# ROUTING/REDIRECTING ALL FLASK ROUTES TO INDEX.HTML WHERE ANGULAR ROUTES ARE SERVED
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	return render_template('index.html')

# API RESOURCE BEGINS

# Retrieves scrapeAirBnbNews articles from google
class bnbnews(Resource):
	def get(self):
		news = scrapeAirBnbNews.getArticles()
		return news
# Get post by id

# Post article to blog
class blogPost(Resource):
	def post(self):
		# args = parser.parse_args()
		header=request.values.get("header")
		author=request.values.get("author")
		content=request.values.get("content")
		category=request.values.get("category")
		blogposts.insert({ "header":header, "author":author, "content":content, "category":category })
		return 'request accepted'

	def get(self):
		allposts = blogposts.find()
		alist =[]
		[alist.append(doc) for doc in blogposts.find()] 
		return str(alist)

# API ENDPOINTS 
api.add_resource(bnbnews, '/api/bnbnews')
api.add_resource(
	blogPost, 
	#Get all posts
	'/api/get_posts',
	#Get article by ID
	'/api/get_post/<post_id>',
	#Get add post
	'/api/add_post',
	#Delete post
	'/api/delete_post/<post_id>',
)

# if __name__ == '__main__':
app.run(debug=True)