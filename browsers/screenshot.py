import os
import time
import psutil

from PIL import ImageGrab
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from misc.setup_logger import logger
from misc.database import update_db

CURRENT_DIRECTORY = os.getcwd()
SCREENSHOT_PATH_BASE = CURRENT_DIRECTORY + "\\screenshots"


def screenshot_website(driver, browser, opera=False, ie=False):
    """
    Makes a screenshot of the opened website.
    :param driver: Browser WebDriver
    :param browser: Browser
    :param opera: True if older opera version, False otherwise
    :param ie: True if IE is the actual browser, False otherwise
    :return: None
    """
    logger.info("Going to make screenshot.")
    new_directory(SCREENSHOT_PATH_BASE)
    # If alert window appears, Accept and continue to the website.
    logger.info("Waiting until the website is loaded.")
    try:
        load_website(driver, browser, opera=opera, ie=ie)
        update_db(browser.name, browser.version)
    except Exception as e:
        logger.error("Error occured in function 'shot()' - {}".format(e))
    finally:
        kill_browser()


def new_directory(item):
    """
    Creates new directory if does not exist.
    :param item: Directory to be created
    :return: None
    """
    if os.path.exists(item):
        logger.info("# Directory exists, not creating: {}".format(item))
    else:
        logger.info("# Creating directory: {}".format(item))
        try:
            os.makedirs(item)
        except:
            logger.error("Error occured while creating: {}".format(item))


def load_website(driver, browser, opera=False, ie=False):
    """
    Loads the website and saves the screenshots to the path.
    :param driver: Browser WebDriver
    :param browser: Browser
    :param opera: True if older opera version, False otherwise
    :param ie: True if IE is the actual browser, False otherwise
    :return: None
    """
    # If old opera then screenshot directly because there is an alert.
    if opera:
        save_all_screenshots(browser)
    else:
        # Otherwise check if the web is loaded and screenshot it afterwards.
        try:
            logger.info("Waiting for the page to load.")
            id = set_id(ie)
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, id)))
        except Exception as e:
            logger.info("Exception occured: {}. Making screenshot.".format(e))
        finally:
            save_all_screenshots(browser)


def save_all_screenshots(browser):
    """
    Save screenshots to case path and default path as well.
    :param browser: Browser
    :return: None
    """
    time.sleep(5)
    make_and_save_screenshot(get_screenshot_path(SCREENSHOT_PATH_BASE, browser))
    make_and_save_screenshot(get_screenshot_case_path(SCREENSHOT_PATH_BASE, browser))
    time.sleep(2)


def make_and_save_screenshot(path):
    """
    Makes and saves the screenshot into correct path.
    :param path: PATH where screenshots will be saved
    :return: None
    """
    logger.info("Saving screenshot to - {}".format(path))
    snapshot = ImageGrab.grab()
    snapshot.save(path)


def get_screenshot_path(path, browser):
    """
    Gets the path for browsers directory where the screenshot will be saved.
    :param path: Screenshots directory path
    :param browser: Browser
    :return: Finalized PATH where browsers screenshots will be saved
    """
    logger.info("Preparing path where screenshot will be saved.")
    directory = path + "\\browsers" + "\\" + browser.name + "\\" + browser.version
    if not os.path.exists(directory):
        os.makedirs(directory)
    screenshot_name = browser.case + ".png"
    screenshot_path = directory + "\\" + screenshot_name
    logger.info("Screenshot BROWSER path set - {}".format(screenshot_path))
    return screenshot_path


def get_screenshot_case_path(path, browser):
    """
    Gets the path for case directory where the screenshot will be saved.
    :param path: Screenshots directory path
    :param browser: Browser
    :return: Finalized PATH where case screenshots will be saved
    """
    logger.info("Preparing path where screenshot will be saved.")
    directory = path + "\\cases" + "\\" + browser.case + "\\" + browser.name
    if not os.path.exists(directory):
        os.makedirs(directory)
    screenshot_name = browser.version + ".png"
    screenshot_path = directory + "\\" + screenshot_name
    logger.info("Screenshot CASE path set - {}".format(screenshot_path))
    return screenshot_path


def set_id(ie):
    """
    Set the ID of element present on the cert page
    :param ie: True if IE is the actual browser, False otherwise
    :return: ID of element that Selenium will look for on current case web site
    """
    # ID for internet explorer page
    id_ie = "invalidcert_mainTitle"
    # ID for other browsers page
    id_other = "content"
    if ie:
        logger.info("Setting the ID to -  {}".format(id_ie))
        final_id = id_ie
    else:
        logger.info("Setting the ID to -  {}".format(id_other))
        final_id = id_other
    return final_id


def kill_browser():
    """
    Process kill function for browsers so that removing files after uninstall works.
    :return: None
    """
    logger.info("Going to kill browsers process.")
    for proc in psutil.process_iter():
        # check whether the process name matches
        if any(procstr in proc.name() for procstr in
               ["Opera", "opera.exe", "Chromium", "chromium.exe", "Firefox", "firefox.exe"]):
            logger.info("Killing {}".format(proc.name()))
            proc.kill()
    logger.info("Browser killed.")


def remove_item(item):
    """
    Removes the given directory.
    :param item: Directory to be removed
    :return: None
    """
    if os.path.exists(item):
        logger.info("# Removing item: {}".format(item))
        try:
            os.rmdir(item)
        except Exception:
            logger.error("Error occured while deleting item: {}".format(item))
    else:
        logger.info("# Item does not exist, not removing: {}".format(item))
