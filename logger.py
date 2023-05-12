import logging 
from logging.handlers import RotatingFileHandler


from pathlib import Path


base_path = str(Path(__file__).parent)
file_name = '/Logs/main_log'

full_path = base_path + file_name

# New Logging Script

log_format = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s ||| [%(threadName)s] ")

logger = logging.getLogger('root')
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_format)
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)

if full_path != '':
    file_handler = RotatingFileHandler(full_path, mode='a', maxBytes=5*1024*1024,
                                    backupCount=2, encoding=None, delay=False)
    file_handler.setFormatter(log_format)
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)




