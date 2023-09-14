import { useState } from 'react';
import './App.css';

function App() {
  const [inputs, setInput] = useState({
    firstName: '',
    lastName: '',
    age: '',
    gender: '',
    destination: '',
    nutsF: '',
    lactoseF: '',
    Vegan: ''
  });

  const handleChange = (e) => {
    const value = (e.target.type === 'checkbox')
      ? e.target.checked : e.target.value;
    setInput({ ...inputs, [e.target.name]: value })

  };
  // const handleSubmit = (e) => {
  //   // e.preventDefault();
  //   console.log('input>', inputs);
  // }
  const fullname = (`${inputs.firstName} ${inputs.lastName}`)

  return (
    <div className="App">
      <header className="App-header">
        <form>
          First Name:<input name="firstName" onChange={(e) => handleChange(e)} /><br />
          Last Name:<input name="lastName" onChange={(e) => handleChange(e)} /><br />
          Age:<input name="age" onChange={(e) => handleChange(e)} /><br />
          Male:<input type="radio" name="gender" value='Male' onChange={(e) => handleChange(e)} /><br />
          Female:<input type="radio" name="gender" value='Female' onChange={(e) => handleChange(e)} /><br />
          <h5>Select your destination:</h5>
          <select name='destination' onChange={(e) => handleChange(e)}>
            <option value="1">Thailand</option>
            <option value="2">Japan</option>
            <option value="3">Brazil</option>
          </select><br />
          <h5>Your dietary restriction:</h5>
          Nuts Free:<input type="checkbox" name="nutsF" onChange={(e) => handleChange(e)} /><br />
          Lactose Free:<input type="checkbox" name="lactoseF" onChange={(e) => handleChange(e)} /><br />
          Vegan:<input type="checkbox" name="vegan" onChange={(e) => handleChange(e)} /><br />

          <input type='submit' />
        </form>

        <div>
          <h2>Entered Information</h2>
          <div>
            <p>Full name: {fullname}</p>
            <p>Age: {inputs.age}</p>
            <p>Gender: {inputs.gender}</p>
            <p>Your Destination: {inputs.destination}</p>
            <h4>Dietary Restrictions:</h4>
            <p>Nuts Free:{inputs.nutsF ? 'Yes' : 'No'}</p>
            <p>Lactose Free:{inputs.lactoseF ? 'Yes' : 'No'}</p>
            <p>Vegan:{inputs.vegan ? 'Yes' : 'No'}</p>

          </div>
        </div>
      </header>
    </div>
  );
}

export default App;
