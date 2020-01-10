from browsers.firefox import firefox
from browsers.opera import opera
from browsers.chromium import chromium
from browsers.chrome import chrome
from browsers.iexplorer import iexplorer
from browsers.edge import edge

from setup_logger import logger
import os


CURRENT_DIR = os.getcwd()


def parse_browser_version(version):
    """Parsing the whole version string to the first part only."""
    logger.info('Parsing browsers full version to short.')
    full_version = version.split(".")
    v_number = int(full_version[0])
    logger.info('Browser short version - %s', v_number)
    return v_number


def open_browser(driver, url):
    """Opens given url in the browsers."""
    logger.info('Opening %s', url)
    driver.get(url)


def open_webpage(browser, url, case, version, package):
    """Opens the URL in desired browsers."""
    if browser == 'firefox':
        firefox(browser, version, case, package, url)
    if browser == 'opera':
        opera(browser, version, case, package, url)
    if package == 'chromium':
        chromium(browser, version, case, package, url)
    if browser == 'chrome' and package != 'chromium':
        chrome(browser, version, case, package, url)
    if browser == 'ie':
        iexplorer(browser, version, case, package, url)
    if browser == 'edge':
        edge(browser, version, case, package, url)
