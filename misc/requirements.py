import subprocess
import os

CURRENT_DIR = os.getcwd()
DRIVERS_PATH_BASE = CURRENT_DIR + "\\drivers"
CHROME_DRIVERS = DRIVERS_PATH_BASE + "\\chromedrivers"
FIREFOX_DRIVERS = DRIVERS_PATH_BASE + "\\firefoxdrivers"
OPERA_DRIVERS = DRIVERS_PATH_BASE + "\\operadrivers"


def check_requirements():
    """
    Checks if all requirements are met.
    :return: True if all requirements are met, False otherwise
    """
    return check_if_admin() and check_drivers()


def check_if_admin():
    """
    Checks if user has Administrator Command Prompt running
    :return: None
    """
    cmd = "net session >nul 2>&1"
    is_admin = subprocess.call(cmd, shell=True)
    if is_admin != 0:
        print("You are not and Administrator. Change to Administrator Command Line in order to run this.")
        return False
    return True


def check_drivers():
    """
    Checks if drivers are in correct folder structure
    :return: True if drivers directory exists or is not empty, False otherwise
    """
    if dir_exists(DRIVERS_PATH_BASE) and dir_not_empty(DRIVERS_PATH_BASE):
        return check_driver_dirs()
    print("Drivers directory is empty or does not exist!")
    return False


def check_driver_dirs():
    """
    Checks all required dirs
    :return: True if all driver directories exists and are not empty, False otherwise
    """
    return dir_exists(CHROME_DRIVERS) and dir_not_empty(CHROME_DRIVERS) and \
        dir_exists(FIREFOX_DRIVERS) and dir_not_empty(FIREFOX_DRIVERS) and \
        dir_exists(OPERA_DRIVERS) and dir_not_empty(OPERA_DRIVERS)


def dir_exists(directory):
    """
    Checks if given directory exist
    :param directory: Path to directory
    :return: True if directory exists, False otherwise
    """
    if os.path.exists(directory):
        return True
    print("{} folder is missing!".format(directory))
    return False


def dir_not_empty(directory):
    """
    Checks if given directory is not empty
    :param directory: Path to directory
    :return: True if directory is not empty, False otherwise
    """
    if os.listdir(directory):
        return True
    print("{} folder is empty!".format(directory))
    return False


def install_dependencies():
    """
    Installs missing dependencies included in the requirements.txt file
    :return: None
    """
    pip_cmd = "pip3 install --quiet -r requirements.txt"
    process = subprocess.Popen(pip_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for _ in process.stdout.readlines():
        process.wait()

