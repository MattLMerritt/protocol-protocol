import React from "react";
import "../styles/Content.scss";
import instagramlogo from "../imgs/Instagram_icon.webp";
import gmaillogo from "../imgs/gmail_logo.png";
import facebooklogo from "../imgs/facebook_logo.png";
import linkendinlogo from "../imgs/linkedin-logo-linkedin-icon-transparent-free-png.webp";
import { Link } from "react-router-dom";

const ContactUs = () => {
  return (
    <div className="container">
      <div className="contact-us">
        <div>Contact Us</div>{" "}
      </div>
      <div className="content-container">
        <div className="image-container">
        <Link
        className="link"
        to="https://www.instagram.com/">
          <div>
            <img
              className="link-img"
              src={instagramlogo}
              alt=""
              style={{ width: "275px", height: "150px" }}
            />
          </div>
          </Link>
          <Link 
          className="link"
          to="https://www.facebook.com/home">
          <div>
            <img
              className="link-img"
              src={facebooklogo}
              alt=""
              style={{ width: "275px", height: "150px" }}
            />
          </div>
          </Link>
          <Link
          className="link"
          to="https://www.google.com/gmail/about/">
          <div>
            <img
              className="link-img"
              src={gmaillogo}
              alt=""
              style={{ width: "300px", height: "150px" }}
            />
          </div>
          </Link>
        </div>
        
      
      </div>
    </div>
  );
};

export default ContactUs;
