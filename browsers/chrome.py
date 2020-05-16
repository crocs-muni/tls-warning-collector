from browsers.screenshot import screenshot_website
from selenium import webdriver

from misc.setup_logger import logger


def chrome(browser, version, case, package, url):
    """Opens Google Chrome and makes a screenshot of the desired website,"""
    logger.info("Preparing driver.")
    driver = webdriver.Chrome()
    driver.maximize_window()
    logger.info("Driver is set.")
    logger.info("Opening  {}".format(url))
    driver.get(url)
    try:
        screenshot_website(driver, browser, version, package, case)
    finally:
        logger.info("Closing the browsers.")
        driver.quit()
