import subprocess
import time
import os

CURRENT_DIR = os.getcwd()


def check_requirements():
	print("Check drivers.")
	drivers_path = CURRENT_DIR + "\\drivers"
	cmd = 'echo %Path% | find /c ' + str(drivers_path)
	proc = subprocess.call(cmd, shell=True)
	time.sleep(5)
	print("Installing requirements.")
	pip_cmd = 'pip3 install -r requirements.txt'
	subprocess.Popen(pip_cmd)


check_requirements()