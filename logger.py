import logging
from logging.handlers import RotatingFileHandler

# Set up a logger for the application
logger = logging.getLogger('game_logger')
logger.setLevel(logging.DEBUG)

# Create a rotating file handler
def setup_logger(log_file='game.log', max_bytes=5 * 1024 * 1024, backup_count=3):
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

# Call the setup function to initialize the logger
setup_logger()

# Example usage
if __name__ == '__main__':
    logger.debug('Debug message')
    logger.info('Info message')
    logger.warning('Warning message')
    logger.error('Error message')
    logger.critical('Critical message')