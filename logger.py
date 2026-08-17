import logging
from logging.handlers import RotatingFileHandler


def setup_logger(log_file='game.log', max_bytes=5 * 1024 * 1024, backup_count=5):
    """Sets up a logger that rotates log files."""
    # Create a logger object
    logger = logging.getLogger('game_logger')
    logger.setLevel(logging.DEBUG)  # Set the logging level

    # Create a handler for rotating file logging
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)  # Set level for handler

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger

# Example usage of the logger setup
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger has been set up.')