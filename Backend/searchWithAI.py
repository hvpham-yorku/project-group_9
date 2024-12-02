import os
import requests
import webscraping_ai
import argparse
import json
import sys
from dotenv import load_dotenv
from webscraping_ai.rest import ApiException
from pprint import pprint
from urllib.parse import urlparse

# Load environment variables
load_dotenv()

# Configure API client
configuration = webscraping_ai.Configuration(
    host="https://api.webscraping.ai"
)
configuration.api_key['api_key'] = os.getenv("API_KEY")  # Ensure your API key is set as an environment variable

def validate_url(url):
    """
    Validates a URL by checking:
    - Proper format (scheme and netloc)
    - If the domain is reachable

    Args:
        url (str): The URL to validate.

    Returns:
        bool: True if valid and reachable, False otherwise.
    """
    parsed_url = urlparse(url)
    if not (parsed_url.scheme and parsed_url.netloc):
        print("Error: The URL is not properly formatted.")
        return False

    try:
        # Attempt to reach the domain
        response = requests.head(url, timeout=5)
        if response.status_code >= 400:
            print(f"Warning: The URL is reachable but returned a status code {response.status_code}.")
        return True
    except requests.RequestException as e:
        print(f"Error: Unable to reach the URL. Details: {e}")
        return False

def check_internet_connection():
    """
    Checks if the system has an active internet connection.

    Returns:
        bool: True if the internet is accessible, False otherwise.
    """
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.RequestException:
        return False

def scrape_website(url, question):
    """
    Scrape the content of a website and ask a specific question about the page.

    Args:
        url (str): The URL of the website to scrape.
        question (str): A question or instruction to summarize the page content.

    Returns:
        dict: A dictionary containing the response from the WebScraping.AI API.
    """
    # Default scraping parameters
    context_limit = 4000
    response_tokens = 100
    on_context_limit = 'error'
    timeout = 10000  # in milliseconds
    js = True  # Enable JavaScript rendering
    js_timeout = 2000
    proxy = 'datacenter'
    country = 'us'
    device = 'desktop'
    error_on_404 = False
    error_on_redirect = False
    headers = {}  # Add any custom headers if required
    js_script = ''  # Leave empty if no custom JavaScript is needed

    # Use the WebScraping.AI API
    try:
        with webscraping_ai.ApiClient(configuration) as api_client:
            api_instance = webscraping_ai.AIApi(api_client)
            api_response = api_instance.get_question(
                url,
                question=question,
                context_limit=context_limit,
                response_tokens=response_tokens,
                on_context_limit=on_context_limit,
                headers=headers,
                timeout=timeout,
                js=js,
                js_timeout=js_timeout,
                proxy=proxy,
                country=country,
                device=device,
                error_on_404=error_on_404,
                error_on_redirect=error_on_redirect,
                js_script=js_script
            )
            return api_response
    except ApiException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='WebScraping Tool')
    parser.add_argument('url', help='The website URL to scrape')
    parser.add_argument('question', help='Your question or instruction for the webpage')
    args = parser.parse_args()

    target_url = args.url
    question = args.question

    # Check internet connection
    if not check_internet_connection():
        print(json.dumps({"status": "error", "message": "No internet connection. Please check your network and try again."}))
        sys.exit(1)

    # Validate the URL
    if not validate_url(target_url):
        print(json.dumps({"status": "error", "message": "Invalid or unreachable URL"}))
        sys.exit(1)

    # Scrape the website and get the response
    response = scrape_website(target_url, question)

    if "error" in response:
        print(json.dumps({"status": "error", "message": response['error']}))
        sys.exit(1)
    else:
        print(json.dumps({"status": "success", "response": response}))