from setup_logger import output
from browsers import open_webpage
import yaml
import os.path
import subprocess
from setup_logger import logger

try:
    with open('config.yaml', 'r') as yamlfile:
        cfg = yaml.safe_load(yamlfile)
except:
    logger.info("Some error occured while reading config.yaml")


def main():
    """Iterates over all of the browsers and versions and runs the script for screenshots"""
    for browser in cfg['browsers']:
        for version in cfg['browsers'][browser]['versions']:
            logger.info('######## Processing %s v(%s)', browser, version)
            if browser != 'edge':
                install_browser(browser, version)
            get_ssl_screenshot(browser, version)
            uninstall_browser(browser)


def remove_item(item):
    """Removes the given directory"""
    if os.path.exists(item):
        logger.info("# Removing item: %s", item)
        try:
            os.rmdir(item)
        except:
            logger.error("Error occured while deleting item: %s", item)
    else:
        logger.info("# Item does not exist, not removing: %s", item)


def new_directory(item):
    """Creates new directory if not exists."""
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
    """Installs given browser version."""
    cmd = "choco install " + cfg['browsers'][browser]['package'] + " --force --version=" + version + \
          "--yes --nocolor --limit-output --no-progress --ignore-checksums --log-file=choco-log.log"
    logger.info("# Installing the browser.")
    subprocess.Popen(cmd)
    logger.info("# Installation done.")


def uninstall_browser(browser):
    """Uninstalls given browser."""
    cmd = "choco uninstall " + cfg['browsers'][browser]['package'] + \
          " --allversions --yes --nocolor --limit-output --log-file=choco-log.log"
    logger.info("# Uninstalling the browser.")
    subprocess.Popen(cmd)
    logger.info("# Uninstalling done.")
    logger.info("# Removing installation folders.")
    for folder in cfg['browsers'][browser]['installFolders']:
        remove_item(folder)
    logger.info("All folders are removed.")


def get_ssl_screenshot(browser, version):
    """Getting the screenshot of SSL warning in given browser version."""
    # Loop through all cases
    for case in cfg['cases']:
        logger.info("#### Processing case %s %s", case, cfg['cases'][case]['url'])
        output()
        open_webpage(cfg['browsers'][browser]['binary'], cfg['cases'][case]['url'], version,
                     cfg['browsers'][browser]['package'])


if __name__ == '__main__':
    main()
