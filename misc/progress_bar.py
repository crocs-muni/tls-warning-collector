from misc.setup_logger import logger


def set_progress_percentage(iteration, total):
    """
    Counts the progress percentage.
    :param iteration: Order number of browser or version
    :param total: Total number of browsers or versions
    :return: Percentage number
    """
    return float((iteration + 1) / total * 100)


def print_progress(progress_percentage, cases=False, versions=False):
    """
    Prints the progress info for cases, versions or the whole run.
    :param progress_percentage: Actual progress percentage number
    :param cases: True if printing progress for cases of particular version
    :param versions: True if printing progress for versions of particular browser
    :return: None
    """
    if cases:
        logger.info("")
        logger.info("Cases progress: ")
    elif versions: 
        logger.info("")
        logger.info("Versions Progress: ")
    else:
        logger.info("")
        logger.info("Main Progress: ")
    print_progress_bar(progress_percentage)


def print_progress_bar(progress_percentage):
    """
    Prints the progress bar.
    :param progress_percentage: Actual progress percentage number
    :return: None
    """
    length = 40
    perc_graph = (length * progress_percentage) / 100
    output = "["
    counter = 0
    for i in range(int(perc_graph)):
        output += "="
        counter += 1
    for j in range((length - counter) + 1):
        output += " "
    output += "] "
    output += str(round(progress_percentage,2))
    output += "%"
    logger.info(output)
    logger.info("")

