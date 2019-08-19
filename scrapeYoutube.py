# Pull in Youtube Videos
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

	
	# theUrl = 'https://kit.com/rakidzich'
	theUrl = 'https://www.youtube.com/channel/UCvwmrPfn8ff-rTlc9YoH7Bg/videos'
	browser.get(theUrl) 	
	# get the html and the link
	# wait = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return document.body.innerHTML;")
	# time.sleep(.7)

	WebDriverWait(browser, 2).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3.ytd-grid-video-renderer"))
    )

	# cards = browser.find_elements_by_class_name('collection-card')
	# videos = browser.find_elements_by_class_name('yt-simple-endpoint')
	videos = browser.find_elements_by_id('video-title')
	# yt-simple-endpoint
	
	vidLinks = []

	for vid in videos:
		link = (vid.get_attribute('href'))
		code = link.split("=")[1]
		vidLinks.append(code)

	# print (vidLinks)
	return (vidLinks)
	browser.quit()


# getVideos()