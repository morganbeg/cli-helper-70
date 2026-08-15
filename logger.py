import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=5*1024*1024, backup_count=3):
    logger = logging.getLogger('game_logger')
    logger.setLevel(logging.DEBUG)  

    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger

# Usage example
if __name__ == '__main__':
    my_logger = setup_logger()
    my_logger.info('Logger has been set up!')
    my_logger.debug('This is a debug message.')
    my_logger.error('This is an error message.')
