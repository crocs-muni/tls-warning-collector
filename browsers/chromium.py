from selenium.webdriver import DesiredCapabilities
from misc.browser import parse_browser_version, open_browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from browsers.screenshot import screenshot_website, kill_browser
from misc.setup_logger import logger
import os

CURRENT_DIR = os.getcwd()


def chromium(browser, version, case, package, url):
    """
    Opens Chromium and makes a screenshot of the desired website.
    :param browser: Browser
    :param version: Browser version
    :param case: Case to be collected
    :param package: Browser package name
    :param url: Case url
    :return: None
    """
    v_number = parse_browser_version(version)
    driver_path = set_chromium_driver_path(v_number)
    old_driver = v_number < 74
    capabilities = set_chromium_capabilities()
    driver = set_chromium_driver(driver_path, capabilities)
    try:
        open_chromium(driver, url, browser, version, package, case, old_driver=old_driver)
    except Exception as e:
        logger.error("Exception in chromium() - {}".format(e))
    finally:
        driver.quit()
    kill_browser()


def set_chromium_driver_path(v_number):
    """
    Setting driver path for Chromium.
    :param v_number: Browser version
    :return: Path to driver
    """
    logger.info("Preparing driver path.")
    driver_version = set_chrome_driver_version(v_number)
    driver_path = CURRENT_DIR + "\\drivers\\chromedrivers\\chromedriver-" + driver_version + "\\chromedriver.exe"
    logger.info("Driver path set.")
    return driver_path


def set_chrome_driver_version(v_number):
    """
    Returns the folder name for chromedrivers of the given version.
    :param v_number: Browser version
    :return: Driver version
    """
    logger.info("Getting chromedriver version.")
    driver_version = ""
    if v_number >= 78:
        driver_version = "78"
    if v_number == 77:
        driver_version = "77"
    if v_number == 76:
        driver_version = "76"
    if v_number == 75:
        driver_version = "75"
    if v_number == 74:
        driver_version = "74"
    if 72 <= v_number < 74:
        driver_version = "2.46"
    if 70 <= v_number < 72:
        driver_version = "2.45"
    if 68 <= v_number < 70:
        driver_version = "2.42"
    if 66 <= v_number < 68:
        driver_version = "2.40"
    if 64 <= v_number < 66:
        driver_version = "2.37"
    if 62 <= v_number < 64:
        driver_version = "2.35"
    if 60 <= v_number < 62:
        driver_version = "2.33"
    if 58 <= v_number < 60:
        driver_version = "2.30"
    if 56 <= v_number < 58:
        driver_version = "2.29"
    if 54 <= v_number < 56:
        driver_version = "2.27"
    if 46 <= v_number < 54:
        driver_version = "2.20"
    if 43 <= v_number < 46:
        driver_version = "2.18"
    if 40 <= v_number < 43:
        driver_version = "2.15"
    if 36 <= v_number < 40:
        driver_version = "2.12"
    if 34 <= v_number < 36:
        driver_version = "2.10"
    if 32 <= v_number < 34:
        driver_version = "2.9"
    if 30 <= v_number < 32:
        driver_version = "2.8"
    if v_number < 30:
        driver_version = "2.6"
    logger.info("Chromedriver version - {}".format(driver_version))
    return driver_version


def set_chromium_capabilities():
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
    return capabilities


def set_chromium_driver(driver_path, capabilities):
    """
    Setting Chromium driver with special windows size. Otherwise it won"t open maximized in older versions.
    :param driver_path: Path to driver
    :param capabilities: Capabilities
    :return: WebDriver
    """
    driver = webdriver.Chrome(desired_capabilities=capabilities, executable_path=driver_path)
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    logger.info("Driver is set.")
    return driver


def open_chromium(driver, url, browser, version, package, case, old_driver=False):
    """
    Runs the screenshot funciton in a different thread.
    :param driver: Browser driver
    :param url: Case url
    :param browser: Browser
    :param version: Browser version
    :param package: Browser package name
    :param case: Case to collect
    :param old_driver: True if the driver version is older than 74
    :return: None
    """
    try:
        if old_driver:
            try:
                if case == "expired" or case == "wrong-host" or case == "self-signed" or case == "untrusted-root" or case == "revoked":
                    driver.set_page_load_timeout(5)
                    driver.set_script_timeout(5)
                open_browser(driver, url)
                screenshot_website(driver, browser, version, package, case)
            except Exception as e:
                logger.error("Exception occured {} - making screenshot.".format(e))
                screenshot_website(driver, browser, version, package, case)
        else:
            open_browser(driver, url)
            screenshot_website(driver, browser, version, package, case)
    except Exception as e:
        logger.error("Error in open_chromium: {}".format(e))
