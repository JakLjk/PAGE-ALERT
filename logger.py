import logging 

# Variable can be implemented into proper config file, and imported
LOG_PATH = ""

# If path for logging file was defined:
if LOG_PATH:
        handlers = [logging.FileHandler(LOG_PATH),
                    logging.StreamHandler()]
# If path for logging file was not defined, don't save logs, just display them:        
else: 
    handlers = [logging.StreamHandler()]

# using implementation from logging module
logger = logging

logger.basicConfig(
    level=logging.INFO,
    # Formatting of logging information, that will be displayed.
    format="%(asctime)s [%(levelname)s] %(message)s ||| [%(threadName)s] ",
    handlers=handlers)