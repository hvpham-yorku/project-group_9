import './App.css';
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Home from "./pages/Home";
import Search from "./pages/Search";
import Crawl from "./pages/Crawl";

//This file just sets up the routes for the project.
function App() {

  return (
    <div>
      <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<Home/>}></Route>
        <Route exact path="/search" element={<Search/>}></Route>
        <Route exact path="/crawl" element={<Crawl/>}></Route>
      </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App
