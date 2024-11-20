import requests
import urllib.robotparser
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
import time
import sqlite3
import json
import sys

def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def fetch_robots_txt(domain):
    robots_url = f"https://{domain}/robots.txt"
    parser = urllib.robotparser.RobotFileParser()
    try:
        response = requests.get(robots_url, timeout=5)
        if response.status_code == 200:
            parser.parse(response.text.splitlines())
        else:
            parser.allow_all = True
    except Exception:
        parser.allow_all = True
    return parser

def is_allowed(url, robot_parsers):
    parsed_url = urlparse(url)
    domain = f"{parsed_url.scheme}://{parsed_url.netloc}"
    if domain not in robot_parsers:
        robot_parsers[domain] = fetch_robots_txt(domain)
    parser = robot_parsers[domain]
    return parser.can_fetch("*", url)

def crawl(seed_urls, depth=2, limit=50):
    visited = set()
    queue = deque([(url, depth) for url in seed_urls])
    crawled_data = []
    robot_parsers = {}

    while queue and len(crawled_data) < limit:
        url, depth = queue.popleft()
        if depth == 0 or url in visited:
            continue
        if not is_allowed(url, robot_parsers):
            continue
        visited.add(url)

        try:
            response = requests.get(url, timeout=3)
            if response.status_code != 200:
                continue
        except requests.RequestException:
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('title').text if soup.find('title') else 'No Title'
        text = soup.get_text(separator=" ", strip=True)
        crawled_data.append({'url': url, 'title': title, 'content': text})

        for link in soup.find_all('a', href=True):
            next_url = urljoin(url, link['href'])
            if is_valid_url(next_url) and next_url not in visited:
                queue.append((next_url, depth - 1))

        time.sleep(1)

    return crawled_data

def save_to_database(crawled_data):
    conn = sqlite3.connect('search_engine.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS pages (
                        id INTEGER PRIMARY KEY,
                        url TEXT UNIQUE,
                        title TEXT,
                        content TEXT
                    )''')

    for page in crawled_data:
        try:
            cursor.execute('INSERT OR IGNORE INTO pages (url, title, content) VALUES (?, ?, ?)',
                           (page['url'], page['title'], page['content']))
        except sqlite3.IntegrityError:
            continue

    conn.commit()
    conn.close()

if __name__ == "__main__":
    try:
        seed_urls = sys.argv[1:]  # Accept seed URLs as arguments
        if not seed_urls:
            raise ValueError("No seed URLs provided")

        crawled_data = crawl(seed_urls)
        save_to_database(crawled_data)

        print(json.dumps({"status": "success", "records_crawled": len(crawled_data)}))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))
        sys.exit(1)