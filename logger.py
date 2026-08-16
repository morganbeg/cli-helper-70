import logging
from logging.handlers import RotatingFileHandler

# Set up a logger for the application
logger = logging.getLogger('cli_helper')
logger.setLevel(logging.DEBUG)  # Set logging level to DEBUG

# Define a rotating file handler
handler = RotatingFileHandler('cli_helper.log', maxBytes=5*1024*1024, backupCount=3)
handler.setLevel(logging.DEBUG)  # Log debug and above to this file

# Create a formatter and set it for the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)  

# Example usage of the logger
logger.info("Logger setup complete.")
logger.debug("This is a debug message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")