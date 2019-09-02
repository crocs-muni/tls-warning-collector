from PIL import ImageGrab
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from main import *
from setup_logger import logger

CURRENT_DIRECTORY = os.getcwd()
SCREENSHOT_PATH_BASE = CURRENT_DIRECTORY + "\\screenshots"


def save_screenshot(path):
    """Saves the screenshot into correct path."""
    logger.info('Saving screenshot to - %s.', path)
    snapshot = ImageGrab.grab()
    snapshot.save(path)


def get_screenshot_path(path, browser, version, case):
    """Gets path for browser directory where screenshot will be saved."""
    logger.info('Preparing path where screenshot will be saved.')
    directory = path + '\\browsers' + '\\' + browser + '\\' + version
    if not os.path.exists(directory):
        os.makedirs(directory)
    screenshot_name = case + '.png'
    screenshot_path = directory + '\\' + screenshot_name
    logger.info('Screenshot BROWSER path set - %s.', screenshot_path)
    return screenshot_path


def get_screenshot_case_path(path, browser, version, case):
    """Gets path for case directory where screenshot will be saved."""
    logger.info('Preparing path where screenshot will be saved.')
    directory = path + '\\cases' + '\\' + case + '\\' + browser
    if not os.path.exists(directory):
        os.makedirs(directory)
    screenshot_name = version + '.png'
    screenshot_path = directory + '\\' + screenshot_name
    logger.info('Screenshot CASE path set - %s.', screenshot_path)
    return screenshot_path


def screenshot_website(driver, browser, version, package, case, chromium=False, ie=False, opera_new=False, opera_old=False):
    """Makes screenshot of the opened website."""
    logger.info('Checking if directory exists. If not, creating new.')
    new_directory(SCREENSHOT_PATH_BASE)
    logger.info('Preparing to screenshot website.')
    logger.info('chromium=%s, ie=%s, opera_new=%s, opera_old=%s', chromium, ie, opera_new, opera_old)
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
    # If alert window appears, Accept and continue to the website.
    if opera_old:
        try:
            logger.info('Old opera version. Need to accept the alert.')
            logger.info('Wait for 2 seconds.')
            time.sleep(2)
            logger.info('Sending LEFT key.')
            webdriver.ActionChains(driver).send_keys(Keys.LEFT).perform()
            logger.info('Sending RETURN key.')
            webdriver.ActionChains(driver).send_keys(Keys.RETURN).perform()
            logger.info('Keys sent.')
        except Exception as ex:
            logger.error('Something went wrong. - %s', ex)
            pass
    logger.info('Waiting until the website is loaded.')
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, final_id)))
    except:
        logger.info('The page had some other certificate issue. Making screenshot.')
    finally:
        time.sleep(2)
        if chromium:
            logger.info('Sending ALT + SPACE + X to maximize screen.')
            webdriver.ActionChains(driver).send_keys(Keys.ALT, Keys.SPACE, "x").perform()
            logger.info('Keys sent.')
            save_screenshot(get_screenshot_path(SCREENSHOT_PATH_BASE, package, version, case))
            save_screenshot(get_screenshot_case_path(SCREENSHOT_PATH_BASE, package, version, case))
        else:
            save_screenshot(get_screenshot_path(SCREENSHOT_PATH_BASE, browser, version, case))
            save_screenshot(get_screenshot_case_path(SCREENSHOT_PATH_BASE, browser, version, case))
            time.sleep(3)
            # In new versions of Opera the browser does not close after sending driver.close().
            if opera_new:
                # Trying to send ALT + F4 to close the browser.
                logger.info('Sending ALT + F4 to close the browser.')
                webdriver.ActionChains(driver).key_down(Keys.ALT).send_keys(Keys.F4).key_up(Keys.ALT).perform()
                logger.info('Keys sent.')
