import React, { useRef, useState } from "react";
import "./App.css";

function CharacterCounter() {
  const inputRef = useRef(null);
  const [charCount, setCharCount] = useState(0);

  const handleInputChange = () => {
    const textLength = inputRef.current.value.length;
    setCharCount(textLength)
  };

  return (
    <div>
      <h1>Character Counter</h1>
      <textarea
        ref={inputRef}
        onChange={handleInputChange}
        placeholder="Type something..."></textarea>
      <p>Character Count: {charCount}</p>
    </div>
  );
}

function AppTwo() {
  return (
    <div className="App">
      <CharacterCounter />
    </div>
  );
}

export default AppTwo;