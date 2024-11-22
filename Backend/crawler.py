# Import required libraries
import requests  # For making HTTP requests
import urllib.robotparser  # For parsing robots.txt files
from bs4 import BeautifulSoup  # For HTML parsing
from urllib.parse import urljoin, urlparse  # For URL manipulation
from collections import deque  # For implementing a queue
import time  # For implementing delays
import sqlite3  # For database interaction
import json  # For JSON formatting
import sys  # For accessing command-line arguments

# Function to check if a URL is valid
def is_valid_url(url):
    """
    Validates if the given URL has a proper scheme (http/https) and domain.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

# Function to fetch and parse robots.txt for a domain
def fetch_robots_txt(domain):
    """
    Retrieves the robots.txt file for a domain and parses it.
    If unavailable, assumes crawling is allowed.
    """
    robots_url = f"https://{domain}/robots.txt"
    parser = urllib.robotparser.RobotFileParser()
    try:
        response = requests.get(robots_url, timeout=5)
        if response.status_code == 200:
            parser.parse(response.text.splitlines())
        else:
            parser.allow_all = True  # Default to allowing crawling
    except Exception:
        parser.allow_all = True  # Handle errors gracefully
    return parser

# Function to check if crawling a URL is allowed by robots.txt
def is_allowed(url, robot_parsers):
    """
    Checks if the given URL can be crawled based on robots.txt rules.
    Caches parsers to avoid redundant requests.
    """
    parsed_url = urlparse(url)
    domain = f"{parsed_url.scheme}://{parsed_url.netloc}"
    if domain not in robot_parsers:
        robot_parsers[domain] = fetch_robots_txt(domain)
    parser = robot_parsers[domain]
    return parser.can_fetch("*", url)

# Main crawling function
def crawl(seed_urls, depth=2, limit=50):
    """
    Crawls the web starting from a list of seed URLs up to a specified depth.
    Limits the number of pages crawled to `limit`.
    """
    visited = set()  # To track visited URLs
    queue = deque([(url, depth) for url in seed_urls])  # Queue for BFS with depth tracking
    crawled_data = []  # To store crawled data
    robot_parsers = {}  # Cache for robots.txt parsers

    while queue and len(crawled_data) < limit:
        url, depth = queue.popleft()
        if depth == 0 or url in visited:  # Skip if depth is zero or URL is already visited
            continue
        if not is_allowed(url, robot_parsers):  # Check robots.txt rules
            continue
        visited.add(url)  # Mark URL as visited

        try:
            response = requests.get(url, timeout=3)  # Fetch the page
            if response.status_code != 200:
                continue  # Skip non-successful responses
        except requests.RequestException:
            continue  # Handle connection errors gracefully

        # Parse the page content
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title').text if soup.find('title') else 'No Title'
        text = soup.get_text(separator=" ", strip=True)
        crawled_data.append({'url': url, 'title': title, 'content': text})

        # Find and enqueue valid links
        for link in soup.find_all('a', href=True):
            next_url = urljoin(url, link['href'])  # Resolve relative URLs
            if is_valid_url(next_url) and next_url not in visited:
                queue.append((next_url, depth - 1))  # Enqueue with reduced depth

        time.sleep(1)  # Politeness delay

    return crawled_data

# Function to save crawled data to an SQLite database
def save_to_database(crawled_data):
    """
    Saves crawled data (URLs, titles, and content) into an SQLite database.
    Creates the table if it does not exist.
    """
    conn = sqlite3.connect('search_engine.db')  # Connect to the database
    cursor = conn.cursor()

    # Create the pages table if it doesn't already exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS pages (
                        id INTEGER PRIMARY KEY,
                        url TEXT UNIQUE,
                        title TEXT,
                        content TEXT
                    )''')

    # Insert crawled data into the table
    for page in crawled_data:
        try:
            cursor.execute('INSERT OR IGNORE INTO pages (url, title, content) VALUES (?, ?, ?)',
                           (page['url'], page['title'], page['content']))
        except sqlite3.IntegrityError:
            continue  # Skip duplicate entries

    conn.commit()  # Save changes
    conn.close()  # Close the database connection

# Main execution block
if __name__ == "__main__":
    try:
        # Accept seed URLs from command-line arguments
        seed_urls = sys.argv[1:]
        if not seed_urls:
            raise ValueError("No seed URLs provided")

        # Start crawling and save the results
        crawled_data = crawl(seed_urls)
        save_to_database(crawled_data)

        # Output success message with the number of records crawled
        print(json.dumps({"status": "success", "records_crawled": len(crawled_data)}))
    except Exception as e:
        # Handle errors and output a JSON-formatted error message
        print(json.dumps({"status": "error", "message": str(e)}))
        sys.exit(1)
