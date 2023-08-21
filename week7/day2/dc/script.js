document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('libform');
    const storyElement = document.getElementById('story');
    const libButton = document.getElementById('lib-button');

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        const noun = document.getElementById('noun').value.trim();
        const adjective = document.getElementById('adjective').value.trim();
        const person = document.getElementById('person').value.trim();
        const verb = document.getElementById('verb').value.trim();
        const place = document.getElementById('place').value.trim();

        if (noun !== '' && adjective !== '' && person !== '' && verb !== '' && place !== '') {
            const story = generateStory(noun, adjective, person, verb, place);
            storyElement.textContent = story;
        }
    });

    libButton.addEventListener('click', function () {
        const currentStory = storyElement.textContent;
        if (currentStory) {
            const stories = [
                "Once upon a time, there was a [adjective] [noun] named [person] who loved to [verb] in [place].",
                "In a faraway [place], a [adjective] [noun] named [person] discovered their love for [verb].",
                "[person] always dreamed of visiting [place] and [verb] with their favorite [noun]."
            ];
            const newStory = getRandomStory(stories, currentStory);
            storyElement.textContent = newStory;
        }
    });
});

function generateStory(noun, adjective, person, verb, place) {
    const story = `Once upon a time, there was a ${adjective} ${noun} named ${person} who loved to ${verb} in ${place}.`;
    return story;
}

function getRandomStory(stories, currentStory) {
    let newStory = currentStory;
    while (newStory === currentStory) {
        newStory = stories[Math.floor(Math.random() * stories.length)];
    }
    return newStory;
}
