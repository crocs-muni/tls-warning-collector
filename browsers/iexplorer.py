from misc.setup_logger import logger
from browsers.screenshot import screenshot_website
from selenium import webdriver


def iexplorer(browser, version, case, package, url):
    """Opens Internet Explorer and makes a screenshot of the desired website."""
    logger.info("Preparing driver.")
    driver = webdriver.Ie("C:\\Users\\IEUser\\Downloads\\IEDriverServer")
    driver.maximize_window()
    logger.info("Driver is set.")
    logger.info("Opening {}".format(url))
    driver.get(url)
    try:
        screenshot_website(driver, browser, version, package, case, ie=True)
    finally:
        logger.info("Closing the browsers.")
        driver.quit()
