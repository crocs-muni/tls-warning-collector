from setup_logger import output, logger
from browsers import *
from progress_bar import set_progress_percentage, print_progress
from requirements import check_requirements
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
    check_requirements()
    all_browsers = len(read_config()['browserIDs'])
    iteration = 0
    for browserID in read_config()['browserIDs']:
        iteration += 1
        all_versions = cfg['browsers'][browserID]['other-versions']
        v_iteration = 0
        progress = set_progress_percentage(iteration, all_browsers)
        for version in all_versions:
            v_iteration += 1
            v_progress = set_progress_percentage(v_iteration, len(all_versions))
            logger.info('######## Processing %s v(%s)', browserID, version)
            if browserID != 'edge':
                install_browser(browserID, version)
            get_ssl_screenshot(browserID, version)
            print_progress(v_progress, versions=True)
            uninstall_browser(browserID)
        print_progress(progress)
    return


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
    all_cases = len(cfg['cases'])
    iteration = 0
    for case in cfg['cases']:
        iteration += 1
        progress = set_progress_percentage(iteration, all_cases)
        try:
            output(browser, str(version), case)
            open_webpage(cfg['browsers'][browser]['binary'], cfg['cases'][case]['url'], case, str(version),
                     cfg['browsers'][browser]['package'])
        except Exception as e:
            logger.error("Something went TERRIBLY wrong. - %s", e)
        print_progress(progress, cases=True)


if __name__ == '__main__':
    main()
