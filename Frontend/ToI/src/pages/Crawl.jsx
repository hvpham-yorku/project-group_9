import React, { useState } from 'react';
import axios from 'axios';

// This page allows the user to use the web-crawling functionality
function Crawler() {
  const [urls, setUrls] = useState('');
  const [result, setResult] = useState(null);

  //This function makes a call to the "crawl" in the backend and passes the list of urls
  const handleCrawl = async () => {
    try {
      const response = await axios.get(`http://localhost:4000/crawl?urls=${urls}`);
      setResult(response.data);
    } catch (error) {
      setResult({ status: 'error', message: error.response?.data?.message || 'An error occurred' });
    }
  };

  //This block displays the UI for the page
  return (
    <div>
      <p className="text-8xl pb-10">Web Crawler</p>

      {/* This is the textbox for input */}
      <input
        type="text"
        value={urls}
        onChange={(e) => setUrls(e.target.value)}
        placeholder="Enter comma-separated URLs"
      />

      {/* Clicking on this button calls the crawling function */}
      <button onClick={handleCrawl}>Crawl</button>

      {/* Display the results */}
      {result && (
        <div>
          <h3>Crawl Result:</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default Crawler;