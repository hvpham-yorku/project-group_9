import sqlite3
import json
import sys

def search_database(query):
    conn = sqlite3.connect('search_engine.db')
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT url, title FROM pages WHERE content LIKE ?", ('%' + query + '%',))
    results = cursor.fetchall()
    conn.close()

    return [{"title": title, "url": url} for url, title in results]

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise ValueError("No query provided")

        search_query = sys.argv[1]
        results = search_database(search_query)

        print(json.dumps({"status": "success", "results": results}, indent=4))
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))
        sys.exit(1)
