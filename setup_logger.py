import logging
import time
import os

# Create directory logs if it does not already exist.
if not os.path.exists('logs'):
    os.makedirs('logs')

# Set-up basic configuration. This needs to be set-up only once.
timestamp = time.strftime("%d-%m-%Y")
filename = '/logs/logfile' + timestamp + '.log'
logging.basicConfig(filename='', format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=0)
# Creating logger which will be used in other files.
logger = logging.getLogger('tls-warning-collector')
