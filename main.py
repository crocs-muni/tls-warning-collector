import sys
from setup_logger import logger
from browsers import *


def get_browser():
    """Gets browser binary."""
    args = sys.argv[1:]
    browser = str(args[0])
    logger.info('Getting browser binary. - %s', browser)
    return browser


def get_package():
    """Gets browser package. In case of Chromium it is important because binary is chrome."""
    args = sys.argv[1:]
    package = str(args[4])
    logger.info('Getting browser package. - %s', package)
    return package


def get_version():
    """Gets browser version."""
    args = sys.argv[1:]
    version = str(args[1])
    logger.info('Getting browser version. - %s', version)
    return version


def get_case():
    """Gets case of SSL."""
    args = sys.argv[1:]
    case = str(args[2])
    logger.info('Getting case of badssl. - %s', case)
    return case


def get_case_url():
    """Gets URL for the required SSL warning page."""
    args = sys.argv[1:]
    url = str(args[3])
    logger.info('Getting URL for badssl page. - %s', url)
    return url


def main():
    """Function which makes it all work as a one function."""
    open_webpage(get_browser(), get_case_url(), get_version(), get_package())


if __name__ == '__main__':
    main()
