import { useState, useRef, useEffect } from 'react';
import './App.css';
// use context - state management

// useRef

// useReducer

function App() {
  const [count, setCount] = useState(0)

  const inputRef = useRef(null);
  const inputEmailRef = useRef(null);
  // const txtRef = useRef(null);

  const txt = useRef('');
  let txtOne = 'text One';
  useEffect(() => {
    console.log(inputRef);
    inputRef.current.value = 'Enter Text';

  }, []);

  const handleClick = (() => {
    inputRef.current.focus();
    console.log(inputEmailRef.current.value);
    txt.current = txt.current + "0";
    txtOne = 'textTwo';
    console.log(txt.current, txtOne);
  })

  const reRender = (() => {
    setCount(count + 1);
  })

  return (
    <div className="App">
      <h1>useRef</h1>
      <h4>{txt.current}</h4>
      <h4>{txtOne}</h4>
      <input ref={inputRef} />
      <input type='email' ref={inputEmailRef} />
      <button onClick={handleClick}>Input Focus</button>
      <button onClick={reRender}>Rerender</button>

    </div>
  );
}

export default App;
