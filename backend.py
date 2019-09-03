from flask import Flask, render_template
from flask_restful import Api
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
import resources
from resources import storeBnbnews, storeYoutube, storeKits


articles = {}

# INIT APP
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# INIT FLASK RESTFUL API
api = Api(app)
# INIT CORS RULES FOR API
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# INIT BACKGROUND TASK SCHEDULER
scheduler = BackgroundScheduler()
scheduler.start()

# SCHEDULED SCRIPT RUNS
kitjob = scheduler.add_job(storeKits, 'interval', days=1)
tubejob = scheduler.add_job(storeYoutube, 'interval', hours=1)
newsjob = scheduler.add_job(storeBnbnews, 'interval', hours=1)


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
api.add_resource(resources.user, '/api/user/') # POST, GET, PUT, DELETE
api.add_resource(resources.allusers, '/api/allusers') # GET
api.add_resource(resources.blogpostlist, '/api/blogpostlist') # GET
api.add_resource(resources.blogpost, '/api/blogpost/') # POST, GET, PUT, DELETE
api.add_resource(resources.commentlist, '/api/commentlist/') # GET
api.add_resource(resources.comment, '/api/comment/') # POST, GET, PUT, DELETE


# if __name__ == '__main__':
# 	app.run(debug=True, threaded=True)