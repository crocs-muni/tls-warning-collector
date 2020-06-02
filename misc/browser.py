import os
from misc.setup_logger import logger

CURRENT_DIR = os.getcwd()


class Browser:
    """
    Class that represents browsers
    """
    def __init__(self, name, version, case, package, url, short_version):
        self.name = name
        self.version = version
        self.case = case
        self.package = package
        self.url = url
        self.short_version = short_version

    def set_short_browser_version(self):
        """
        Parsing the whole version string to the first part only.
        :param version: Browser version
        :return: Major number of the browser version
        """
        full_version = self.version.split(".")
        self.short_version = int(full_version[0])


class Driver:
    """
    Class that represents driver for a particular browser
    """
    def __init__(self, path, version, capabilities):
        self.path = path
        self.version = version
        self.capabilities = capabilities

    def set_driver_path(self):
        logger.info("Preparing driver path.")
        self.path = CURRENT_DIR + "\\drivers\\firefoxdrivers\\geckodriver-" + self.version + "\\geckodriver.exe"
        logger.info("Driver path set to - {}".format(self.path))


def open_browser(driver, url):
    """
    Opens given url in the browsers.
    :param driver: Browser driver
    :param url: Case URL
    :return: None
    """
    logger.info("Opening {}".format(url))
    driver.get(url)
