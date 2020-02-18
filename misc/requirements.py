import subprocess
import time
import os

CURRENT_DIR = os.getcwd()


def check_requirements():
    """Checks if all requirements are met."""
    check_if_admin()
    pip_cmd = 'pip3 install --quiet -r requirements.txt'
    subprocess.call(pip_cmd, shell=True)
    time.sleep(1)
    return


def check_if_admin():
    """Checks if user has Administrator Command Prompt running"""
    cmd = 'net session >nul 2>&1'
    is_admin = subprocess.call(cmd, shell=True)
    if is_admin == 0:
        pass
    else:
        print("You are not and Administrator. Change to Administrator Command Line in order to run this.")
        return
    return
