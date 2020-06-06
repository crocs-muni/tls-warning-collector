import multiprocessing
import time
import os

from selenium.webdriver import DesiredCapabilities
from misc.browser import Driver, open_browser
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
from browsers.screenshot import screenshot_website, kill_browser
from misc.setup_logger import logger


CURRENT_DIR = os.getcwd()


class OperaDriver(Driver):
    """
    Class that represents Opera Driver
    """
    def __init__(self, path, version, capabilities, old=False):
        super().__init__(path, version, capabilities)
        self.old = old

    def set_driver_path(self):
        """
        Setting Opera driver path.
        :return: None
        """
        logger.info("Preparing driver path.")
        self.path = CURRENT_DIR + "\\drivers\\operadrivers\\operadriver-" + self.version + "\\operadriver.exe"
        logger.info("Driver path set.")

    def set_driver_version(self, browser_version):
        """
        Returns the folder name for operadrivers of the given version.
        :param browser_version: Browser version
        :return: Driver version
        """
        logger.info("Getting operadriver version.")
        if browser_version >= 63:
            self.version = "76"
        if browser_version == 62:
            self.version = "2.41"
        if 58 < browser_version < 62:
            self.version = "2.45"
        if 56 < browser_version <= 58:
            self.version = "2.36"
        if browser_version == 56:
            self.version = "2.40"
        if browser_version == 55:
            self.version = "2.38"
        if browser_version == 54:
            self.version = "2.37"
        if browser_version == 53:
            self.version = "2.36"
        if 50 < browser_version <= 52:
            self.version = "2.35"
        if browser_version == 50:
            self.version = "2.33"
        if browser_version == 49:
            self.version = "2.33"
        if browser_version == 48:
            self.version = "2.30"
        if browser_version == 47:
            self.version = "2.30"
        if 42 < browser_version <= 46:
            self.version = "2.29"
        if 40 < browser_version <= 42:
            self.version = "2.27"
        if 26 < browser_version <= 40:
            self.version = "0.2.2"
        if browser_version == 26:
            self.version = "0.2.0"
        if browser_version <= 25:
            self.version = "0.1.0"
        logger.info("Operadriver version - {}".format(self.version))

    def set_capabilities(self, browser):
        """
        Setting capabilities for Opera.
        :return: Capabilities
        """
        logger.info("Setting capabilities.")
        opts = Options()
        if not self.old:
            # In older version these switches do not work, but alerts are there by default.
            opts.add_experimental_option("excludeSwitches", ["ignore-certificate-errors", "ignore-ssl-errors"])
        capabilities = DesiredCapabilities.OPERA
        capabilities.update(opts.to_capabilities())
        capabilities["acceptInsecureCerts"] = False
        capabilities["acceptSslCerts"] = False
        capabilities["operaOptions"] = {"binary": "C:\\Program Files\\Opera\\" + browser.version + "\\opera.exe"}
        logger.info("Capabilities are set.")
        self.capabilities = capabilities

    def set_opera_driver_oldness(self):
        """
        Checking if Opera driver version is lower than 2.40. If yes, sets the old value to True, False otherwise
        :return: None
        """
        logger.info("Checking if the Opera version is lower than 2.40")
        if float(self.version) < 2.40:
            logger.info("Opera version is using old driver. - True")
            self.old = True

    def create_opera_driver(self):
        """
        Setting Opera driver to be able to open URL.
        :return: WebDriver
        """
        logger.info("Preparing driver.")
        webdriver_service = service.Service(self.path)
        webdriver_service.start()
        driver = webdriver.Remote(webdriver_service.service_url, self.capabilities)
        driver.maximize_window()
        logger.info("Driver is set.")
        return driver


def opera(browser):
    """
    Opens Opera and makes a screenshot of the desired website.
    :param browser: Browser
    :return: None
    """
    browser.set_short_browser_version()
    opera_driver = prepare_driver(browser)
    driver = opera_driver.create_opera_driver()
    time.sleep(2)
    try:
        open_opera(driver, browser, old_driver=opera_driver.old)
    except Exception as e:
        logger.error("Exception in opera(): - {}".format(e))
    finally:
        driver.quit()
    kill_browser()


def open_opera(driver, browser, old_driver=False):
    """
    Run screenshot in different thread.
    :param driver: Driver
    :param browser: Browser
    :param old_driver: True if opera runs old driver, False otherwise
    :return: None
    """
    try:
        if old_driver:
            logger.info("Starting timeout_and_screenshot.")
            timeout_and_screenshot(driver, browser)
        else:
            open_browser(driver, browser.url)
            screenshot_website(driver, browser)
    except Exception as e:
        logger.error("Error in open_opera: {}".format(e))


def timeout_and_screenshot(driver, browser):
    """
    Opens the url in different thread so that it is not waiting until the page is loaded.
    :param driver: Driver
    :param browser: Browser
    :return: None
    """
    try:
        p1 = multiprocessing.Process(name="p1", target=open_browser, args=(driver, browser.url))
        logger.info("Starting process for open_browser.")
        p1.start()
        p1.join(3)
        logger.info("Going to take screenshot from timeout_and_screenshot.")
        if opera:
            screenshot_website(driver, browser, True, False)
    except Exception as e:
        logger.error("Exception in multiprocessing: {}".format(e))
    finally:
        logger.info("Checking if thread is active")
        terminate_thread(p1)


def terminate_thread(thread):
    """
    Terminate the thread.
    :param thread: Thread to be terminated
    :return: None
    """
    if thread.is_alive():
        logger.info("Terminating the thread")
        thread.terminate()
        thread.join()


def prepare_driver(browser):
    """
    Preparing Operadriver to run Opera via Selenium
    :param browser: Browser object
    :return: Driver object ready to be used
    """
    driver = OperaDriver("", 0, None)
    driver.set_opera_driver_oldness()
    driver.set_driver_version(browser.short_version)
    driver.set_driver_path()
    driver.set_capabilities(browser)
    return driver
