import React, { useState } from 'react';

// This page allows the user to use the web-crawling functionality
function AISearch() {
  const [url, setUrl] = useState('');
  const [question, setQuestion] = useState('');
  const [result, setResult] = useState(null);

  //This function makes a call to the "search-ai" in the backend and passes the url as well as the question
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


  //This block displays the UI for the page
  return (
    <div>
      <p className="text-8xl pb-10">Search</p>

      {/* This is the textbox for inputting the URL to be searched */}
      <input
        type="text"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        placeholder="Enter URL"
      />

      {/* This is the textbox for inputting the question to search the URL for */}
      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Enter question"
      />

      {/* Clicking this button passes the values in the texboxes as arguments to the function that calls the backend */}
      <button onClick={handleAISearch}>Search with AI</button>

      {/* This block displays the results of the query */}
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
