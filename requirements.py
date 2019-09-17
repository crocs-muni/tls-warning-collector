import subprocess
import time
import os

CURRENT_DIR = os.getcwd()


def check_requirements():
    print("Check drivers.")
    drivers_path = CURRENT_DIR + "\\drivers"
    cmd = 'echo %Path% | find "tls-warning-collector-dev\\drivers"'
    proc = subprocess.call(cmd, shell=True)
    time.sleep(3)
    print("Installing requirements.")
    pip_cmd = 'pip3 install -r requirements.txt'
    subprocess.Popen(pip_cmd)


check_requirements()
