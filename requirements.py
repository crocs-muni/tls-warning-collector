import subprocess
import time
import os

CURRENT_DIR = os.getcwd()


def check_requirements():
	print("Check drivers.")
	drivers_path = CURRENT_DIR + "\\drivers"
	cmd = 'echo %Path% | find "tls-warning-collector-dev\\drivers"'
	proc = subprocess.call(cmd, shell=True)
	if proc == 0:
		# Everything went well and the drivers are in Path
		print("Drivers are in path. Continue installation...")
	else:
		print("Drivers are NOT in Path. Follow instructions in the drivers folder and then re-run this program.")
		return 0
	time.sleep(1)
	print("Installing requirements.")
	pip_cmd = 'pip3 install -r requirements.txt'
	subprocess.Popen(pip_cmd)
	time.sleep(1)
	return 0


if __name__ == '__main__':
	check_requirements()
