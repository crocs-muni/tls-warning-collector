import os
from browsers.screenshot import screenshot_website
from selenium import webdriver
from misc.browser import Driver, open_browser
from misc.setup_logger import logger

CURRENT_DIR = os.getcwd()


class EdgeDriver(Driver):
    """
    Class that represents Edge Driver
    """
    def set_driver_path(self):
        """
        Set a correct PATH to the Selenium Web driver
        :return: None
        """
        logger.info("Preparing driver path.")
        self.path = CURRENT_DIR + "\\drivers\\MicrosoftWebDriver"
        logger.info("Driver path set to - {}".format(self.path))

    def set_capabilities(self):
        """
        Setting capabilities for Edge.
        :return: Capabilities
        """
        self.capabilities = webdriver.DesiredCapabilities.EDGE.copy()

    def create_edge_driver(self):
        """
        Setting Edge driver to be able to open URL.
        :return: None
        """
        logger.info("Preparing driver.")
        driver = webdriver.Edge(executable_path=self.capabilities)
        driver.maximize_window()
        logger.info("Driver is set.")
        return driver


def edge(browser):
    """
    Opens Edge browsers and makes a screenshot of the desired website.
    :param browser: Browser
    :return: None
    """
    edge_driver = prepare_driver()
    driver = edge_driver.create_edge_driver()
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
    driver = EdgeDriver("", 0, None)
    driver.set_driver_path()
    driver.set_capabilities()
    return driver
