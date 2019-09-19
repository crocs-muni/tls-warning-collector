import subprocess
import time
import os

CURRENT_DIR = os.getcwd()


def check_requirements():
	"""Checks if all requirements are met."""
    check_if_admin()
 	check_if_in_path()
    pip_cmd = 'pip3 install --quiet -r requirements.txt'
    subprocess.call(pip_cmd, shell=True)
    time.sleep(1)
    return


def check_if_in_path():
	"""Checks if drivers folder is in PATH"""
	drivers_path = CURRENT_DIR + "\\drivers"
    cmd = 'echo %Path% | find "tls-warning-collector-dev\\drivers" >nul'
    proc = subprocess.call(cmd, shell=True)
    if proc == 0:
        pass
    else:
        print("Drivers are NOT in Path. Follow instructions in the drivers folder and then re-run this program.")
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
