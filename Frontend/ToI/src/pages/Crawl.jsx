import React, { useState } from 'react';
import axios from 'axios';

function Crawler() {
  const [urls, setUrls] = useState('');
  const [result, setResult] = useState(null);

  const handleCrawl = async () => {
    try {
      const response = await axios.get(`http://localhost:4000/crawl?urls=${urls}`);
      setResult(response.data);
    } catch (error) {
      setResult({ status: 'error', message: error.response?.data?.message || 'An error occurred' });
    }
  };

  return (
    <div>
      <h2>Web Crawler</h2>
      <input
        type="text"
        value={urls}
        onChange={(e) => setUrls(e.target.value)}
        placeholder="Enter comma-separated URLs"
      />
      <button onClick={handleCrawl}>Crawl</button>
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
