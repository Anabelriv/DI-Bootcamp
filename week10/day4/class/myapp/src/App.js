// import { useState } from 'react';
import './App.css';
import ErrorBoundary from './ErrorBoundary';
// import Parent from "./component/Parent";
// import Child from "./component/Child";
import Counter from './component/Counter';

function App() {
  return <>
    {/* <Parent user="admin">
      <Child />
    </Parent> */}
    <ErrorBoundary>
      <Counter />
    </ErrorBoundary>
    <Counter />
    <h1>Something</h1>
  </>

}


export default App;



// function App() {
//   const [email, setEmail] = useState("");
//   const [password, setPassword] = useState("");
//   const [inputs, setInput] = useState({
//     email: '',
//     password: '',
//     yesno: '',
//     color: '',
//   });

//   const handleInputs = (e) => {
//     const value = (e.target.type === 'checkbox')
//       ? e.target.checked : e.target.value;
//     setInput({ ...inputs, [e.target.name]: value })
//   };
//   const handleSubmit = (e) => {
//     e.preventDefault();
//     console.log('input>', inputs);
//   }
//   return (
//     <div className="App">
//       <header className="App-header">
//         <form onSubmit={handleSubmit}>
//           Email:<input name="email" onChange={(e) => handleInputs(e)} /><br />
//           Password:<input name="pass" onChange={(e) => handleInputs(e)} /><br />

//           Yes/No:<input type="checkbox" name="yesno" onChange={(e) => handleInputs(e)} /><br />
//           <select name='color' onChange={(e) => handleInputs(e)}>
//             <option value="1">Red</option>
//             <option value="2">Yellow</option>
//             <option value="3">Blue</option>

//           </select><br />
//           <input type='submit' value='Submit' />
//         </form>

//       </header>
//     </div>
//   );
// }

