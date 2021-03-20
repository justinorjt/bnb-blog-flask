# Pull in Google Air-BnB Articles

from bs4 import BeautifulSoup as bsoup
import requests
from html.parser import HTMLParser
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium

def getArticles():
	#SETUP WEBDRIVER
	config = selenium.webdriver.ChromeOptions()
	config.add_argument('headless')
	browser = webdriver.Chrome(options=config) 

	theUrl = 'https://www.google.com/search?q=airbnb+news&tbm=nws&source=lnt&tbs=qdr:m&sa=X&ved=0ahUKEwiAhMmfkbLeAhVHja0KHS6UCPcQpwUIIQ&biw=1536&bih=706&dpr=1.25'
	browser.get(theUrl)
	try:
		WebDriverWait(browser,2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.dbsr")))

		page = browser.page_source
		# print(page)
	finally:
		browser.quit()


	soup = bsoup(page, 'html.parser')
	posts = soup.find_all('div', attrs={'class':'dbsr'})
	
	info = []
	for p in posts:

		title = p.find('div',{'class':'JheGif nDgy9d'}).get_text()
		link = p.find('a').get('href')
		#rso > div:nth-child(2) > g-card > div > div > div.dbsr > a
		description = p.find('div',{'class':'Y3v8qd'}).get_text()
		info.append({'title':title,'link':link,'desc':description})

	# print(info)
	return info

# getArticles()