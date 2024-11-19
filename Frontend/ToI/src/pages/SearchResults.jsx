import React from "react";
import ResultComponent from "../components/ResultComponent";

export default function Search() {
  return (
    <div>
      <div className="w-[350px] grid grid-cols-2">
        <p className="text-8xl">ToI</p>
        <input className="w-[350px]" type="text" placeholder="Please enter your search here" />
        <p>Traditional Search</p>        
      </div>
      <div style={{ textAlign: 'left' }}>
        <ResultComponent user="This is a name that I have put"></ResultComponent>
      </div>
    </div>);
}
