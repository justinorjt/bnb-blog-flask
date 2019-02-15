from flask import Flask, request, render_template
from flask_restful import Resource, Api, reqparse,abort
from requests import put, get, post, delete
from pymongo import MongoClient
import json
import scrapeAirBnbNews
# client = MongoClient('localhost:27017')
# db = client.ContactDB

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return render_template('index.html')

# ROUTING/REDIRECTING ALL FLASK ROUTES TO INDEX.HTML WHERE ANGULAR ROUTES ARE SERVED
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('index.html')

class TodoList(Resource):
    def get(self):
        articles = scrapeAirBnbNews.getArticles()
        return articles

api.add_resource(TodoList, '/api/articles')
# api.add_resource(Todo, '/api/todos/<todo_id>')

# if __name__ == '__main__':
app.run(debug=True)