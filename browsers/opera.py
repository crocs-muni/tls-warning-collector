from selenium.webdriver import DesiredCapabilities
from browser import parse_browser_version, open_browser
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
from browsers.screenshot import screenshot_website, kill_browser
import multiprocessing
import time
from setup_logger import logger
import os

CURRENT_DIR = os.getcwd()


def opera(browser, version, case, package, url):
    """Opens Opera and makes a screenshot of the desired website."""
    v_number = parse_browser_version(version)
    old_opera = check_opera_if_old(v_number)
    driver_path = set_opera_driver_path(v_number)
    capabilities = set_opera_capabilities(old_opera, version)
    driver = set_opera_driver(driver_path, capabilities)
    time.sleep(2)
    try:
        open_opera(driver, url, browser, version, package, case, old_driver=old_opera)
    except Exception as e:
        logger.error('Exception in opera(): - %s', e)
    finally:
        driver.quit()
        kill_browser()


def check_opera_if_old(v_number):
    """Checking if Opera version is lower or equal to '40'."""
    logger.info('Checking if the Opera version is lower or equal to 40')
    if v_number <= 57:
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
            logger.info('Starting timeout_and_screenshot.')
            timeout_and_screenshot(driver, url, browser, version, package, case)
        else:
            open_browser(driver, url)
            screenshot_website(driver, browser, version, package, case)
    except Exception as e:
        logger.error("Error in open_opera: %s", e)


def timeout_and_screenshot(driver, url, browser, version, package, case):
    """Opens the url in different thread so that it is not waiting until the page is loaded."""
    try:
        p1 = multiprocessing.Process(name='p1', target=open_browser, args=(driver, url))
        logger.info('Starting process for open_browser.')
        p1.start()
        p1.join(3)
        logger.info('Going to take screenshot from timeout_and_screenshot.')
        if opera:
            screenshot_website(driver, browser, version, package, case, True, False)
    except Exception as e:
        logger.error("Exception in multiprocessing: %s", e)
    finally:
        logger.info('Checking if thread is active')
        terminate_thread(p1)


def terminate_thread(thread):
    """Terminate the thread."""
    if thread.is_alive():
        logger.info('Terminating the thread')
        thread.terminate()
        thread.join()
