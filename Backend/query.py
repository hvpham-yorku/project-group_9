# Import required libraries
import sqlite3  # For database interaction
import json  # For JSON formatting and output
import sys  # For accessing command-line arguments

# Function to search the database
def search_database(query):
    """
    Searches the database for records where the content matches the given query.
    Returns a list of dictionaries containing the titles and URLs of matching pages.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect('search_engine.db')
    cursor = conn.cursor()

    # Execute the search query, using a LIKE clause for partial matches
    cursor.execute("SELECT DISTINCT url, title FROM pages WHERE content LIKE ?", ('%' + query + '%',))
    results = cursor.fetchall()  # Fetch all matching rows

    # Close the database connection
    conn.close()

    # Format the results as a list of dictionaries
    return [{"title": title, "url": url} for url, title in results]

# Main execution block
if __name__ == "__main__":
    try:
        # Ensure a search query is provided as a command-line argument
        if len(sys.argv) < 2:
            raise ValueError("No query provided")  # Raise an error if no query is provided

        # Get the search query from the command-line arguments
        search_query = sys.argv[1]

        # Perform the database search
        results = search_database(search_query)

        # Output the results as a JSON-formatted success message
        print(json.dumps({"status": "success", "results": results}, indent=4))
    except Exception as e:
        # Handle errors and output a JSON-formatted error message
        print(json.dumps({"status": "error", "message": str(e)}))
        sys.exit(1)  # Exit with a non-zero status to indicate an error
