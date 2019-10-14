from screenshot import screenshot_website, kill_browser
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
from setup_logger import logger
import os
import multiprocessing

CURRENT_DIR = os.getcwd()


def firefox(browser, version, case, package, url):
    """Opens Firefox and makes a screenshot of the desired website."""
    v_number = parse_browser_version(version)
    driver_path = set_firefox_driver_path(v_number)
    capabilities = set_firefox_capabilities(v_number)
    driver = set_firefox_driver(driver_path, capabilities)
    try:
        open_browser(driver, url)
        screenshot_website(driver, browser, version, package, case)
    except Exception as e:
        logger.error('Exception from Selenium but going to take a screenshot. -- %s', e)
        screenshot_website(driver, browser, version, package, case)
    finally:
        driver.quit()
        kill_browser()


def parse_browser_version(version):
    """Parsing the whole version string to the first part only."""
    logger.info('Parsing browser full version to short.')
    full_version = version.split(".")
    v_number = int(full_version[0])
    logger.info('Browser short version - %s', v_number)
    return v_number


def set_firefox_driver_path(v_number):
    """Setting Firefox driver path."""
    logger.info('Preparing driver path.')
    driver_version = set_firefox_driver_version(v_number)
    driver_path = CURRENT_DIR + '\\drivers\\firefoxdrivers\\geckodriver-' + driver_version + '\\geckodriver.exe'
    logger.info('Driver path set to - %s', driver_path)
    return driver_path


def set_firefox_driver_version(v_number):
    """Setting Firefox driver version."""
    driver_version = ''
    logger.info('Getting geckodriver version.')
    if v_number >= 62:
        driver_version = '24'
    if 52 <= v_number < 62:
        driver_version = '17'
    if 47 <= v_number < 52:
        driver_version = '14'
    if v_number < 47:
        driver_version = '10'
    logger.info('Geckodriver version - %s.', driver_version)
    return driver_version


def set_firefox_capabilities(v_number):
    """Setting Firefox capabilities."""
    # Marionette is protocol used to communicate with Gecko Driver in versions 48 and higher.
    capabilities = DesiredCapabilities.FIREFOX
    capabilities['marionette'] = True
    capabilities['acceptInsecureCerts'] = False
    capabilities['acceptSslCerts'] = False
    # For Firefox 47 and lower the marionette needs to be set to False because it is not included.
    if v_number < 47:
        capabilities['marionette'] = False
    logger.info('Capabilities are set to - %s', capabilities)
    return capabilities


def set_firefox_driver(driver_path, capabilities):
    """Setting Firefox driver to be able to open URL."""
    logger.info('Preparing driver.')
    driver = webdriver.Firefox(executable_path=driver_path, capabilities=capabilities)
    driver.maximize_window()
    logger.info('Driver is set.')
    return driver


def open_browser(driver, url):
    """Opens given url in the browser."""
    logger.info('Opening %s', url)
    try:
        driver.get(url)
        driver.save_screenshot('C:\\Users\\IEUser\\Desktop\\screenshot.png')
    except Exception as e:
        logger.error("Error in open_browser(): %s", e)


def opera(browser, version, case, package, url):
    """Opens Opera and makes a screenshot of the desired website."""
    v_number = parse_browser_version(version)
    old_opera = check_opera_if_old(v_number)
    old_driver = v_number < 42
    driver_path = set_opera_driver_path(v_number)
    capabilities = set_opera_capabilities(old_opera, version)
    driver = set_opera_driver(driver_path, capabilities)
    try:
        open_opera(driver, url, browser, version, package, case, old_driver=old_driver)
    except Exception as e:
        logger.error('Exception in opera() - %s', e)
    finally:
        driver.quit()
        kill_browser()


def check_opera_if_old(v_number):
    """Checking if Opera version is lower or equal to '40'."""
    logger.info('Checking if the Opera version is lower or equal to 40')
    if v_number <= 40:
        logger.info('Opera version is using old driver. - True')
        return True
    return False


def set_opera_driver_path(v_number):
    """Setting Opera driver path."""
    logger.info('Preparing driver path.')
    driver_version = set_opera_driver_version(v_number)
    driver_path = CURRENT_DIR + '\\drivers\\operadrivers\\operadriver-' + driver_version + '\\operadriver.exe'
    logger.info('Driver path set.')
    return driver_path


def set_opera_driver_version(v_number):
    """Returns the folder name for operadrivers of the given version."""
    logger.info('Getting operadriver version.')
    driver_version = ''
    if v_number >= 63:
        driver_version = '76'
    if v_number == 62:
        driver_version = '2.41'
    if 58 < v_number < 62:
        driver_version = '2.45'
    if 56 < v_number <= 58:
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
        driver_version = '2.33'
    if v_number == 48:
        driver_version = '2.30'
    if v_number == 47:
        driver_version = '2.30'
    if 42 < v_number <= 46:
        driver_version = '2.29'
    if 40 < v_number <= 42:
        driver_version = '2.27'
    if 26 < v_number <= 40:
        driver_version = '0.2.2'
    if v_number == 26:
        driver_version = '0.2.0'
    if v_number <= 25:
        driver_version = '0.1.0'
    logger.info('Operadriver version - %s.', driver_version)
    return driver_version


