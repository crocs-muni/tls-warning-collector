import os
from misc.setup_logger import logger

CURRENT_DIR = os.getcwd()


class Browser:
    """
    Class that represents browsers

    Attributes
    ----------
    name: str
        Browser name
    version: str
        Browser version
    case: str
        TLS warning to be collected
    package: str
        Browser package name
    url: str
        URL to get the TLS warning page
    short_version: int
        Major browser version without the release number

    Methods
    -------
    set_short_browser_version()
        Parsing the whole version string to the first part only.
    """

    def __init__(self, name, version, case, package, url, short_version):
        """
        :param name: Browser name
        :param version: Browser version
        :param case: TLS warning to be collected
        :param package: Browser package name
        :param url: URL to get the TLS warning page
        :param short_version: Major browser version without the release number
        """
        self.name = name
        self.version = version
        self.case = case
        self.package = package
        self.url = url
        self.short_version = short_version

    def set_short_browser_version(self):
        """
        Parsing the whole version string to the first part only.
        :return: None
        """
        full_version = self.version.split(".")
        self.short_version = int(full_version[0])


class Driver:
    """
    Class that represents driver for a particular browser

    Attributes
    ----------
    path: str
        Path to the driver in drivers folder
    version: str
        Version of the driver
    capabilities: dict
        Capabilities that need to be set in order to collect TLS warnings screenshots
    """

    def __init__(self, path, version, capabilities):
        """
        :param path: Path to the driver in drivers folder
        :param version: Version of the driver
        :param capabilities: Capabilities that need to be set in order to collect TLS warnings screenshots
        """
        self.path = path
        self.version = version
        self.capabilities = capabilities


def open_browser(driver, url):
    """
    Opens given url in the browsers.
    :param driver: Browser driver
    :param url: Case URL
    :return: None
    """
    logger.info("Opening {}".format(url))
    driver.get(url)
