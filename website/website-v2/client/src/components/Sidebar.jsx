import React from "react";
import { Link } from "react-router-dom";
import "../styles/Sidebar.scss";
import github_logo from "../imgs/github_logo.png";
import rcos_logo_red from "../imgs/rcos_logo_red.png";

const Sidebar = () => {
  return (
    <div className="sidebar">
      Sidebar
      <div className="sidebar_content">
        <div className="section">
          <div className="section_title">
            <Link className="link">
              <h3>section_title</h3>
            </Link>
          </div>
          <div className="outer_list">
            <ul>
              <li className="outer_list_item">
                <details>
                  <summary>
                    <Link className="link">Protocol 1</Link>
                  </summary>
                  <ul className="inner_list">
                    <li className="inner_list_item">
                      {" "}
                      <Link className="link"> Description</Link>
                    </li>
                    <li className="inner_list_item">
                      {" "}
                      <Link className="link"> Example</Link>
                    </li>
                  </ul>
                </details>
              </li>
            </ul>
          </div>
        </div>
        <div className="section">
          <div className="section_title">
            <h3>section_title2</h3>
          </div>
          {/* <img src={github_logo} alt="" />
          <img src={rcos_logo_red} alt="" /> */}
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
