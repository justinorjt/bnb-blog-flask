from flask import Flask, request, render_template, jsonify, url_for, abort, session
from flask_restful import Resource, Api, reqparse,abort
from flask_cors import CORS
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from pymongo import MongoClient
import uuid
import resources
from resources import storeBnbnews, storeYoutube, storeKits


articles = {}

# INIT APP
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
api = Api(app)
# cors = CORS(app, resources=r'/api/*')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
scheduler = BackgroundScheduler()
scheduler.start()

# SCHEDULED SCRIPT RUNS
kitjob = scheduler.add_job(storeKits, 'interval', days=1)
tubejob = scheduler.add_job(storeYoutube, 'interval', hours=12)
newsjob = scheduler.add_job(storeBnbnews, 'interval', hours=3)


@app.route('/')
def index():
	return render_template('index.html')

# ROUTING/REDIRECTING ALL FLASK ROUTES TO INDEX.HTML WHERE ANGULAR ROUTES ARE SERVED
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	return render_template('index.html')


# API ENDPOINTS 
api.add_resource(resources.bnbnews, '/api/bnbnews') #GET
api.add_resource(resources.kitcollections, '/api/kitcollections') #GET
api.add_resource(resources.youtube, '/api/youtube') #GET
api.add_resource(resources.login, '/api/login') # POST
# api.add_resource(resources.user, '/api/user') # POST, GET, PUT, DELETE
api.add_resource(resources.user, '/api/user', '/api/user/<user_id>') # POST, GET, PUT, DELETE
api.add_resource(resources.allusers, '/api/allusers') # GET
api.add_resource(resources.blogpostlist, '/api/blogpostlist') # GET
api.add_resource(resources.blogpost, '/api/blogpost/') # POST, GET, PUT, DELETE

# if __name__ == '__main__':
# app.environment = development
app.run(debug=True, threaded=True)