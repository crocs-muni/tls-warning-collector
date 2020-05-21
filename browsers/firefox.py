from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from misc.browser import parse_browser_version, open_browser
from browsers.screenshot import screenshot_website, kill_browser
from misc.setup_logger import logger
import os

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
        logger.error("Exception from Selenium but going to take a screenshot. -- {}".format(e))
        screenshot_website(driver, browser, version, package, case)
    finally:
        driver.quit()
    kill_browser()


def set_firefox_driver_path(v_number):
    """Setting Firefox driver path."""
    logger.info("Preparing driver path.")
    driver_version = set_firefox_driver_version(v_number)
    driver_path = CURRENT_DIR + "\\drivers\\firefoxdrivers\\geckodriver-" + driver_version + "\\geckodriver.exe"
    logger.info("Driver path set to - {}".format(driver_path))
    return driver_path


def set_firefox_driver_version(v_number):
    """Setting Firefox driver version."""
    driver_version = ""
    logger.info("Getting geckodriver version.")
    if v_number >= 62:
        driver_version = "24"
    if 52 <= v_number < 62:
        driver_version = "17"
    if 47 <= v_number < 52:
        driver_version = "14"
    if v_number < 47:
        driver_version = "11"
    logger.info("Geckodriver version - {}".format(driver_version))
    return driver_version


def set_firefox_capabilities(v_number):
    """Setting Firefox capabilities."""
    # Marionette is protocol used to communicate with Gecko Driver in versions 48 and higher.
    capabilities = DesiredCapabilities.FIREFOX
    capabilities["marionette"] = True
    capabilities["acceptInsecureCerts"] = False
    capabilities["acceptSslCerts"] = False
    # For Firefox 47 and lower the marionette needs to be set to False because it is not included.
    if v_number < 47:
        capabilities["marionette"] = False
    logger.info("Capabilities are set to - {}".format(capabilities))
    return capabilities


def set_firefox_driver(driver_path, capabilities):
    """Setting Firefox driver to be able to open URL."""
    logger.info("Preparing driver.")
    driver = webdriver.Firefox(executable_path=driver_path, capabilities=capabilities)
    driver.maximize_window()
    logger.info("Driver is set.")
    return driver
