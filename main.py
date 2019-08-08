from callback_functions import *


def main():
    """Function which makes it all work as a one function."""
    open_webpage(get_browser(), get_case_url(), get_version(), get_package())


if __name__ == '__main__':
    main()
