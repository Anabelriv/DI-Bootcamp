import React, { useState, useEffect } from 'react';
import superheroesData from '../Heroes.json';
import '../App.css';

function CardGame() {
    const [superheroes, setSuperheroes] = useState(superheroesData.superheroes);
    const [currentScore, setCurrentScore] = useState(0);
    const [topScore, setTopScore] = useState(0);
    const [clickedSuperheroIds, setClickedSuperheroIds] = useState([]);

    useEffect(() => {
        shuffleSuperheroes();
    }, []);

    const shuffleSuperheroes = () => {
        const shuffledSuperheroes = [...superheroes].sort(() => Math.random() - 0.5);
        setSuperheroes(shuffledSuperheroes);
    };

    const handleSuperheroClick = (superheroId) => {
        if (clickedSuperheroIds.includes(superheroId)) {
            // User clicked on the same superhero twice, reset the score
            setCurrentScore(0);
            setClickedSuperheroIds([]); // Reset the clicked superhero IDs
        } else {
            // User clicked on a new superhero, update the score
            setCurrentScore(currentScore + 1);

            // Update the top score if the current score surpasses it
            if (currentScore + 1 >= topScore) {
                setTopScore(currentScore + 1);
            }

            setClickedSuperheroIds([...clickedSuperheroIds, superheroId]); // Add the clicked superhero ID
        }

        // Shuffle the superheroes after each click
        shuffleSuperheroes();
        console.log(clickedSuperheroIds)
    };

    return (
        <div className="App">
            <header className="App-header">
                <Navbar currentScore={currentScore} topScore={topScore} />
                <div className="superhero-container">
                    {superheroes.map((superhero) => (
                        <Superhero
                            key={superhero.id}
                            id={superhero.id}
                            name={superhero.name}
                            image={superhero.image}
                            onClick={handleSuperheroClick}
                        />
                    ))}
                </div>
            </header >
        </div >
    );
}

function Navbar({ currentScore, topScore }) {
    return (
        <nav>

            <div className="scores">
                <p>Superheroes Memory Game</p>
                <div className="score">
                    Current Score: {currentScore}
                </div>
                <div className="score">
                    Top Score: {topScore}
                </div>
            </div>
            <div class="intro">Get points by clicking on an image but don't click on any more than once!</div>
        </nav>
    );
}

function Superhero({ id, name, image, onClick }) {
    return (
        <div className="superhero" onClick={() => onClick(id)}>
            <img src={image} alt={name} id='image' />
            <p className='namehero'>{name}</p>
        </div>
    );
}

export default CardGame;
