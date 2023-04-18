import React from "react";
import "../styles/Content.scss";
import instagramlogo from "../imgs/Instagram_icon.webp";
import gmaillogo from "../imgs/gmail_logo.png";
import facebooklogo from "../imgs/facebook_logo.png";
import linkendinlogo from "../imgs/linkedin-logo-linkedin-icon-transparent-free-png.webp";

const ContactUs = () => {
  return (
    <div className="container">
      <div className="contact-us">
        <div>Contact Us</div>{" "}
      </div>
      <div className="content-container">
        <div className="image-container">
          <div>
            <img
              className="link-img"
              src={instagramlogo}
              alt=""
              style={{ width: "275px", height: "150px" }}
            />
          </div>
          <div>
            <img
              className="link-img"
              src={facebooklogo}
              alt=""
              style={{ width: "275px", height: "150px" }}
            />
          </div>
          <div>
            <img
              className="link-img"
              src={gmaillogo}
              alt=""
              style={{ width: "300px", height: "150px" }}
            />
          </div>
        </div>
        
      
      </div>
    </div>
  );
};

export default ContactUs;
