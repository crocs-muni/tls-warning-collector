from PIL import ImageGrab
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from main import *
from setup_logger import logger
import os
import time
import psutil


CURRENT_DIRECTORY = os.getcwd()
SCREENSHOT_PATH_BASE = CURRENT_DIRECTORY + "\\screenshots"


def save_screenshot(path):
    """Saves the screenshot into correct path."""
    logger.info('Saving screenshot to - %s.', path)
    snapshot = ImageGrab.grab()
    snapshot.save(path)


def get_screenshot_path(path, browser, version, case):
    """Gets the path for browser directory where the screenshot will be saved."""
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


def screenshot_website(driver, browser, version, package, case, chromium=False, ie=False, opera_new=False, opera_old=False):
    """Makes a screenshot of the opened website."""
    isChromium = chromium
    isIe = ie
    logger.info('Checking if directory exists. If not, creating new.')
    new_directory(SCREENSHOT_PATH_BASE)
    logger.info('Preparing to screenshot website.')
    logger.info('chromium=%s, ie=%s, opera_new=%s, opera_old=%s', chromium, ie, opera_new, opera_old)
    final_id = setID(isIe)
    # If alert window appears, Accept and continue to the website.
    logger.info('Waiting until the website is loaded.')
    try:
        if opera_old:
            shot(driver, final_id, browser, version, package, case, isChromium)
        else:
            shot(driver, final_id, browser, version, package, case, isChromium)
        # In new versions of Opera the browser does not close after sending driver.close().
    finally:
        if opera_new or opera_old:
            kill_opera()


def setID(ie):
    """Set the ID of element present on the cert page"""
    # ID for internet explorer page
    id_ie = "invalidcert_mainTitle"
    # ID for other browsers page
    id_other = "content"
    logger.info('Checking if IE is TRUE.')
    if ie:
        logger.info('Setting the ID to - %s.', id_ie)
        final_id = id_ie
    else:
        logger.info('Setting the ID to - %s.', id_other)
        final_id = id_other
    return final_id


def kill_opera():
    """Process kill function for Opera browser"""
    logger.info('Going to kill Opera browser process.')
    for proc in psutil.process_iter():
        # check whether the process name matches
        if any(procstr in proc.name() for procstr in ['Opera', 'opera.exe']):
            logger.info(f'Killing {proc.name()}')
            proc.kill()
    logger.info('Opera killed.')


def shot(driver, final_id, browser, version, package, case, chromium=False):
    """Call functions to make the screenshot"""
    try:
        # Wait until the page is loaded
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, final_id)))
    except:
        logger.info('The page had some certificate issue. Making screenshot.')
    finally:
        time.sleep(2)
        if chromium:
            maximize_chromium(driver)
            # This is almost twice because 'Chromium' and 'Chrome' have the same binary but different package
            save_screenshot(get_screenshot_path(SCREENSHOT_PATH_BASE, package, version, case))
            save_screenshot(get_screenshot_case_path(SCREENSHOT_PATH_BASE, package, version, case))
        else:
            save_screenshot(get_screenshot_path(SCREENSHOT_PATH_BASE, browser, version, case))
            save_screenshot(get_screenshot_case_path(SCREENSHOT_PATH_BASE, browser, version, case))
            time.sleep(3)    


def maximize_chromium(driver):
    """This is the only working way to set Chromium to fullscreen"""
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    time.sleep(2)
