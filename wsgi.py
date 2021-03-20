from backend import app
from resources import storeBnbnews, storeYoutube, storeKits


if __name__ == '__main__':
	# storeYoutube()
	# storeKits()
	# storeBnbnews()
	app.run(debug=True, threaded=True)
