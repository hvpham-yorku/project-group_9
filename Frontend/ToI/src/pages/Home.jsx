import React from "react";


// This is the page that currently serves as the frontend for the searching functionality
export default function Test() {
  return (
    <div className="grid grid-cols-1 pt-48">
      <div className="pb-10">
        <p className="text-8xl">ToI</p>
      </div>
      <div className="grid grid-cols-3">
      <a href="/crawl">
        <button>Webcrawling</button>
        </a>
        <p className="px-10"></p>
        <a href="/search">
        <button>Search</button>
        </a>
      </div>
    </div>);
}
