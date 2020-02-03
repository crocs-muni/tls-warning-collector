from PIL import ImageGrab
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from setup_logger import logger

import os
import time
import psutil


CURRENT_DIRECTORY = os.getcwd()
SCREENSHOT_PATH_BASE = CURRENT_DIRECTORY + "\\screenshots"


def screenshot_website(driver, browser, version, package, case, opera=False, ie=False):
    """Makes a screenshot of the opened website."""
    logger.info('Going to make screenshot.')
    new_directory(SCREENSHOT_PATH_BASE)
    # If alert window appears, Accept and continue to the website.
    logger.info('Waiting until the website is loaded.')
    try:
        load_website(driver, browser, version, package, case, opera=opera, ie=ie)
    except Exception as e:
        logger.error("Error occured in function 'shot()' - %s", e)
    finally:
        kill_browser()


def new_directory(item):
    """Creates new directory if does not exist."""
    if os.path.exists(item):
        logger.info("# Directory exists, not creating: %s", item)
    else:
        logger.info("# Creating directory: %s", item)
        try:
            os.makedirs(item)
        except:
            logger.error("Error occured while creating: %s", item)
    return


def load_website(driver, browser, version, package, case, opera=False, ie=False):
    """Loads the website and saves the screenshots to the path."""
    # If old opera then screenshot directly because there is an alert.
    if opera:
        save_all_screenshots(browser, version, case, package)
    else:
        # Otherwise check if the web is loaded and screenshot it afterwards.
        try:
            logger.info('Waiting for the page to load.')
            # Wait until the page is loaded
            id = set_id(ie, chromium)
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, id)))
        except Exception as e:
            logger.info('Exception occued: %s. Making screenshot.', e)
        finally:
            save_all_screenshots(browser, version, case, package)


def save_all_screenshots(browser, version, case, package):
    """Save screenshots to case path and default path as well."""
    time.sleep(5)
    make_and_save_screenshot(get_screenshot_path(SCREENSHOT_PATH_BASE, package, version, case))
    make_and_save_screenshot(get_screenshot_case_path(SCREENSHOT_PATH_BASE, package, version, case))
    time.sleep(2)


def make_and_save_screenshot(path):
    """Makes and saves the screenshot into correct path."""
    logger.info('Saving screenshot to - %s.', path)
    snapshot = ImageGrab.grab()
    snapshot.save(path)


def get_screenshot_path(path, browser, version, case):
    """Gets the path for browsers directory where the screenshot will be saved."""
    logger.info('Preparing path where screenshot will be saved.')
    directory = path + '\\browsers' + '\\' + browser + '\\' + version
    if not os.path.exists(directory):
        os.makedirs(directory)
    screenshot_name = case + '.png'
    screenshot_path = directory + '\\' + screenshot_name
    logger.info('Screenshot BROWSER path set - %s.', screenshot_path)
    return screenshot_path


def get_screenshot_case_path(path, browser, version, case):
    """Gets the path for case directory where the screenshot will be saved."""
    logger.info('Preparing path where screenshot will be saved.')
    directory = path + '\\cases' + '\\' + case + '\\' + browser
    if not os.path.exists(directory):
        os.makedirs(directory)
    screenshot_name = version + '.png'
    screenshot_path = directory + '\\' + screenshot_name
    logger.info('Screenshot CASE path set - %s.', screenshot_path)
    return screenshot_path


def set_id(ie, chromium):
    """Set the ID of element present on the cert page"""
    # ID for internet explorer page
    id_ie = "invalidcert_mainTitle"
    # ID for other browsers page
    id_other = "content"
    id_debugging = 'debugging'
    if ie:
        logger.info('Setting the ID to - %s.', id_ie)
        final_id = id_ie
    elif chromium:
        logger.info('Setting the ID to - %s.', id_debugging)
        final_id = id_debugging
    else:
        logger.info('Setting the ID to - %s.', id_other)
        final_id = id_other
    return final_id


def kill_browser():
    """Process kill function for browsers so that removing files after uninstall works."""
    logger.info('Going to kill browsers process.')
    for proc in psutil.process_iter():
        # check whether the process name matches
        if any(procstr in proc.name() for procstr in ['Opera', 'opera.exe', 'Chromium', 'chromium.exe', 'Firefox', 'firefox.exe']):
            logger.info(f'Killing {proc.name()}')
            proc.kill()
    logger.info('Browser killed.')


def remove_item(item):
    """Removes the given directory."""
    if os.path.exists(item):
        logger.info("# Removing item: %s", item)
        try:
            os.rmdir(item)
        except:
            logger.error("Error occured while deleting item: %s", item)
    else:
        logger.info("# Item does not exist, not removing: %s", item)
    return