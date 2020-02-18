from browsers.screenshot import screenshot_website
from selenium import webdriver

from setup_logger import logger


def edge(browser, version, case, package, url):
    """Opens Edge browsers and makes a screenshot of the desired website."""
    capabilities = webdriver.DesiredCapabilities.EDGE.copy()
    logger.info('Preparing driver.')
    driver = webdriver.Edge(executable_path=r'C:\\Users\\IEUser\\Downloads\\MicrosoftWebDriver')
    driver.maximize_window()
    logger.info('Driver is set.')
    logger.info('Opening %s', url)
    driver.get(url)
    try:
        screenshot_website(driver, browser, version, package, case, ie=True)
    finally:
        logger.info('Closing the browsers.')
        driver.quit()