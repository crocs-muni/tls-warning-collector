import os
from misc.setup_logger import logger
from misc.browser import Driver, open_browser
from browsers.screenshot import screenshot_website
from selenium import webdriver

CURRENT_DIR = os.getcwd()


class IEDriver(Driver):
    """
    Class that represents Edge Driver
    """

    def set_driver_path(self):
        """
        Set a correct PATH to the Selenium Web driver
        :return: None
        """
        logger.info("Preparing driver path.")
        self.path = CURRENT_DIR + "\\drivers\\IEDriverServer"
        logger.info("Driver path set to - {}".format(self.path))

    def create_ie_driver(self):
        """
        Setting Edge driver to be able to open URL.
        :return: None
        """
        logger.info("Preparing driver.")
        driver = webdriver.Ie(self.path)
        driver.maximize_window()
        logger.info("Driver is set.")
        return driver


def iexplorer(browser):
    """
    Opens Internet Explorer and makes a screenshot of the desired website.
    :param browser: Browser
    :return: None
    """
    ie_driver = prepare_driver()
    driver = ie_driver.create_ie_driver()
    try:
        open_browser(driver, browser.url)
        screenshot_website(driver, browser, ie=True)
    finally:
        logger.info("Closing the browsers.")
        driver.quit()


def prepare_driver():
    """
    Preparing EdgeDriver to run Edge via Selenium
    :return: Driver object ready to be used
    """
    driver = IEDriver("", 0, None)
    driver.set_driver_path()
    return driver
