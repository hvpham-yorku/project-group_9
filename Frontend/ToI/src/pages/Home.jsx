import React from "react";
import { Link } from "react-router-dom";
import SearchComponent from "../components/SearchComponent";

export default function Test() {
  return (
    <div className="grid grid-cols-1 gap-4">
      <div>
        <p className="text-8xl">ToI</p>
        <SearchComponent />
      </div>
      {/* <a href="/search">
        <button>Traditional Search</button>
      </a>
      <b href="/scrape">
        <button>Webscraping</button>
      </b> */}
    </div>);
}
