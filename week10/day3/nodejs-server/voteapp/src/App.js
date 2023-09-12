import { useState } from 'react';
import './App.css';

function App() {
  const [languages, setLanguages] = useState([
    { name: "Php", votes: 0 },
    { name: "Python", votes: 0 },
    { name: "JavaSript", votes: 0 },
    { name: "Java", votes: 0 }
  ])
  const changeVotes = (languageIndex) => {
    const updatedLanguages = languages.map((lang, index) => {
      if (index === languageIndex) {
        return { ...lang, votes: lang.votes + 1 };
      } else {
        return lang;
      };
    });
    setLanguages(updatedLanguages);
  };


  return (
    <div>
      <h1>Vote Your Language!</h1>
      <ul>
        {languages.map((language, index) => (
          <li key={index}>
            {language.name}: {language.votes} votes
            <button onClick={() => changeVotes(index)}>Click Here!</button>
          </li>
        ))}
      </ul>
    </div>

  );
};

export default App;
