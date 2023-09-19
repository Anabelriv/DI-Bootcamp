import { useState, createContext } from 'react';
import './App.css';
import Counter from './components/Counter';
import Text from './components/Text';
// use context - state management

// useRef

// useReducer
export const AppContext = createContext();
export const TextContext = createContext();
function App() {
  const [count, setCount] = useState(0)
  const [txt, setTxt] = useState("bla bla bla")
  return (
    <div className="App">
      <h1>Counter</h1>
      {txt}
      <AppContext.Provider value={{ count, setCount, title: 'Zivuch' }}>
        <Counter />
      </AppContext.Provider>
      <TextContext.Provider value={{ setTxt }}>
        <Text />
      </TextContext.Provider>
    </div>
  );
}
// function App() {
//   const [count, setCount] = useState(0)

//   return (
//     <div className="App">
//       <h1>Counter</h1>
//       <Counter count={count} setCount={setCount} />

//     </div>
//   );
// }

export default App;
