from setup_logger import logger


def set_progress_percentage(iteration, all_browsers):
    """Counts the progress percentage."""
    return float((iteration + 1) / all_browsers * 100)


def print_progress(progress_percentage):
    """Prints the progress info."""
    logger.info("Progress: ")
    print_progress_bar(progress_percentage)


def print_progress_bar(progress_percentage):
    """Prints the progress bar."""
    length = 40
    perc_graph = (length * progress_percentage) / 100
    output = "["
    counter = 0
    for i in range(perc_graph):
        output += "="
        counter += 1
    for j in range((length - counter) + 1):
        output += " "
    output += "]"
    logger.info(output)
