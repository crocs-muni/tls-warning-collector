import os.path
import subprocess

from misc.setup_logger import output, logger
from misc.progress_bar import set_progress_percentage, print_progress
from misc.requirements import check_requirements, install_dependencies
from misc.database import insert_into_db, get_sum_from_db, prepare_db, cfg
from misc.browser import Browser

from browsers.firefox import firefox
from browsers.opera import opera
from browsers.chromium import chromium
from browsers.iexplorer import iexplorer
from browsers.edge import edge


def main():
    """
    Iterates over all of the browsers and versions and runs the script for getting screenshots.
    :return None
    """
    install_dependencies()
    if not check_requirements():
        return
    prepare_db()
    all_browsers_count = len(cfg.get("browserIDs"))
    for index, browserID in enumerate(cfg.get("browserIDs")):
        all_versions = cfg.get("browsers")[browserID].get("versions")
        collect_warnings(all_versions, browserID)
        progress = set_progress_percentage(index, all_browsers_count)
        print_progress(progress)
    get_sum_from_db()


def collect_warnings(all_versions, browser):
    """
    Iterates over all of the browser versions and runs the script for getting screenshots.
    :param all_versions: All browser versions for the collection
    :param browser: Browser
    :return: None
    """
    all_versions_count = len(all_versions)
    for v_index, version in enumerate(all_versions):
        v_progress = set_progress_percentage(v_index, all_versions_count)
        logger.info("######## Processing {} v({})".format(browser, version))
        if browser != "edge":
            return_code = install_browser(browser, version)
            insert_into_db(browser, version, 0)
            if return_code != 0:
                logger.error("# Installation failed...Skipping to the next browser version.")
                continue
        get_ssl_screenshot(browser, version)
        print_progress(v_progress, versions=True)
        uninstall_browser(browser)


def install_browser(browser, version):
    """
    Installs the given browsers version.
    :param browser: Browser
    :param version: Browser version
    :return: True if installation was successful, False otherwise
    """
    cmd = "choco install " + str(cfg.get("browsers")[browser].get("package")) + " --force --version="\
        + str(version) + " --yes --nocolor --limit-output --no-progress --ignore-checksums " \
        "--log-file=choco-log.log"
    logger.info("# Installing the browser.")
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    logger.info("# Please wait...")
    for _ in process.stdout.readlines():
        process.wait()
    return process.returncode


def uninstall_browser(browser):
    """
    Uninstalls the given browsers.
    :param browser: Browser
    :return: None
    """
    cmd = "choco uninstall " + str(cfg.get("browsers")[browser].get("package")) + \
          " --allversions --yes --nocolor --limit-output --log-file=choco-log.log"
    logger.info("# Uninstalling the browsers.")
    subprocess.Popen(cmd)
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    logger.info("# Please wait...")
    for _ in process.stdout.readlines():
        process.wait()
    logger.info("# Uninstalling done.")
    logger.info("# Removing installation folders.")
    for folder in cfg.get("browsers")[browser].get("installFolders"):
        remove_item(folder)


def remove_item(item):
    """
    Removes the given directory.
    :param item: Folder to be removed
    :return: None
    """
    if os.path.exists(item):
        logger.info("# Removing item: {}".format(item))
        try:
            os.rmdir(item)
        except OSError:
            logger.error("Error occured while deleting item: {}".format(item))
    else:
        logger.info("# Item does not exist, not removing: {}".format(item))


def get_ssl_screenshot(browser, version):
    """
    Gets the screenshot of SSL warning in the given browsers version.
    :param browser: Browser
    :param version: Browser version
    :return: None
    """
    logger.info("# Preparing iteration.")
    all_cases = len(cfg.get("cases"))
    for index, case in enumerate(cfg.get("cases")):
        progress = set_progress_percentage(index, all_cases)
        try:
            output(browser, str(version), case)
            open_webpage(cfg.get("browsers")[browser].get("binary"), cfg.get("cases")[case].get("url"), case,
                         str(version), cfg.get("browsers")[browser].get("package"))
        except Exception as e:
            logger.error("Something went TERRIBLY wrong. - {}".format(e))
        print_progress(progress, cases=True)


def open_webpage(browser, url, case, version, package):
    """
    Opens the URL in desired browsers.
    :param browser: Browser
    :param url: Case URL
    :param case: Case to be collected
    :param version: Browser version
    :param package: Browser package name
    :return: None
    """
    browser_obj = Browser(browser, version, case, package, url)
    if browser == "firefox":
        firefox(browser_obj)
    elif browser == "opera":
        opera(browser_obj)
    elif package == "chromium":
        chromium(browser_obj)
    elif browser == "ie":
        iexplorer(browser_obj)
    elif browser == "edge":
        edge(browser_obj)


if __name__ == "__main__":
    main()
