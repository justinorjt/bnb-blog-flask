# Pull in Youtube Videos
from bs4 import BeautifulSoup as bsoup
from html.parser import HTMLParser
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium

def getVideos():
	config = selenium.webdriver.ChromeOptions()
	config.add_argument('headless')
	browser = webdriver.Chrome(options=config) 

	
	theUrl = 'https://www.youtube.com/channel/UCvwmrPfn8ff-rTlc9YoH7Bg/videos'
	browser.get(theUrl)

	try:
		WebDriverWait(browser, 2).until(
	        EC.presence_of_element_located((By.CSS_SELECTOR, "h3.ytd-grid-video-renderer"))
	    )

		page = browser.page_source

	finally:
		browser.quit()

	
	soup = bsoup(page, 'html.parser')
	videos = soup.find_all('a', attrs={'id':'video-title'})
	# videos = browser.find_elements_by_id('video-title')
	vidLinks = []

	for vid in videos:
		# link = (vid.get_attribute('href'))
		link = vid.get('href')
		code = link.split("=")[1]
		vidLinks.append({"video":code})

	# print (vidLinks)
	return (vidLinks)


# getVideos()