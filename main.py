import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
import time
import sqlite3

# Helper function to validate URLs
def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

# Crawl function: Crawl multiple websites starting from seed URLs
def crawl(seed_urls, depth=2, limit=50):
    visited = set()
    queue = deque([(url, depth) for url in seed_urls])
    crawled_data = []

    while queue and len(crawled_data) < limit:
        url, depth = queue.popleft()
        if depth == 0 or url in visited:
            continue
        visited.add(url)

        try:
            response = requests.get(url, timeout=3)
            if response.status_code != 200:
                continue
        except requests.RequestException:
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        print(f"Crawling URL: {url}")

        # Extract page info for indexing
        title = soup.find('title').text if soup.find('title') else 'No Title'
        text = soup.get_text(separator=" ", strip=True)
        crawled_data.append({'url': url, 'title': title, 'content': text})

        # Find new links to crawl
        for link in soup.find_all('a', href=True):
            next_url = urljoin(url, link['href'])
            if is_valid_url(next_url) and next_url not in visited:
                queue.append((next_url, depth - 1))

        time.sleep(1)  # Be polite by pausing between requests

    return crawled_data

# Function to save crawled data to SQLite database
def save_to_database(crawled_data):
    conn = sqlite3.connect('search_engine.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS pages (
                        id INTEGER PRIMARY KEY,
                        url TEXT,
                        title TEXT,
                        content TEXT
                    )''')

    for page in crawled_data:
        cursor.execute('INSERT INTO pages (url, title, content) VALUES (?, ?, ?)',
                       (page['url'], page['title'], page['content']))

    conn.commit()
    conn.close()

# Function to search the database for a query term
def search_database(query):
    conn = sqlite3.connect('search_engine.db')
    cursor = conn.cursor()

    cursor.execute("SELECT url, title FROM pages WHERE content LIKE ?", ('%' + query + '%',))
    results = cursor.fetchall()
    conn.close()

    return results

# Example usage
if __name__ == "__main__":
    # Step 1: Start crawling from seed URLs
    seed_urls = ["https://www.cnn.com", "https://www.cnn.com/politics/live-news/election-trump-harris-11-08-24/index.html", "https://www.worlddata.info"]
    crawled_data = crawl(seed_urls)

    # Step 2: Save the crawled data to the database
    save_to_database(crawled_data)

    # Step 3: Search the database
    search_query = input("Enter search query: ")
    results = search_database(search_query)

    # Display search results
    if results:
        for url, title in results:
            print(f"Title: {title}, URL: {url}")
    else:
        print("No results found.")
