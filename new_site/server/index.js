// server/index.js

const express = require("express");

const PORT = process.env.PORT || 3001;

const app = express();


// create get requets handling
app.get("/api", (req, res) => {
  res.json({ message: "Hello from server!" });
});

// listen on port
app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
});