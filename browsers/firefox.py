import os

from selenium.common.exceptions import WebDriverException
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from misc.browser import Driver, open_browser
from browsers.screenshot import screenshot_website, kill_browser
from misc.setup_logger import logger


CURRENT_DIR = os.getcwd()


class FFDriver(Driver):
    """
    Class that represents Firefox Driver
    """

    def set_driver_path(self):
        """
        Set a correct PATH to the Selenium Web driver
        :return: None
        """
        logger.info("Preparing driver path.")
        self.path = CURRENT_DIR + "\\drivers\\firefoxdrivers\\geckodriver-" + self.version + "\\geckodriver.exe"
        logger.info("Driver path set to - {}".format(self.path))

    def set_firefox_driver_version(self, browser_version):
        """
        Setting Firefox driver version.
        :param browser_version: Browser version
        :return: Driver version
        """
        logger.info("Getting geckodriver version.")
        if browser_version >= 62:
            self.version = "24"
        elif 52 <= browser_version < 62:
            self.version = "17"
        elif 47 <= browser_version < 52:
            self.version = "14"
        elif browser_version < 47:
            self.version = "11"
        logger.info("Geckodriver version - {}".format(self.version))

    def set_capabilities(self, browser_version):
        """
        Setting Firefox capabilities.
        :param browser_version: Browser version
        :return: None
        """
        # Marionette is protocol used to communicate with Gecko Driver in versions 48 and higher.
        capabilities = DesiredCapabilities.FIREFOX
        capabilities["marionette"] = True
        capabilities["acceptInsecureCerts"] = False
        capabilities["acceptSslCerts"] = False
        # For Firefox 47 and lower the marionette needs to be set to False because it is not included.
        if browser_version < 47:
            capabilities["marionette"] = False
        logger.info("Capabilities are set to - {}".format(capabilities))
        self.capabilities = capabilities

    def create_firefox_driver(self):
        """
        Setting Firefox driver to be able to open URL.
        :return: Selenium WebDriver
        """
        logger.info("Preparing driver.")
        driver = webdriver.Firefox(executable_path=self.path, capabilities=self.capabilities)
        driver.maximize_window()
        logger.info("Driver is set.")
        return driver


def firefox(browser):
    """
    Opens Firefox and makes a screenshot of the desired website.
    :param browser: Browser
    :return: None
    """
    browser.set_short_browser_version()
    ff_driver = prepare_driver(browser)
    driver = ff_driver.create_firefox_driver()
    try:
        open_browser(driver, browser.url)
        screenshot_website(driver, browser)
    except WebDriverException as e:
        logger.error("Exception from Selenium but going to take a screenshot. -- {}".format(e))
        screenshot_website(driver, browser)
    finally:
        driver.quit()
    kill_browser()


def prepare_driver(browser):
    """
    Preparing Geckodriver to run Firefox via Selenium
    :param browser: Browser object
    :return: Driver object ready to be used
    """
    ff_driver = FFDriver("", 0, None)
    ff_driver.set_firefox_driver_version(browser.short_version)
    ff_driver.set_driver_path()
    ff_driver.set_capabilities(browser.short_version)
    return ff_driver
