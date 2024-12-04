import React, { useState } from 'react';

function AISearch() {
  const [url, setUrl] = useState('');
  const [question, setQuestion] = useState('');
  const [result, setResult] = useState(null);

  const handleAISearch = async () => {
    try {
      const response = await fetch('http://localhost:4000/search-ai', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url, question }),
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error('Error:', error);
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
        placeholder="Enter question"
      />
      <button onClick={handleAISearch}>Search with AI</button>
      {result && (
        <div>
          <h3>AI Search Result:</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default AISearch;
