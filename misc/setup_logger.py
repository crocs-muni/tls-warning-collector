import logging
import time
import os

TIMESTAMP = time.strftime("%d-%m-%Y-%H%M%S")
CURRENT_DIR = os.getcwd()
LOG_FILE = CURRENT_DIR + "\\logs\\logfile" + TIMESTAMP + ".log"

# Create directory logs in current dir if it does not already exist.
if not os.path.exists("logs"):
    try:
        os.makedirs("logs")
    except OSError as e:
        raise e

# Set-up basic configuration. This needs to be set-up only once.
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%d-%b-%y %H:%M:%S", level=0, handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()])
# Creating logger which will be used in other files.
logger = logging.getLogger("tls-warning-collector")


def output(browser, version, case):
    """
    Output for the test iteration
    :param browser: Browser
    :param version: Browser version
    :param case: Case to collect
    :return: None
    """
    logger.info("##################################################")
    logger.info("                                                  ")
    logger.info("           {} {} {}         ".format(browser, version, case))
    logger.info("                                                  ")
    logger.info("##################################################")
