import logging
import os

# Create log directory if it doesn't exist
LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(LOG_DIR, "behave_test.log")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Set up logger
logger = logging.getLogger("behaveLogger")
logger.setLevel(logging.INFO)

# Create file handler which logs info messages
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(logging.INFO)

# Create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the handler to the logger if not already added
if not logger.hasHandlers():
    logger.addHandler(file_handler)