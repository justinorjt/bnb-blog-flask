# Pull in Google Air-BnB Articles

from bs4 import BeautifulSoup as bsoup
import requests
from html.parser import HTMLParser
import pandas as pd

def getArticles():
	theUrl = 'https://www.google.com/search?q=airbnb+news&tbm=nws&source=lnt&tbs=qdr:m&sa=X&ved=0ahUKEwiAhMmfkbLeAhVHja0KHS6UCPcQpwUIIQ&biw=1536&bih=706&dpr=1.25'
	# get the html and the link
	r = requests.get(theUrl)
	page = r.text
	#filter through tags
	soup = bsoup(page, 'html.parser')
	posts = soup.find_all('div', attrs={'class':'g'})

	 #List of objects to populate dataframe
	art =[]
	# if images are needed
	# for img in images:
	# 	ii = img.find('img').get('src')

	# loop to add articles to list
	for post in posts:
		tt = (post.find('a').get_text())
		ll = (post.find('a').get('href'))
		dd = (post.find('div',{'class':'st'}).get_text())
		art.append({'title':tt,'link':ll,'desc':dd})
	
	#ADD LIST OF ARTICLE INFO OBJECTS TO DATA FRAME
	articles = pd.DataFrame(art)
	# print(art)
	return art

# getArticles()