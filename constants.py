API_URL = 'https://api.example.com'
MAX_CONNECTION_RETRIES = 5
TIMEOUT_DURATION = 30
ERROR_MESSAGES = {
    'network': 'Network error occurred. Please try again.',
    'timeout': 'Request timed out. Please check your connection.',
    'invalid_response': 'Received an invalid response from the server.',
}

def get_error_message(error_type):
    """Fetches an error message based on the error type."""
    return ERROR_MESSAGES.get(error_type, 'An unknown error occurred.')

# Usage Example

if __name__ == '__main__':
    # Simulating a network error
    error_type = 'network'
    print(get_error_message(error_type))  # Outputs: Network error occurred. Please try again.

