from setup_logger import output, logger
from browsers import *
import time
import yaml
import os.path
import subprocess


def read_config():
    """Loads data from config.yaml to cfg."""
    try:
        with open('config.yaml', 'r') as yamlfile:
            conf = yaml.safe_load(yamlfile)
    except:
        logger.info("Some error occured while reading config.yaml")
    return conf


# Global variable cfg for configuration file
cfg = read_config()


def main():
    """Iterates over all of the browsers and versions and runs the script for getting screenshots."""
    for browserID in read_config()['browserIDs']:
        for version in cfg['browsers'][browserID]['versions']:
            logger.info('######## Processing %s v(%s)', browserID, version)
            if browserID != 'edge':
                install_browser(browserID, version)
            get_ssl_screenshot(browserID, version)
            uninstall_browser(browserID)


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


def install_browser(browser, version):
    """Installs the given browser version."""
    cmd = "choco install " + str(cfg['browsers'][browser]['package']) + " --force --version=" + str(version) + \
          " --yes --nocolor --limit-output --no-progress --ignore-checksums --log-file=choco-log.log"
    logger.info("# Installing the browser.")
    subprocess.Popen(cmd)
    time.sleep(60)
    logger.info("# Installation done.")


def uninstall_browser(browser):
    """Uninstalls the given browser."""
    cmd = "choco uninstall " + str(cfg['browsers'][browser]['package']) + \
          " --allversions --yes --nocolor --limit-output --log-file=choco-log.log"
    logger.info("# Uninstalling the browser.")
    subprocess.Popen(cmd)
    time.sleep(60)
    logger.info("# Uninstalling done.")
    logger.info("# Removing installation folders.")
    for folder in cfg['browsers'][browser]['installFolders']:
        remove_item(folder)
    logger.info("All folders are removed.")


def get_ssl_screenshot(browser, version):
    """Gets the screenshot of SSL warning in the given browser version."""
    # Loop through all cases
    logger.info("# Preparing iteration.")
    for case in cfg['cases']:
        try:
            output(browser, str(version), case)
            open_webpage(cfg['browsers'][browser]['binary'], cfg['cases'][case]['url'], case, str(version),
                     cfg['browsers'][browser]['package'])
        except Exception as e:
            logger.error("Something went TERRIBLY wrong. - %s", e)


if __name__ == '__main__':
    main()
