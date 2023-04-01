import React from "react";
import "../styles/Content.scss";

const Home = () => {
  return (
    <div className="container">
      <div className="content">
        <h1>Project Protocol Protocol</h1>
        <h2>Description</h2>
        <blockquote>
          <p>
            A central repository for information about all types of protocols
            from electronics, to networks, and more.
          </p>
        </blockquote>
        <p style={{ paddingTop: 20 }}>
          This site aims to provide descriptions, examples, and instructions of
          how to use a variety of protocols.
        </p>
        <h2>What is a protocol?</h2>
        <p>
          the system of rules and acceptable behavior used at official
          ceremonies and occasions. (
          <a href="https://dictionary.cambridge.org/us/dictionary/english/protocol">
            Cambridge Dictionary 2023
          </a>
          )
        </p>
        <p>
          Informally; protocols are used wherever there needs to be an aggred
          upon form of communcation. Protocols are used in countless areas from
          medicine, politics, conversation, and more. This site is focused on
          all protocols related to computing, such as electrical and networking.
        </p>
        <h2>Thanks</h2>
        <p>
          This project was created out of a desire to contribute to open-source
          projects, as apart of Rensselaer Center for Open Source (
          <a href="https://rcos.io/">RCOS</a>).
        </p>
        <p>
          This project was made possible using Docsify.js, click{" "}
          <a href="https://github.com/docsifyjs/docsify/">here</a>
          to learn more.
        </p>
        <h2>License</h2>
        <p>MIT</p>
      </div>
    </div>
  );
};

export default Home;
