import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=10*1024*1024, backup_count=5):
    # Create a logger
    logger = logging.getLogger('app_logger')
    logger.setLevel(logging.DEBUG)

    # Create a file handler that rotates the log files
the   file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    file_handler.setLevel(logging.DEBUG)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(file_handler)

    return logger

# Example of using the logger setup
if __name__ == '__main__':
    logger = setup_logger()
    logger.debug('This is a debug message')
    logger.info('Logger setup complete')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')