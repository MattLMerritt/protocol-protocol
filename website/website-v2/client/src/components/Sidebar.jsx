import React from "react";
import { Link } from "react-router-dom";
import "../styles/Sidebar.scss";
import github_logo from "../imgs/github_logo.png";
import rcos_logo_red from "../imgs/rcos_logo_red.png";
import { HashLink } from "react-router-hash-link";

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
                    <Link className="link" to="/Uart">
                      UART
                    </Link>
                  </summary>
                  <ul className="inner_list">
                    <li className="inner_list_item">
                      {" "}
                      <HashLink className="link" to="/Uart/#description">
                        {" "}
                        Description
                      </HashLink>
                    </li>
                    <li className="inner_list_item">
                      {" "}
                      <HashLink className="link" to="/Uart/#examples">
                        {" "}
                        Examples
                      </HashLink>
                    </li>
                    <li className="inner_list_item">
                      {" "}
                      <HashLink className="link" to="/Uart/#instructions">
                        {" "}
                        Instructions
                      </HashLink>
                    </li>
                  </ul>
                </details>
              </li>
              <li className="outer_list_item">
                <details>
                  <summary>
                    <Link className="link">Protocol 2</Link>
                  </summary>
                  <ul className="inner_list">
                    <li className="inner_list_item">
                      {" "}
                      <HashLink className="link"> inner_list_item</HashLink>
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
            }}
          >
            Share
          </div>
          <Link
            className="link"
            to="https://github.com/MattLMerritt/protocol-protocol"
          >
            <img
              src={github_logo}
              alt=""
              style={{ width: "45px", height: "auto", marginRight: "10px" }}
            />
          </Link>
          <Link className="link" to="https://rcos.io/">
            <img
              src={rcos_logo_red}
              alt=""
              style={{ width: "100px", height: "auto", marginLeft: "10px" }}
            />
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Sidebar;
