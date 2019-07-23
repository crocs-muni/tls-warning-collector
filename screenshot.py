from PIL import ImageGrab
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

ScreenshotPathBase = "C:\\users\\username\\documents\\ssl\\screenshots"

def save_screenshot(path):
	'''Saves the screenshot into correct path.'''
	snapshot = ImageGrab.grab()
	snapshot.save(path)


def get_browser():
	'''Gets browser binary.'''
	args = sys.argv[1:]
	browser = str(args[0])
	return browser


def get_package():
	'''Gets browser package. In case of Chromium it is important because binary is chrome.'''
	args = sys.argv[1:]
	package = str(args[4])
	return package


def get_version():
	'''Gets browser version.'''
	args = sys.argv[1:]
	version = str(args[1])
	return version


def get_case():
	'''Gets case of SSL.'''
	args = sys.argv[1:]
	case = str(args[2])
	return case 


def get_case_url():
	'''Gets URL for the required SSL warning page.'''
	args = sys.argv[1:]
	url = str(args[3])
	return url 


def get_screenshot_path(path, browser, version, case):
	'''Gets path for browser directory where screenshot will be saved.'''
	directory = path + '/browsers' + '/' + browser + '/' + version
	if not os.path.exists(directory):
		os.makedirs(directory)
	screenshot_name = case + '.png'
	screenshot_path = directory + '/' + screenshot_name
	return screenshot_path


def get_screenshot_case_path(path, browser, version, case):
	'''Gets path for case directory where screenshot will be saved.'''
	directory = path + '/cases' + '/' + case + '/' + browser
	if not os.path.exists(directory):
		os.makedirs(directory)
	screenshot_name = version + '.png'
	screenshot_path = directory + '/' + screenshot_name
	return screenshot_path


def open_webpage(browser, url, version, package):
	'''Opens the URL in desired browser'''
	if browser == 'firefox':
		driver_path = 'C:\\Users\\IEUser\\Downloads\\geckodriver-'
		version = ''
		exe = '\\geckodriver.exe' 
		# Marionette is protocol used to communicate with Gecko Driver in versions 48 and higher.
		capabilities = {'marionette': True}
		# For Firefox 47 and lower the marionette needs to be set to False because it is not included.
		full_version = get_version().split(".")
		if full_version[0] == '62':
			version = '24'
		if full_version[0] == '52':
			version = '14'
		if full_version[0] == '45':
			version = '8'
			capabilities = {'marionette': False}
		driver_path = driver_path + version + exe
		driver = webdriver.Firefox(executable_path=driver_path, capabilities=capabilities)
		driver.maximize_window()
		driver.get(url)
		try:
			screenshot_website(driver) 
		finally:
			driver.quit()
	if browser == 'opera':
		driver_path = 'C:\\Users\\IEUser\\Downloads\\operadriver-'
		version = ''
		full_version = get_version().split(".")
		if full_version[0] == '56':
			version = '2.40'
		if full_version[0] == '46':
			version = '2.29'
		if full_version[0] == '38':
			version = '0.2.2'
		driver_path = driver_path + version + '\\operadriver.exe'
		webdriver_service = service.Service(driver_path)
		webdriver_service.start()
		capabilities = {'operaOptions': {'binary': 'C:\\Users\\IEUser\\AppData\\Local\\Programs\\Opera\\'+ get_version() +'\\opera.exe'}}
		driver = webdriver.Remote(webdriver_service.service_url, capabilities)
		driver.maximize_window()
		driver.get(url)
		try:
			screenshot_website(driver)
		finally:
			driver.close()
			driver.quit()
	if package == 'chromium':
		driver_path = 'C:\\Users\\IEUser\\Downloads\\chromedriver-'
		version = ''
		full_version = get_version().split(".")
		if full_version[0] == '75':
			version = '75'
		if full_version[0] == '71':
			version = '71'
		if full_version[0] == '67':
			version = '67'
		if full_version[0] == '34':
			version = '2.10'
		if full_version[0] == '41':
			version = '2.15'
		driver_path = driver_path + version + '\\chromedriver.exe'
		opts = Options()
		opts.add_argument('--start-maximized')
		opts.binary_location = 'C:\\Program Files (x86)\\Chromium\\Application\\chrome.exe'
		driver = webdriver.Chrome(options=opts, executable_path=driver_path)
		driver.get(url)
		try:
			screenshot_website(driver, chromium=True)
		finally:
			driver.quit()
	if browser == 'chrome' and package != 'chromium':
		driver = webdriver.Chrome()
		driver.maximize_window()
		driver.get(url)
		try:
			screenshot_website(driver)
		finally:
			driver.quit()
	if browser == 'ie':
		driver = webdriver.Ie('C:\\Users\\IEUser\\Downloads\\IEDriverServer')
		driver.maximize_window()
		driver.get(url)
		try:
			screenshot_website(driver, ie=True)
		finally:
			driver.quit()
	if browser == 'edge':
		capabilities = webdriver.DesiredCapabilities.EDGE.copy()
		driver = webdriver.Edge(executable_path=r'C:\\Users\\IEUser\\Downloads\\MicrosoftWebDriver')
		driver.maximize_window()
		driver.get(url)
		try:
			screenshot_website(driver, ie=True)
		finally:
			driver.quit()


def screenshot_website(driver, chromium=False, ie=False):
	'''Makes screenshot of the opened website.'''
	id_ie = "invalidcert_mainTitle"
	id_other = "content"
	final_id = ''
	if ie:
		final_id = id_ie
	else:
		final_id = id_other
	# If alert window appears, Accept and continue to the website.
	try:
		WebDriverWait(driver, 3).until(EC.alert_is_present())
		alert = driver.switchTo().alert()
		alert.accept()
	except:
		pass
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, final_id)))
	time.sleep(2)
	if chromium:
		save_screenshot(get_screenshot_path(ScreenshotPathBase, get_package(), get_version(), get_case()))
		save_screenshot(get_screenshot_case_path(ScreenshotPathBase, get_package(), get_version(), get_case()))
	else:
		save_screenshot(get_screenshot_path(ScreenshotPathBase, get_browser(), get_version(), get_case()))
		save_screenshot(get_screenshot_case_path(ScreenshotPathBase, get_browser(), get_version(), get_case()))


def save_all_screenshots():
	'''Function which makes it all work as a one function.'''
	open_webpage(get_browser(), get_case_url(), get_version(), get_package())
	
if __name__ == '__main__':
    save_all_screenshots()
