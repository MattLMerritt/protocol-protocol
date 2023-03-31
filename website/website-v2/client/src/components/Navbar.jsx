import React from "react";
import {useRef} from "react"
import {FaBars, FaTimes} from "react-icons/fa"
import protlogo from "../imgs/protlogo.png";
import "../styles/Navbar.css"

function Navbar () {


  const navRef = useRef();

  const showNavBar = () =>  {
    navRef.current.classList.toggle("responsive_nav");
  }

  return( 
    <header>
       <h3>
        <img src={protlogo} alt="" style={{ width: '100px', height: '110px' }} />
      </h3>
      <nav ref={navRef}>
        <a href="/#">Contact Us</a>
        <a href="/#">About</a>
        <a href="/#">Simulation</a>
        <button className = "nav-btn nav-close-btn" onClick={showNavBar}>
          <FaTimes/>
        </button>
      </nav>
      <button className = "nav-btn" onClick={showNavBar}>
        <FaBars/>
      </button>
    </header>
  );
  
};

export default Navbar;
