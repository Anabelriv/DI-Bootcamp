// import logo from './logo.svg';
import './App.css';
import UserFavoriteAnimals from "./components/UserFavoriteAnimals";
import Exercise from "./components/Exercise3";
import { v4 as uuidv4 } from "uuid";
function App() {
  const myelementone = <h1>I Love JSX!</h1>
  const myelement = <h1>React is {5 + 5} times better with JSX</h1>;
  const user = {
    firstName: 'Bob',
    lastName: 'Dylan',
    favAnimals: ['Horse', 'Turtle', 'Elephant', 'Monkey']
  };
  return (
    <div className="App">
      <header>
        <p>Hello World!</p>
        {myelementone}
        {myelement}
        <div>
          <h3>{user.firstName}</h3>
          <h3>{user.lastName}</h3>
          <UserFavoriteAnimals favAnimals={user.favAnimals} />
        </div>
        <div>
          <Exercise />
        </div>

      </header>
    </div>
  );
}

export default App;
