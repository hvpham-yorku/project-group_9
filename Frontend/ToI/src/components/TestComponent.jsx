// components/AISearch.js
import React, { useState } from 'react';
import axios from 'axios';

function AISearch() {
  const [url, setUrl] = useState('');
  const [question, setQuestion] = useState('');
  const [result, setResult] = useState(null);

  const handleAISearch = async () => {
    try {
      const response = await axios.post('http://localhost:3000/search-ai', { url, question });
      setResult(response.data);
    } catch (error) {
      setResult({ status: 'error', message: error.response?.data?.message || 'An error occurred' });
    }
  };

  return (
    <div>
      <h2>AI-Assisted Search</h2>
      <input 
        type="text" 
        value={url} 
        onChange={(e) => setUrl(e.target.value)} 
        placeholder="Enter URL"
      />
      <input 
        type="text" 
        value={question} 
        onChange={(e) => setQuestion(e.target.value)} 
        placeholder="Enter your question"
      />
      <button onClick={handleAISearch}>Search with AI</button>
      {result && (
        <div>
          <h3>Result:</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default AISearch;
