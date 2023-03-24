import React from "react";
import { Link } from "react-router-dom";
import "../styles/Sidebar.scss";
import github_logo from "../imgs/github_logo.png";
import rcos_logo_red from "../imgs/rcos_logo_red.png";

const Sidebar = () => {
  return (
    <div className="sidebar">
      <div className="sidebar_content">
        <div className="section">
          <div className="section_title">
            <Link className="link">
              <h3>Protocol Navigation</h3>
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
        <div className="section share">
          <div
            className="section_title"
            style={{
              color: "#908e8d",
              fontWeight: 500,
              margin: "0 0 12px",
              paddingLeft: 20,
            }}
          >
            Share
          </div>
          <Link
            className="link"
            to="https://github.com/MattLMerritt/protocol-protocol"
          >
            <img src={github_logo} alt="" />
          </Link>
          <Link className="link" to="https://rcos.io/">
            <img src={rcos_logo_red} alt="" />
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
