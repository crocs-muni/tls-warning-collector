import subprocess
import time
import os

CURRENT_DIR = os.getcwd()
DRIVERS_PATH_BASE = CURRENT_DIR + "\\drivers"
CHROME_DRIVERS = DRIVERS_PATH_BASE + "\\chromedrivers"
FIREFOX_DRIVERS = DRIVERS_PATH_BASE + "\\firefoxdrivers"
OPERA_DRIVERS = DRIVERS_PATH_BASE + "\\operadrivers"


def check_requirements():
    """Checks if all requirements are met."""
    check_if_admin()
    check_drivers()
    pip_cmd = "pip3 install --quiet -r requirements.txt"
    subprocess.call(pip_cmd, shell=True)
    time.sleep(1)
    return


def check_if_admin():
    """Checks if user has Administrator Command Prompt running"""
    cmd = "net session >nul 2>&1"
    is_admin = subprocess.call(cmd, shell=True)
    if is_admin == 0:
        pass
    else:
        print("You are not and Administrator. Change to Administrator Command Line in order to run this.")
        return
    return


def check_drivers():
    """Checks if drivers are in correct folder structure"""
    if dir_exists(DRIVERS_PATH_BASE) and dir_not_empty(DRIVERS_PATH_BASE):
        return check_driver_dirs()
    else:
        print("Drivers directory is empty or does not exist!")
        return


def dir_exists(directory):
    """Checks if given directory exist"""
    if not os.path.exists(directory):
        print("{} folder is missing!".format(directory))
        return
    return


def dir_not_empty(directory):
    """Checks if given directory is not empty"""
    if not os.listdir(directory):
        print("{} folder is empty!".format(directory))
        return
    return


def check_driver_dirs():
    """Checks all required dirs"""
    return dir_exists(CHROME_DRIVERS) and dir_not_empty(CHROME_DRIVERS) and dir_exists(FIREFOX_DRIVERS) and \
           dir_not_empty(FIREFOX_DRIVERS) and dir_exists(OPERA_DRIVERS) and dir_not_empty(OPERA_DRIVERS)
