import React from "react";
import ChatBot from "./ChatBot";

function App() {
  return (
    <div
      style={{
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        background: "#eef2ff",
      }}
    >
      <ChatBot />
    </div>
  );
}

export default App;
