from misc.setup_logger import output, logger
from misc.progress_bar import set_progress_percentage, print_progress
from misc.requirements import check_requirements

from browsers.firefox import firefox
from browsers.opera import opera
from browsers.chromium import chromium
from browsers.chrome import chrome
from browsers.iexplorer import iexplorer
from browsers.edge import edge

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
    all_browsers = len(read_config().get('browserIDs'))
    for index, browserID in enumerate(read_config().get('browserIDs')):
        all_versions = cfg.get('browsers')[browserID].get('one-version')
        progress = set_progress_percentage(index + 1, all_browsers)
        for v_index, version in enumerate(all_versions):
            v_progress = set_progress_percentage(v_index + 1, len(all_versions))
            logger.info('######## Processing %s v(%s)', browserID, version)
            if browserID != 'edge':
                return_code = install_browser(browserID, version)
                if return_code != 0:
                    logger.error("# Installation failed...")
                    uninstall_browser(browserID)
                    logger.info("# Skipping to the next browser version.")
                    continue
            get_ssl_screenshot(browserID, version)
            print_progress(v_progress, versions=True)
            uninstall_browser(browserID)
        print_progress(progress)


def install_browser(browser, version):
    """Installs the given browsers version."""
    cmd = "choco install " + str(cfg.get('browsers')[browser].get('package')) + " --force --version=" + str(version) + \
          " --yes --nocolor --limit-output --no-progress --ignore-checksums --log-file=choco-log.log"
    logger.info("# Installing the browser.")
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    logger.info("# Please wait...")
    for _ in process.stdout.readlines():
        process.wait()
    rc = process.returncode
    return rc


def uninstall_browser(browser):
    """Uninstalls the given browsers."""
    cmd = "choco uninstall " + str(cfg.get('browsers')[browser].get('package')) + \
          " --allversions --yes --nocolor --limit-output --log-file=choco-log.log"
    logger.info("# Uninstalling the browsers.")
    subprocess.Popen(cmd)
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    logger.info("# Please wait...")
    for _ in process.stdout.readlines():
        process.wait()
    logger.info("# Uninstalling done.")
    logger.info("# Removing installation folders.")
    for folder in cfg.get('browsers')[browser].get('installFolders'):
        remove_item(folder)


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


def get_ssl_screenshot(browser, version):
    """Gets the screenshot of SSL warning in the given browsers version."""
    # Loop through all cases
    logger.info("# Preparing iteration.")
    all_cases = len(cfg.get('cases'))
    iteration = 0
    for case in cfg['cases']:
        iteration += 1
        progress = set_progress_percentage(iteration, all_cases)
        try:
            output(browser, str(version), case)
            open_webpage(cfg.get('browsers')[browser].get('binary'), cfg.get('cases')[case].get('url'), case, str(version),
                     cfg.get('browsers')[browser].get('package'))
        except Exception as e:
            logger.error("Something went TERRIBLY wrong. - %s", e)
        print_progress(progress, cases=True)


def open_webpage(browser, url, case, version, package):
    """Opens the URL in desired browsers."""
    if browser == 'firefox':
        firefox(browser, version, case, package, url)
    if browser == 'opera':
        opera(browser, version, case, package, url)
    if package == 'chromium':
        chromium(browser, version, case, package, url)
    if browser == 'chrome' and package != 'chromium':
        chrome(browser, version, case, package, url)
    if browser == 'ie':
        iexplorer(browser, version, case, package, url)
    if browser == 'edge':
        edge(browser, version, case, package, url)


if __name__ == '__main__':
    main()
