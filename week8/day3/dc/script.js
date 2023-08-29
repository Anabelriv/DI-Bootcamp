// Use this Giphy API Random documentation. Use this API Key : hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My
// In the HTML file, add a form, containing an input and a button. This input is used to fetch gif depending on a specific category.
// In the JS file, create a program to fetch one random gif depending on the search of the user (ie. If the search is “sun”, append on the page one gif with a category of “sun”).
// The gif should be appended with a DELETE button next to it. Hint : to find the URL of the gif, look for the sub-object named “images” inside the data you receive from the API.
// Allow the user to delete a specific gif by clicking the DELETE button.
// Allow the user to remove all of the GIFs by clicking a DELETE ALL button.


const apiKey = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My";
const searchForm = document.getElementById("searchForm");
const searchInput = document.getElementById("searchInput");
const gifContainer = document.getElementById("gifContainer");
const deleteAllButton = document.getElementById("deleteAll");

searchForm.addEventListener("submit", async function (event) {
    event.preventDefault();
    const searchTerm = searchInput.value.trim();
    if (searchTerm !== "") {
        const gifData = await fetchRandomGif(searchTerm);
        displayGif(gifData);
    }
});

deleteAllButton.addEventListener("click", function () {
    gifContainer.innerHTML = "";
});

async function fetchRandomGif(searchTerm) {
    const response = await fetch(`https://api.giphy.com/v1/gifs/random?api_key=${apiKey}&tag=${searchTerm}`);
    if (!response.ok) {
        throw new Error("Problem with fetch");
    }
    const data = await response.json();
    return data.data;
}

function displayGif(gifData) {
    const gifUrl = gifData.images.original.url;
    const category = gifData.title || "Unknown";

    const gifDiv = document.createElement("div");
    gifDiv.classList.add("gif");

    const gifImage = document.createElement("img");
    gifImage.src = gifUrl;
    gifDiv.appendChild(gifImage);

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.addEventListener("click", function () {
        gifDiv.remove();
    });
    gifDiv.appendChild(deleteButton);

    const categoryText = document.createElement("p");
    categoryText.textContent = `Category: ${category}`;
    gifDiv.appendChild(categoryText);

    gifContainer.appendChild(gifDiv);
}
