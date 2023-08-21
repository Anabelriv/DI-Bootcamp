// Array of planets with their moons
const planets = [
    { name: "Mercury", moons: 0 },
    { name: "Venus", moons: 0 },
    { name: "Earth", moons: 1 },
    { name: "Mars", moons: 2 },
    { name: "Jupiter", moons: 79 },
    { name: "Saturn", moons: 83 },
    { name: "Uranus", moons: 27 },
    { name: "Neptune", moons: 14 }
];

// Function to create a planet div
function createPlanetDiv(planetName, moonCount) {
    const planetDiv = document.createElement('div');
    planetDiv.className = 'planet';

    // Set background color based on planet name
    planetDiv.style.backgroundColor = getRandomColor();

    // Create moons for the planet
    for (let i = 0; i < moonCount; i++) {
        const moonDiv = document.createElement('div');
        moonDiv.className = 'moon';
        moonDiv.style.left = `${i * 40}px`; // Position moons around the planet
        planetDiv.appendChild(moonDiv);
    }

    // Append planet div to the section
    const listPlanetsSection = document.querySelector('.listPlanets');
    listPlanetsSection.appendChild(planetDiv);
}

// Function to generate a random color
function getRandomColor() {
    const letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

// Loop through planets and create divs for each planet
planets.forEach(planet => {
    createPlanetDiv(planet.name, planet.moons);
});
