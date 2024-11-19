import React from "react";
export default function Profile6x6({ header = "Result header", body = "Result body" }) {
  return (
    <div className="pt-10">
      <p className="text-5xl">{ header }</p>
      <p>{ body }</p>
    </div>
  );
}