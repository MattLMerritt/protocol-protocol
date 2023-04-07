import React from "react";
import { Link } from "react-router-dom";
import "../styles/Content.scss";
import linkedinlogo from "../imgs/linkedin-logo-linkedin-icon-transparent-free-png.webp";


const ContactUs = () => {
  return (
    <div className="container">
      <div className="contact-us">
        <div>Contact Us</div>{" "}
      </div>
    <div className="content-container">
      <div className="text-container">
            <p className="contact-info">
              Member 1 contact info:
            </p>
        </div>
        <div className="image-container">
          <Link
            className="link"
            to="https://www.linkedin.com/in/akhil-munipalli-11a5a9255/"
          >
          <img
            classname="link-img"
            src={linkedinlogo}
            alt=""
            style={{ width: "50px", height: "70px" }}
          />
          </Link>
        </div>
      
    </div>
  </div>
  );
};

export default ContactUs;