def set_opera_capabilities(old_opera, version):
    """Setting capabilities for Opera."""
    logger.info('Setting capabilities.')
    v_number = parse_browser_version(version)
    opts = Options()
    if v_number > 40:
        # In older version these switches do not work, but alerts are there by default.
        opts.add_experimental_option('excludeSwitches', ['ignore-certificate-errors', 'ignore-ssl-errors'])
    capabilities = DesiredCapabilities.OPERA
    capabilities.update(opts.to_capabilities())
    capabilities['acceptInsecureCerts'] = False
    capabilities['acceptSslCerts'] = False
    capabilities['operaOptions'] = {'binary': 'C:\\Program Files\\Opera\\' + version + '\\opera.exe'}
    logger.info('Capabilities are set.')
    return capabilities


def set_opera_driver(driver_path, capabilities):
    """Setting Opera driver."""
    logger.info('Preparing driver.')
    webdriver_service = service.Service(driver_path)
    webdriver_service.start()
    driver = webdriver.Remote(webdriver_service.service_url, capabilities)
    driver.maximize_window()
    logger.info('Driver is set.')
    return driver


def open_opera(driver, url, browser, version, package, case, old_driver=False):
    """Run screenshot in different thread."""
    try:
        if old_driver:
            timeout_and_screenshot(driver, url, browser, version, package, case)
        else:
            open_browser(driver, url)
            screenshot_website(driver, browser, version, package, case)
    except Exception as e:
        logger.error("Error in open_opera: %s". e)


def timeout_and_screenshot(driver, url, browser, version, package, case):
    """Opens the url in different thread so that it is not waiting until the page is loaded."""
    try:
        p1 = multiprocessing.Process(name='p1', target=open_browser, args=(driver, url))
        p2 = multiprocessing.Process(name='p2', target=screenshot_website, args=(driver, browser, version, package, case, True, False))
        logger.info('Starting process for screenshot_website.')
        p2.start()
        logger.info('Starting process for open_browser.')
        p1.start()
        #p2.join()
        #p1.join(1)
        # Wait for 1 seconds or unitl process finishes
        logger.info('Going to take screenshot from timeout_and_screenshot.')
    except Exception as e:
        logger.error("Exception in multiprocessing: %s", e)
    finally:
        logger.info('Checking if thread is active')
        terminate_thread(p1)
        terminate_thread(p2)


def terminate_thread(thread):
    """Terminate the thread."""
    if thread.is_alive():
        logger.info('Terminating the thread')
        thread.terminate()
        thread.join()


def chromium(browser, version, case, package, url):
    """Opens Chromium and makes a screenshot of the desired website."""
    v_number = parse_browser_version(version)
    driver_path = set_chromium_driver_path(v_number)
    old_driver = v_number < 74
    capabilities = set_chromium_capabilities()
    driver = set_chromium_driver(driver_path, capabilities)
    try:
        open_chromium(driver, url, browser, version, package, case, old_driver=old_driver)
    except Exception as e:
        logger.error('Exception in chromium() - %s', e)
    finally:
        driver.quit()
        kill_browser()


def set_chromium_driver_path(v_number):
    """Setting driver path for Chromium."""
    logger.info('Preparing driver path.')
    driver_version = set_chrome_driver_version(v_number)
    driver_path = CURRENT_DIR + '\\drivers\\chromedrivers\\chromedriver-' + driver_version + '\\chromedriver.exe'
    logger.info('Driver path set.')
    return driver_path


def set_chrome_driver_version(v_number):
    """Returns the folder name for chromedrivers of the given version."""
    logger.info('Getting chromedriver version.')
    driver_version = ''
    if v_number >= 78:
        driver_version = '78'
    if v_number == 77:
        driver_version = '77'
    if v_number == 76:
        driver_version = '76'
    if v_number == 75:
        driver_version = '75'
    if v_number == 74:
        driver_version = '74'
    if 72 <= v_number < 74:
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
    if 46 <= v_number < 54:
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


def set_chromium_capabilities():
    """Setting capabilities for Chromium."""
    logger.info('Setting chromium capabilities.')
    opts = Options()
    opts.binary_location = 'C:\\Program Files (x86)\\Chromium\\Application\\chrome.exe'
    opts.add_experimental_option('excludeSwitches', ['ignore-certificate-errors', 'ignore-ssl-errors'])
    capabilities = DesiredCapabilities.CHROME
    capabilities.update(opts.to_capabilities())
    capabilities['acceptInsecureCerts'] = False
    capabilities['acceptSslCerts'] = False
    return capabilities


def set_chromium_driver(driver_path, capabilities):
    """Setting Chromium driver with special windows size. Otherwise it won't open maximized in older versions."""
    driver = webdriver.Chrome(desired_capabilities=capabilities, executable_path=driver_path)
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    logger.info('Driver is set.')
    return driver


def open_chromium(driver, url, browser, version, package, case, old_driver=False):
    """Runs the screenshot funciton in a different thread."""
    try:
        if old_driver:
            #open_browser(driver, url)
            timeout_and_screenshot(driver, url, browser, version, package, case)
        else:
            open_browser(driver, url)
            screenshot_website(driver, browser, version, package, case)
    except Exception as e:
        logger.error("Error in open_chromium: %s". e)
        


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
