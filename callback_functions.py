import sys

from screenshot import screenshot_website
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options


ScreenshotPathBase = "C:\\users\\username\\documents\\ssl\\screenshots"


def chrome_driver_version(v_number):
	"""Returns name of folder for chromedrivers given version"""
	short_version = ''
	if v_number == 75:
		short_version = '75'
	if v_number == 76:
		short_version = '76'
	if v_number == 75:
		short_version = '75'
	if v_number == 74:
		short_version = '74'
	if 72 <= v_number < 73:
		short_version = '2.46'
	if 70 <= v_number < 72:
		short_version = '2.45'
	if 68 <= v_number < 70:
		short_version = '2.42'
	if 66 <= v_number < 68:
		short_version = '2.40'
	if 64 <= v_number < 66:
		short_version = '2.37'
	if 62 <= v_number < 64:
		short_version = '2.35'
	if 60 <= v_number < 62:
		short_version = '2.33'
	if 58 <= v_number < 60:
		short_version = '2.30'
	if 56 <= v_number < 58:
		short_version = '2.29'
	if 54 <= v_number < 56:
		short_version = '2.27'
	if 52 <= v_number < 54:
		short_version = '2.24'
	if 50 <= v_number < 52:
		short_version = '2.22'
	if 48 <= v_number < 50:
		short_version = '2.21'
	if 46 <= v_number < 48:
		short_version = '2.20'
	if 43 <= v_number < 46:
		short_version = '2.18'
	if 40 <= v_number < 43:
		short_version = '2.15'
	if 36 <= v_number < 40:
		short_version = '2.12'
	if 34 <= v_number < 36:
		short_version = '2.10'
	if 32 <= v_number < 34:
		short_version = '2.9'
	if 30 <= v_number < 32:
		short_version = '2.8'
	if 29 <= v_number < 30:
		short_version = '2.6'
	return short_version


def opera_driver_version(v_number):
	"""Returns name of folder for operadrivers given version"""
	short_version = ''
	if v_number == 62:
		short_version = '75'
	if v_number == 60:
		short_version = '2.45'
	if v_number == 58:
		short_version = '2.42'
	if v_number == 57:
		short_version = '2.41'
	if v_number == 56:
		short_version = '2.40'
	if v_number == 55:
		short_version = '2.38'
	if v_number == 54:
		short_version = '2.37'
	if v_number == 53:
		short_version = '2.36'
	if v_number == 52:
		short_version = '2.35'
	if v_number == 50:
		short_version = '2.33'
	if v_number == 49:
		short_version = '2.32'
	if v_number == 48:
		short_version = '2.30'
	if v_number == 46:
		short_version = '2.29'
	if v_number == 38:
		short_version = '0.2.2'
	return short_version


def firefox(version, url):
	"""Opens Firefox and makes screenshot of desired website"""
	driver_path = 'C:\\Users\\IEUser\\Downloads\\drivers\\firefoxdrivers\\geckodriver-'
	short_version = ''
	exe = '\\geckodriver.exe'
	# Marionette is protocol used to communicate with Gecko Driver in versions 48 and higher.
	capabilities = {'marionette': True}
	# For Firefox 47 and lower the marionette needs to be set to False because it is not included.
	full_version = version.split(".")
	v_number = int(full_version[0])
	if full_version[0] == '62':
		short_version = '24'
	if 52 <= v_number < 62:
		short_version = '17'
	if 47 <= v_number < 52:
		short_version = '14'
	if v_number <= 47:
		short_version = '10'
		capabilities = {'marionette': False, 'acceptInsecureCerts': True}
	driver_path = driver_path + short_version + exe
	driver = webdriver.Firefox(executable_path=driver_path, capabilities=capabilities)
	driver.maximize_window()
	try:
		driver.get(url)
		screenshot_website(driver)
	except:
		screenshot_website(driver)
	finally:
		driver.quit()


def opera(version, url):
	"""Opens Opera and makes screenshot of desired website"""
	driver_path = 'C:\\Users\\IEUser\\Downloads\\drivers\\operadrivers\\operadriver-'
	full_version = version.split(".")
	v_number = int(full_version[0])
	short_version = opera_driver_version(v_number)
	driver_path = driver_path + short_version + '\\operadriver.exe'
	webdriver_service = service.Service(driver_path)
	webdriver_service.start()
	capabilities = {'operaOptions': {
		'binary': 'C:\\Users\\IEUser\\AppData\\Local\\Programs\\Opera\\' + get_version() + '\\opera.exe'}}
	driver = webdriver.Remote(webdriver_service.service_url, capabilities)
	driver.maximize_window()
	driver.get(url)
	try:
		screenshot_website(driver)
	finally:
		driver.close()
		driver.quit()


def chromium(version, url):
	"""Opens Chromium and makes screenshot of desired website"""
	driver_path = 'C:\\Users\\IEUser\\Downloads\\drivers\\chromedrivers\\chromedriver-'
	full_version = version().split(".")
	v_number = int(full_version[0])
	short_version = chrome_driver_version(v_number)
	driver_path = driver_path + short_version + '\\chromedriver.exe'
	opts = Options()
	opts.add_argument('--start-maximized')
	opts.binary_location = 'C:\\Program Files (x86)\\Chromium\\Application\\chrome.exe'
	driver = webdriver.Chrome(options=opts, executable_path=driver_path)
	driver.get(url)
	try:
		screenshot_website(driver, chromium=True)
	finally:
		driver.quit()


def chrome(version, url):
	"""Opens Google Chrome and makes screenshot of desired website"""
	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.get(url)
	try:
		screenshot_website(driver)
	finally:
		driver.quit()


def iexplorer(version, url):
	"""Opens Internet Explorer and makes screenshot of desired website"""
	driver = webdriver.Ie('C:\\Users\\IEUser\\Downloads\\IEDriverServer')
	driver.maximize_window()
	driver.get(url)
	try:
		screenshot_website(driver, ie=True)
	finally:
		driver.quit()


def edge(version, url):
	"""Opens Edge browser and makes screenshot of desired website"""
	capabilities = webdriver.DesiredCapabilities.EDGE.copy()
	driver = webdriver.Edge(executable_path=r'C:\\Users\\IEUser\\Downloads\\MicrosoftWebDriver')
	driver.maximize_window()
	driver.get(url)
	try:
		screenshot_website(driver, ie=True)
	finally:
		driver.quit()


def open_webpage(browser, url, version, package):
	"""Opens the URL in desired browser"""
	if browser == 'firefox':
		firefox(version, url)
	if browser == 'opera':
		opera(version, url)
	if package == 'chromium':
		chromium(version, url)
	if browser == 'chrome' and package != 'chromium':
		chrome(version, url)
	if browser == 'ie':
		iexplorer(version, url)
	if browser == 'edge':
		edge(version, url)
