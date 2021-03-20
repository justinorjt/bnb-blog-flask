# Pull in Kit Collections
from bs4 import BeautifulSoup as bsoup
from html.parser import HTMLParser
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium

def getKits():
	config = selenium.webdriver.ChromeOptions()
	config.add_argument('headless')
	browser = webdriver.Chrome(options=config) 

	
	theUrl = 'https://kit.co/rakidzich'
	browser.get(theUrl) 	
	# get the html and the link
	# wait = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return document.body.innerHTML;")
	# time.sleep(.7)
	try:

		WebDriverWait(browser, 5).until(
	        EC.presence_of_element_located((By.CSS_SELECTOR, "collection-card"))
	    )
		page = browser.page_source

	finally:
		browser.quit()

	soup = bsoup(page, 'html.parser')
	cards = soup.find_all('a', attrs={'class':'collection-card'})
	
	kits = []

	for card in cards:
		link = card.get('href')
		kits.append({"link":link})

	# print (kits)
	return kits


# getKits()