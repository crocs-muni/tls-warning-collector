from screenshot import screenshot_website
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import InsecureCertificateException
from setup_logger import logger
import os

CURRENT_DIR = os.getcwd()


def chrome_driver_version(v_number):
    """Returns the folder name for chromedrivers of the given version."""
    logger.info('Getting chromedriver version.')
    driver_version = ''
    if v_number == 76:
        driver_version = '76'
    if v_number == 75:
        driver_version = '75'
    if v_number == 74:
        driver_version = '74'
    if 72 <= v_number < 73:
        driver_version = '2.46'
    if 70 <= v_number < 72:
        driver_version = '2.45'
    if 68 <= v_number < 70:
        driver_version = '2.42'
    if 66 <= v_number < 68:
        driver_version = '2.40'
    if 64 <= v_number < 66:
        driver_version = '2.37'
    if 62 <= v_number < 64:
        driver_version = '2.35'
    if 60 <= v_number < 62:
        driver_version = '2.33'
    if 58 <= v_number < 60:
        driver_version = '2.30'
    if 56 <= v_number < 58:
        driver_version = '2.29'
    if 54 <= v_number < 56:
        driver_version = '2.27'
    if 52 <= v_number < 54:
        driver_version = '2.24'
    if 50 <= v_number < 52:
        driver_version = '2.22'
    if 48 <= v_number < 50:
        driver_version = '2.21'
    if 46 <= v_number < 48:
        driver_version = '2.20'
    if 43 <= v_number < 46:
        driver_version = '2.18'
    if 40 <= v_number < 43:
        driver_version = '2.15'
    if 36 <= v_number < 40:
        driver_version = '2.12'
    if 34 <= v_number < 36:
        driver_version = '2.10'
    if 32 <= v_number < 34:
        driver_version = '2.9'
    if 30 <= v_number < 32:
        driver_version = '2.8'
    if v_number < 30:
        driver_version = '2.6'
    logger.info('Chromedriver version - %s.', driver_version)
    return driver_version


def opera_driver_version(v_number):
    """Returns the folder name for operadrivers of the given version."""
    logger.info('Getting operadriver version.')
    driver_version = ''
    if 60 < v_number <= 62:
        driver_version = '75'
    if 58 < v_number <= 60:
        driver_version = '2.45'
    if v_number == 58:
        driver_version = '2.42'
    if v_number == 57:
        driver_version = '2.41'
    if v_number == 56:
        driver_version = '2.40'
    if v_number == 55:
        driver_version = '2.38'
    if v_number == 54:
        driver_version = '2.37'
    if v_number == 53:
        driver_version = '2.36'
    if 50 < v_number <= 52:
        driver_version = '2.35'
    if v_number == 50:
        driver_version = '2.33'
    if v_number == 49:
        driver_version = '2.32'
    if v_number == 48:
        driver_version = '2.30'
    if v_number == 47:
        driver_version = '2.30'
    if 42 < v_number <= 46:
        driver_version = '2.29'
    # version 44 is not on the server so cannot be downloaded
    if 40 < v_number <= 42:
        driver_version = '2.27'
    if v_number <= 40:
        driver_version = '0.2.2'
    logger.info('Operadriver version - %s.', driver_version)
    return driver_version


def firefox(browser, version, case, package, url):
    """Opens Firefox and makes a screenshot of the desired website."""
    logger.info('Preparing driver path.')
    driver_path = CURRENT_DIR + '\\drivers\\firefoxdrivers\\geckodriver-'
    driver_version = ''
    exe = '\\geckodriver.exe'
    logger.info('Driver path set to - %s', driver_path)
    # Marionette is protocol used to communicate with Gecko Driver in versions 48 and higher.
    capabilities = {'marionette': True}
    # For Firefox 47 and lower the marionette needs to be set to False because it is not included.
    logger.info('Parsing browser full version to short.')
    full_version = version.split(".")
    v_number = int(full_version[0])
    logger.info('Browser short version - %s', v_number)
    logger.info('Getting geckodriver version.')
    if full_version[0] >= '62':
        driver_version = '24'
    if 52 <= v_number < 62:
        driver_version = '17'
    if 47 <= v_number < 52:
        driver_version = '14'
    if v_number <= 47:
        driver_version = '10'
        capabilities = {'marionette': False, 'acceptInsecureCerts': True}
    logger.info('Geckodriver version - %s.', driver_version)
    logger.info('Capabilities are set to - %s', capabilities)
    driver_path = driver_path + driver_version + str(exe)
    logger.info('Preparing driver.')
    driver = webdriver.Firefox(executable_path=driver_path, capabilities=capabilities)
    driver.maximize_window()
    logger.info('Driver is set.')
    try:
        logger.info('Opening %s', url)
        driver.get(url)
        logger.info('Going to make screenshot.')
        screenshot_website(driver, browser, version, package, case)
    except InsecureCertificateException:
        logger.error('Insecure certificate exception from Selenium but should create a screenshot.')
        screenshot_website(driver, browser, version, package, case)
    finally:
        logger.info('Closing the browser.')
        driver.quit()


