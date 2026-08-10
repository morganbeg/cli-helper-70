import logging

class CustomLogger:
    def __init__(self, log_file, level=logging.INFO):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)
        handler = logging.FileHandler(log_file)
        handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)

    def log_info(self, message):
        try:
            self.logger.info(message)
        except Exception as e:
            print(f"Error logging info: {e}")

    def log_warning(self, message):
        try:
            self.logger.warning(message)
        except Exception as e:
            print(f"Error logging warning: {e}")

    def log_error(self, message):
        try:
            self.logger.error(message)
        except Exception as e:
            print(f"Error logging error: {e}")

    def log_debug(self, message):
        try:
            self.logger.debug(message)
        except Exception as e:
            print(f"Error logging debug: {e}")

# Example usage: 
if __name__ == '__main__':
    logger = CustomLogger('app.log')
    logger.log_info('This is an info message.')
    logger.log_warning('This is a warning message.')
    logger.log_error('This is an error message.')
    logger.log_debug('This is a debug message.')
