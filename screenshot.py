from PIL import ImageGrab
import os
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from main import *

output = sys.stdout
sys.stdout = open("log.txt", "w")
ScreenshotPathBase = "C:\\users\\username\\documents\\ssl\\screenshots"


def save_screenshot(path):
	"""Saves the screenshot into correct path."""
	snapshot = ImageGrab.grab()
	snapshot.save(path)


def get_screenshot_path(path, browser, version, case):
	"""Gets path for browser directory where screenshot will be saved."""
	directory = path + '/browsers' + '/' + browser + '/' + version
	if not os.path.exists(directory):
		os.makedirs(directory)
	screenshot_name = case + '.png'
	screenshot_path = directory + '/' + screenshot_name
	return screenshot_path


def get_screenshot_case_path(path, browser, version, case):
	"""Gets path for case directory where screenshot will be saved."""
	directory = path + '/cases' + '/' + case + '/' + browser
	if not os.path.exists(directory):
		os.makedirs(directory)
	screenshot_name = version + '.png'
	screenshot_path = directory + '/' + screenshot_name
	return screenshot_path


def screenshot_website(driver, chromium=False, ie=False, opera_new=False, opera_old=False):
	"""Makes screenshot of the opened website."""
	print("Starting screenshot website")
	print("Opera new is: ", opera_new)
	print("Opera old is: ", opera_old)
	# ID for internet explorer page
	id_ie = "invalidcert_mainTitle"
	# ID for other browsers page
	id_other = "content"
	if ie:
		final_id = id_ie
	else:
		final_id = id_other
	# If alert window appears, Accept and continue to the website.
	if opera_old:	
		try:
			print("Inside if opera is true.\r\n")
			webdriver.ActionChains(driver).send_keys(Keys.LEFT).perform()
			webdriver.ActionChains(driver).send_keys(Keys.RETURN).perform()
			print("Sent Keys.\r\n")
		except:
			pass
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, final_id)))
	time.sleep(2)
	if chromium:
		save_screenshot(get_screenshot_path(ScreenshotPathBase, get_package(), get_version(), get_case()))
		save_screenshot(get_screenshot_case_path(ScreenshotPathBase, get_package(), get_version(), get_case()))
	else:
		save_screenshot(get_screenshot_path(ScreenshotPathBase, get_browser(), get_version(), get_case()))
		save_screenshot(get_screenshot_case_path(ScreenshotPathBase, get_browser(), get_version(), get_case()))
		webdriver.ActionChains(driver).send_keys(Keys.TAB + Keys.TAB + Keys.TAB + Keys.RIGHT + Keys.RETURN).perform()
		time.sleep(3)
		if opera_new:
			print("Sending keys.")
			webdriver.ActionChains(driver).send_keys(Keys.ALT + Keys.F4).perform()
			print("Keys sent.")
		sys.stdout.close()