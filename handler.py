import requests
import time
from requests.exceptions import RequestException

def retry_request(url, max_retries=3, delay=2):
    """
    Make a GET request to the specified URL with retry logic.
    :param url: URL to send the GET request.
    :param max_retries: Maximum number of retries before failing.
    :param delay: Delay in seconds between retries.
    :return: Response object if successful, None otherwise.
    """
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP errors
            return response
        except RequestException as e:
            print(f'Attempt {attempt + 1} failed: {e}')
            if attempt < max_retries - 1:
                time.sleep(delay)
            else:
                print('All attempts failed.')
                return None

# Example usage
if __name__ == '__main__':
    result = retry_request('https://example.com')
    if result:
        print('Request succeeded:', result.content)
    else:
        print('Request failed after retries.')