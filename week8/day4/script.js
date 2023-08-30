console.log('ver 2.3 ajax');

// Select elements in DOM
const button = document.querySelector('#button');
const names = document.querySelector('#name');
const height = document.querySelector('#height');
const gender = document.querySelector('#gender');
const birthYear = document.querySelector('#birth-year');
const homeWorld = document.querySelector('#home-world');

// Get the info from API and catch for Errors
button.addEventListener('click', async () => {
    try {
        // Call Loading Data
        updateWithLoading();

        // Get Random people in the API between 1 and 88
        let randomNumber = Math.floor((Math.random() * 88) + 1);
        let apiUrl = 'https://swapi.dev/api/people/' + randomNumber + '/';

        const response = await fetch(apiUrl);

        if (!response.ok) {
            throw new Error(`Error: ${response.status}: ${response.statusText}`);
        }

        const data = await response.json();
        updateInfo(data);
    } catch (error) {
        console.error('There was an error:', error);
        updateInfoWithError();
    }
});

// Display info on screen
async function updateInfo(resp) {
    try {
        if (resp.homeworld === 'unknown') {
            homeWorld.innerText = 'Home World: There is no homeworld';
        } else {
            const url = new URL(resp.homeworld);
            url.protocol = 'https:';
            const response = await fetch(url.href);

            if (!response.ok) {
                throw new Error(`Error: ${response.status}: ${response.statusText}`);
            }

            const data = await response.json();
            // updateInfo(data);
            homeWorld.innerText = `Home World: ${data.name}`;
        }

        names.innerText = resp.name;
        height.innerText = `Height: ${resp.height}`;
        gender.innerText = `Gender: ${resp.gender}`;
        birthYear.innerText = `Birth Year: ${resp.birth_year}`;
    } catch (error) {
        console.error('There was an error:', error);
        updateInfoWithError();
    }
}

// Display when Error
function updateInfoWithError() {
    names.innerText = 'Oh No! That person isnt available.';
    height.innerText = '';
    gender.innerText = '';
    birthYear.innerText = '';
    homeWorld.innerText = '';
}

// Display when updating info (pending data)
function updateWithLoading() {
    names.innerHTML = '<i class="fa fa-spinner fa-pulse fa-3x fa-fw"></i> <p>Loading...</p>';
    height.innerText = '';
    gender.innerText = '';
    birthYear.innerText = '';
    homeWorld.innerText = '';
}
