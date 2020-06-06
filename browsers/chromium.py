import os

from selenium.webdriver import DesiredCapabilities
from misc.browser import Driver, open_browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from browsers.screenshot import screenshot_website, kill_browser
from misc.setup_logger import logger

CURRENT_DIR = os.getcwd()


class ChromiumDriver(Driver):
    """
    Class that represents Chromium Driver
    """

    def set_driver_path(self):
        """
        Setting driver path for Chromium.
        :return: None
        """
        logger.info("Preparing driver path.")
        self.path = CURRENT_DIR + "\\drivers\\chromedrivers\\chromedriver-" + self.version + "\\chromedriver.exe"
        logger.info("Driver path set.")

    def set_driver_version(self, browser_version):
        """
        Returns the folder name for chromedrivers of the given version.
        :param browser_version: 
        :return: Driver version
        """
        logger.info("Getting chromedriver version.")
        if browser_version >= 78:
            self.version = "78"
        if browser_version == 77:
            self.version = "77"
        if browser_version == 76:
            self.version = "76"
        if browser_version == 75:
            self.version = "75"
        if browser_version == 74:
            self.version = "74"
        if 72 <= browser_version < 74:
            self.version = "2.46"
        if 70 <= browser_version < 72:
            self.version = "2.45"
        if 68 <= browser_version < 70:
            self.version = "2.42"
        if 66 <= browser_version < 68:
            self.version = "2.40"
        if 64 <= browser_version < 66:
            self.version = "2.37"
        if 62 <= browser_version < 64:
            self.version = "2.35"
        if 60 <= browser_version < 62:
            self.version = "2.33"
        if 58 <= browser_version < 60:
            self.version = "2.30"
        if 56 <= browser_version < 58:
            self.version = "2.29"
        if 54 <= browser_version < 56:
            self.version = "2.27"
        if 46 <= browser_version < 54:
            self.version = "2.20"
        if 43 <= browser_version < 46:
            self.version = "2.18"
        if 40 <= browser_version < 43:
            self.version = "2.15"
        if 36 <= browser_version < 40:
            self.version = "2.12"
        if 34 <= browser_version < 36:
            self.version = "2.10"
        if 32 <= browser_version < 34:
            self.version = "2.9"
        if 30 <= browser_version < 32:
            self.version = "2.8"
        if browser_version < 30:
            self.version = "2.6"
        logger.info("Chromedriver version - {}".format(self.version))

    def set_capabilities(self):
        """
        Setting capabilities for Chromium.
        :return: Capabilities
        """
        logger.info("Setting chromium capabilities.")
        opts = Options()
        opts.binary_location = "C:\\Program Files\\Chromium\\Application\\chrome.exe"
        opts.add_experimental_option("excludeSwitches", ["ignore-certificate-errors", "ignore-ssl-errors"])
        capabilities = DesiredCapabilities.CHROME
        capabilities.update(opts.to_capabilities())
        capabilities["acceptInsecureCerts"] = False
        capabilities["acceptSslCerts"] = False
        self.capabilities = capabilities

    def create_chromium_driver(self):
        """
        Setting Chromium driver with special windows size. Otherwise it won"t open maximized in older versions.
        :return: WebDriver
        """
        driver = webdriver.Chrome(desired_capabilities=self.capabilities, executable_path=self.path)
        driver.set_window_size(1024, 600)
        driver.maximize_window()
        logger.info("Driver is set.")
        return driver


def chromium(browser):
    """
    Opens Chromium and makes a screenshot of the desired website.
    :param browser: Browser
    :return: None
    """
    browser.set_short_browser_version()
    chromium_driver = prepare_driver(browser)
    driver = chromium_driver.create_chromium_driver()
    old_driver = browser.version < 74
    try:
        open_chromium(driver, browser, old_driver=old_driver)
    except Exception as e:
        logger.error("Exception in chromium() - {}".format(e))
    finally:
        driver.quit()
    kill_browser()


def open_chromium(driver, browser, old_driver=False):
    """
    Opens Firefox and makes a screenshot of the desired website. If the driver version is older,
    it sets a timeout for the script to finish.
    :param driver: Browser driver
    :param browser: Browser
    :param old_driver: True if the driver version is older than 74
    :return: None
    """
    try:
        if old_driver:
            open_browser_with_timeout(driver, browser)
        else:
            open_browser(driver, browser.url)
            screenshot_website(driver, browser)
    except Exception as e:
        logger.error("Error in open_chromium: {}".format(e))


def open_browser_with_timeout(driver, browser):
    """
    Opens Chromium, sets a timeout for the script to finish and takes a screenshot
    :param driver: Browser driver
    :param browser: Browser
    :return: None
    """
    try:
        if browser.case == "expired" or browser.case == "wrong-host" or browser.case == "self-signed" \
                or browser.case == "untrusted-root" or browser.case == "revoked":
            driver.set_page_load_timeout(5)
            driver.set_script_timeout(5)
        open_browser(driver, browser.url)
        screenshot_website(driver, browser)
    except Exception as e:
        logger.error("Exception occured {} - making screenshot.".format(e))
        screenshot_website(driver, browser)


def prepare_driver(browser):
    """
    Preparing Chromedriver to run Chromium via Selenium
    :param browser: Browser object
    :return: Driver object ready to be used
    """
    driver = ChromiumDriver("", 0, None)
    driver.set_driver_version(browser.short_version)
    driver.set_driver_path()
    driver.set_capabilities()
    return driver
