import React from "react";
import { Link } from "react-router-dom";

export default function Test() {
  return (
    <div className="grid grid-cols-1 gap-4">
      <div>
        <p className="text-8xl">ToI</p>
        <input type="text" placeholder="Please type your search here" className=""/>
      </div>
      <a href="/search">
        <button>Traditional Search</button>
      </a>
      <b href="/scrape">
        <button>Webscraping</button>
      </b>
    </div>);
}