def opera(browser, version, case, package, url):
    """Opens Opera and makes a screenshot of the desired website."""
    logger.info('Preparing driver path.')
    driver_path = CURRENT_DIR + '\\drivers\\operadrivers\\operadriver-'
    logger.info('Driver path set.')
    logger.info('Parsing browser full version to short.')
    full_version = version.split(".")
    v_number = int(full_version[0])
    logger.info('Browser short version - %s', v_number)
    old_opera = False
    suffix = False
    suffix_old = '_0'
    driver_version = opera_driver_version(v_number)
    logger.info('Checking if the Opera driver version is "0.2.2"')
    if driver_version == '0.2.2':
        old_opera = True
    if 40 <= v_number < 43:
        suffix = True
    logger.info('Preparing driver.')
    driver_path = driver_path + driver_version + '\\operadriver.exe'
    webdriver_service = service.Service(driver_path)
    webdriver_service.start()
    if suffix:
        capabilities = {'operaOptions': {
            'binary': 'C:\\Users\\IEUser\\AppData\\Local\\Programs\\Opera\\' + version + suffix_old + '\\opera.exe'}}
    else:
        logger.info('Capabilities are set.')
        capabilities = {'operaOptions': {
            'binary': 'C:\\Users\\IEUser\\AppData\\Local\\Programs\\Opera\\' + version + '\\opera.exe'}}
    logger.info('Preparing driver.')
    driver = webdriver.Remote(webdriver_service.service_url, capabilities)
    driver.maximize_window()
    logger.info('Driver is set.')
    logger.info('Opening %s', url)
    driver.get(url)
    try:
        if old_opera:
            screenshot_website(driver, browser, version, package, case, opera_new=False, opera_old=True)
        else:
            screenshot_website(driver, browser, version, package, case, opera_old=False, opera_new=True)
    finally:
        logger.info('Closing the browser.')
        driver.quit()


def chromium(browser, version, case, package, url):
    """Opens Chromium and makes a screenshot of the desired website."""
    logger.info('Preparing driver path.')
    driver_path = CURRENT_DIR + '\\drivers\\chromedrivers\\chromedriver-'
    logger.info('Driver path set.')
    logger.info('Parsing browser full version to short.')
    full_version = version.split(".")
    v_number = int(full_version[0])
    logger.info('Browser short version - %s', v_number)
    driver_version = chrome_driver_version(v_number)
    logger.info('Preparing driver.')
    driver_path = driver_path + driver_version + '\\chromedriver.exe'
    logger.info('Setting chromium options.')
    opts = Options()
    opts.add_argument('--start-maximized')
    opts.binary_location = 'C:\\Program Files (x86)\\Chromium\\Application\\chrome.exe'
    driver = webdriver.Chrome(options=opts, executable_path=driver_path)
    logger.info('Driver is set.')
    logger.info('Opening %s', url)
    driver.get(url)
    try:
        screenshot_website(driver, browser, version, package, case, chromium=True)
    finally:
        logger.info('Closing the browser.')
        driver.quit()


def chrome(browser, version, case, package, url):
    """Opens Google Chrome and makes a screenshot of the desired website,"""
    logger.info('Preparing driver.')
    driver = webdriver.Chrome()
    driver.maximize_window()
    logger.info('Driver is set.')
    logger.info('Opening %s', url)
    driver.get(url)
    try:
        screenshot_website(driver, browser, version, package, case)
    finally:
        logger.info('Closing the browser.')
        driver.quit()


def iexplorer(browser, version, case, package, url):
    """Opens Internet Explorer and makes a screenshot of the desired website."""
    logger.info('Preparing driver.')
    driver = webdriver.Ie('C:\\Users\\IEUser\\Downloads\\IEDriverServer')
    driver.maximize_window()
    logger.info('Driver is set.')
    logger.info('Opening %s', url)
    driver.get(url)
    try:
        screenshot_website(driver, browser, version, package, case, ie=True)
    finally:
        logger.info('Closing the browser.')
        driver.quit()


def edge(browser, version, case, package, url):
    """Opens Edge browser and makes a screenshot of the desired website."""
    capabilities = webdriver.DesiredCapabilities.EDGE.copy()
    logger.info('Preparing driver.')
    driver = webdriver.Edge(executable_path=r'C:\\Users\\IEUser\\Downloads\\MicrosoftWebDriver')
    driver.maximize_window()
    logger.info('Driver is set.')
    logger.info('Opening %s', url)
    driver.get(url)
    try:
        screenshot_website(driver, browser, version, package, case, ie=True)
    finally:
        logger.info('Closing the browser.')
        driver.quit()


def open_webpage(browser, url, case, version, package):
    """Opens the URL in desired browser."""
    if browser == 'firefox':
        firefox(browser, version, case, package, url)
    if browser == 'opera':
        opera(browser, version, case, package, url)
    if package == 'chromium':
        chromium(browser, version, case, package, url)
    if browser == 'chrome' and package != 'chromium':
        chrome(browser, version, case, package, url)
    if browser == 'ie':
        iexplorer(browser, version, case, package, url)
    if browser == 'edge':
        edge(browser, version, case, package, url)
