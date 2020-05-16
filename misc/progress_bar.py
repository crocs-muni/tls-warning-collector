from misc.setup_logger import logger


def set_progress_percentage(iteration, all_browsers):
    """Counts the progress percentage."""
    return float(iteration / all_browsers * 100)


def print_progress(progress_percentage, cases=False, versions=False):
    """Prints the progress info."""
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
    """Prints the progress bar."""
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

