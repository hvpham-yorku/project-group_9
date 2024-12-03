import React from "react";
import { Link } from "react-router-dom";
import SearchComponent from "../components/SearchComponent";
import AISearchComponent from "../components/AISearchComponent";
import ScrapingComponent from "../components/ScrapingComponent";


// This is the page that currently serves as the frontend for the searching functionality
export default function Test() {
  return (
    <div className="grid grid-cols-1 gap-4">
      <div>
        <p className="text-8xl">ToI</p>
        {/* Below is a react component for searching. */}
        <ScrapingComponent />
      </div>
    </div>);
}
