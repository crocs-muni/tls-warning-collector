from setup_logger import output, logger
from browsers import *
import yaml
import os.path
import subprocess

class Iteration:
	def __init__(self, browser, version, case, url, package):
		self.browser = browser
		self.version = version
		self.case = case
		self.url = url
		self.package = package

	def set_browser(self, browser):
		self.browser = browser

	def set_case(self, case):
		self.case = case

	def set_version(self, version):
		self.version = version

	def set_package(self, package):
		self.package = package

	def set_url(self, url):
		self.url = url


iteration = Iteration('','','','','')


def read_config():
    """Load data from config.yaml to cfg"""
    try:
        with open('config.yaml', 'r') as yamlfile:
            conf = yaml.safe_load(yamlfile)
    except:
        logger.info("Some error occured while reading config.yaml")
    return conf


# Global variable cfg for configuration file
cfg = read_config()


def main():
    """Iterates over all of the browsers and versions and runs the script for screenshots"""
    for browserID in read_config()['browserIDs']:
        for version in cfg['browsers'][browserID]['test-versions']:
            logger.info('######## Processing %s v(%s)', browserID, version)
            try:
            		if browserID != 'edge':
                		install_browser(browserID, version)
            		get_ssl_screenshot(browserID, version)
            except Exception as e:
            	logger.error("Something went TERRIBLY wrong. - %s", e)
            finally:
            		uninstall_browser(browserID)


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
    cmd = "choco install " + str(cfg['browsers'][browser]['package']) + " --force --version=" + str(version) + \
          " --yes --nocolor --limit-output --no-progress --ignore-checksums --log-file=choco-log.log"
    logger.info("# Installing the browser.")
    subprocess.Popen(cmd)
    logger.info("# Installation done.")


def uninstall_browser(browser):
    """Uninstalls given browser."""
    cmd = "choco uninstall " + str(cfg['browsers'][browser]['package']) + \
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
    logger.info("# Preparing iteration.")
    for case in cfg['cases']:
    	logger.info("# Setting global variable for browser.")
    	iteration.set_browser(browser)
    	logger.info("# Global variable for browser set - %s.", get_browser())
    	logger.info("# Setting global variable for version.")
    	iteration.set_version(str(version))
    	logger.info("# Global variable for version set - %s.", get_version())
    	logger.info("# Setting global variable for case.")
    	iteration.set_case(case)
    	logger.info("# Global variable for case set - %s.", get_case())
    	logger.info("# Setting global variable for package.")
    	iteration.set_package(cfg['browsers'][browser]['package'])
    	logger.info("# Global variable for package set - %s.", get_package())
    	logger.info("#### Processing case %s %s", case, cfg['cases'][case]['url'])
    	output()
    	open_webpage(cfg['browsers'][browser]['binary'], cfg['cases'][case]['url'], str(version),
                     cfg['browsers'][browser]['package'])


def get_browser():
	logger.info('Browser is - %s', iteration.browser)
	return iteration.browser


def get_version():
	logger.info('Version is - %s', iteration.version)
	return iteration.version


def get_case():
	logger.info('Case is - %s', iteration.case)
	return iteration.case


def get_package():
	logger.info('Package is - %s', iteration.package)
	return iteration.package


if __name__ == '__main__':
    main()
