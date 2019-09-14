import subprocess
import time
import os

CURRENT_DIR = os.getcwd()


def check_requirements():
    pip_cmd = 'pip3 install -r requirements.txt'
    subprocess.Popen(pip_cmd)
    time.sleep(10)
    drivers_path = CURRENT_DIR + "\\drivers"
    cmd = 'echo "$PATH"|grep -q' + drivers_path + '&& echo "drivers are in the PATH! You can continue."'
    subprocess.Popen(cmd)
