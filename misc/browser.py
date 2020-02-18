from misc.setup_logger import logger
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
