import { useState } from 'react';
import reactLogo from './assets/react.svg';
import viteLogo from '/vite.svg';
import './App.css';
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Test from "./pages/Test2";
import Home from "./pages/Home";
import Search from "./pages/SearchResults";
import Scrape from "./pages/ScrapeResults";

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<Home/>}></Route>
        <Route exact path="/search" element={<Search/>}></Route>
        <Route exact path="/scrape" element={<Scrape/>}></Route>
        <Route exact path="/test" element={<Test/>}></Route>
      </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
