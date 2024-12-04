import { useState } from 'react';
import './App.css';
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Test from "./pages/Test2";
import Home from "./pages/Home";
import Search from "./pages/Search";
import Crawl from "./pages/Crawl";

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<Home/>}></Route>
        <Route exact path="/search" element={<Search/>}></Route>
        <Route exact path="/crawl" element={<Crawl/>}></Route>
        <Route exact path="/test" element={<Test/>}></Route>
      </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
