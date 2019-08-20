# Pull in Kit Collections
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

	
	theUrl = 'https://kit.com/rakidzich'
	browser.get(theUrl) 	
	# get the html and the link
	# wait = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return document.body.innerHTML;")
	# time.sleep(.7)

	WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "collection-card"))
    )

	cards = browser.find_elements_by_class_name('collection-card')
	
	kits = []

	for card in cards:
		link = (card.get_attribute('href'))
		kits.append({"link":link})

	# print (kits)
	return (kits)
	browser.quit()


# getKits()