// import { useState, useEffect } from 'react';
import Car from "./components/Car";
import './App.css';

function App() {
  const carinfo = { name: "Ford", model: "Mustang" };

  return (
    <div>
      <h1>Car Information</h1>
      <Car carInfo={carinfo} />
    </div>
  );
}





// const [txt, setTxt] = useState('');

// return (
//   <>
//     <div>
//       <input type='text' onChange={(e) => setTxt(e.target.value)} />
//       <Text txt={txt} />
//     </div>


export default App;

