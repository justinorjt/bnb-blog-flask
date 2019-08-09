# Pull in Kit Collections

from bs4 import BeautifulSoup as bsoup
import requests
from html.parser import HTMLParser
import pandas as pd
from selenium import webdriver

def getKits():
	browser = webdriver.Chrome() 
	theUrl = 'https://kit.com/rakidzich'
	browser.get(theUrl) 	
	# get the html and the link
	innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string

	# r = requests.get(theUrl)

	# driver = webdriver.PhantomJS()
	# driver.get(my_url)
	p_element = driver.find_element_by_id(id_='intro-text')
	print(p_element.text)

	page = r.text
	#filter through tags
	soup = bsoup(page, 'html.parser')
	posts = soup.find_all('div', attrs={'class':'collection-card__header'})

	 #List of objects to populate dataframe
	kits = []
	num = 0
	# loop to add articles to list
	for post in posts:
		# kits.append(post)
		num += 1



	print(innerHTML)

getKits()