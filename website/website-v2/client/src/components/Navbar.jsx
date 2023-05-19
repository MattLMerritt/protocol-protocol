import React from "react";
import { Link } from "react-router-dom";
import { useRef } from "react";
import { FaBars, FaTimes } from "react-icons/fa";
import protlogo from "../imgs/protlogo_white.png";
import "../styles/Navbar.css";

function Navbar() {
  const navRef = useRef();

  const showNavBar = () => {
    navRef.current.classList.toggle("responsive_nav");
  };

  return (
    <header>
      <Link className="link" to="/">
        <h3>
          <img src={protlogo} alt="" style={{ width: "auto", height: "5em" }} />
        </h3>
      </Link>
      <nav ref={navRef}>
        <a href="/contact-us">
          Contact Us
        </a>
        <a href="/#">About</a>
        <a href="/Simulation">
          Simulation
        </a>
        <button className="nav-btn nav-close-btn" onClick={showNavBar}>
          <FaTimes />
        </button>
      </nav>
      <button className="nav-btn" onClick={showNavBar}>
        <FaBars />
      </button>
    </header>
  );
}

export default Navbar;
