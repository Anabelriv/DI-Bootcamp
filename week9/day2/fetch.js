
// usersApiModule.js

// Define the function to fetch user data
const usersInfo = async () => {
    const apiUrl = 'https://jsonplaceholder.typicode.com/users';

    try {
        const response = await fetch(apiUrl);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.log(error);
    }
}
module.exports = { usersInfo }