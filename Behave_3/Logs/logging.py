import logging

# Create or get a logger
logger = logging.getLogger("behave_logger")
logger.setLevel(logging.INFO)

# Formatter for logs
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# File handler for writing logs to a file
file_handler = logging.FileHandler("Logs/behave_test_log.log", mode="w")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Console handler for displaying logs in the terminal
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Behave hooks for logging
def before_scenario(context, scenario):
    logger.info(f"Scenario started: {scenario.name}")

def after_scenario(context, scenario):
    if scenario.status == "passed":
        logger.info(f"Scenario passed: {scenario.name}")
    elif scenario.status == "failed":
        logger.error(f"Scenario failed: {scenario.name}")
    else:
        logger.warning(f"Scenario ended with status {scenario.status}: {scenario.name}")

def before_step(context, step):
    if "open" in step.name.lower():
        logger.info(f"Page opened: {step.name}")

def after_step(context, step):
    if "close" in step.name.lower():
        logger.info(f"Page closed: {step.name}")
    if step.status == "failed":
        logger.error(f"Error in step: {step.name} - {step.exception}")