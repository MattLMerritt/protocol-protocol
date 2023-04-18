import React from "react";
import "../styles/Content.scss";

const Home = () => {
  return (
    <div className="container">
      <div className="content">
        <h1 className="header-size">Project Protocol Protocol</h1>
        <h2 className="subheader-size">Description</h2>
        <blockquote>
          <p className="text-block">
            A central repository for information about all types of protocols
            from electronics, to networks, and more.
          </p>
        </blockquote>
        <p className="text-block" style={{ paddingTop: 15 }}>
          This site aims to provide descriptions, examples, and instructions of
          how to use a variety of protocols.
        </p>
        <h2 className="subheader-size">What is a protocol?</h2>
        <p className="text-block">
          the system of rules and acceptable behavior used at official
          ceremonies and occasions. (
          <a href="https://dictionary.cambridge.org/us/dictionary/english/protocol">
            Cambridge Dictionary 2023
          </a>
          )
        </p>
        <p className="text-block">
          Informally; protocols are used wherever there needs to be an aggred
          upon form of communcation. Protocols are used in countless areas from
          medicine, politics, conversation, and more. This site is focused on
          all protocols related to computing, such as electrical and networking.
        </p>
        <h2 className="subheader-size">Thanks</h2>
        <p className="text-block">
          This project was created out of a desire to contribute to open-source
          projects, as apart of Rensselaer Center for Open Source (
          <a href="https://rcos.io/">RCOS</a>).
        </p>
        <h2 className="subheader-size">License</h2>
        <p className="text-block">MIT</p>
      </div>
    </div>
  );
};

export default Home;
