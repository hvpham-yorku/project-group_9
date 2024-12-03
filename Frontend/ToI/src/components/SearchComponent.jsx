import React, { useState } from 'react';
import axios from 'axios';


// This component makes an API call to the backend and then displays the search result
function SearchComponent() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);

    // The code block below attempts to send a query to the backend save the results in the "response" variable
    try {
      const response = await axios.get(`http://localhost:3000/search?q=${query}`);
      setResults(response.data.results || []);
    } catch (err) {
      setError(err.response?.data?.message || 'There was an error');
      const response = "error";
    } finally {
      setIsLoading(false);
    }
  };

  // The code block below displays the results from the backend
  return (
    <div>
      <form onSubmit={handleSearch}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Enter search query"
        />
        <button type='submit'>Traditional Search</button>
      </form>

      {isLoading && <p>Loading...</p>}
      {error && <p>Error: {error}</p>}
      {results.length > 0 && (
        <div>
          <h2>Search Results:</h2>
          <ul>
            {results.map((result, index) => (
              <li key={index}>
                <p className='text-2xl'>{result.title}</p>
                <p>{result.url}</p>
              </li>
            ))}
          </ul>
        </div>
      )}
      {results.length === 0 && !isLoading && <p>No results found.</p>}
    </div>
  );
}

export default SearchComponent;
