import logging
import os

# Define the log directory and file name
LOG_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(LOG_DIR, "behave_test.log")

# Create the log directory if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

# Set up the logger
logger = logging.getLogger("behaveLogger")
logger.setLevel(logging.INFO)

# Create file handler to write logs to a file
file_handler = logging.FileHandler(LOG_FILE, mode='a')
file_handler.setLevel(logging.INFO)

# Define log message format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the logger if not already added
if not logger.hasHandlers():
    logger.addHandler(file_handler)