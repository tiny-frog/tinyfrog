import backoff
import requests

def is_retryable_error(exception):
    if isinstance(exception, requests.HTTPError):
        status_code = exception.response.status_code
        return status_code >= 400 and status_code < 600
    return False

def get_with_retries(url: str, **kwargs) -> requests.Response:
    """
    Wrapper around reqsuests.get() that retries on network errors and 5xx responses.

    Args:
        url (str): URL to request.
        **kwargs: Keyword arguments passed to requests.get().
        max_tries (int): Maximum number of times to retry the request. Defaults to 5.

    Returns:
        requests.Response: The response object.
    """

    max_tries = kwargs.pop('max_tries', 5)  # Get max_tries from kwargs or use default 5
    giveup_func = lambda e, tries: tries >= max_tries or not is_retryable_error(e)
    
    @backoff.on_exception(backoff.expo, requests.RequestException, giveup=giveup_func)
    def retryable_get(url, **kwargs):
        response = requests.get(url, **kwargs)
        response.raise_for_status()
        return response
    
    return retryable_get(url, **kwargs)


