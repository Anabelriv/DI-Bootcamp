const express = require('express');
const app = express();
const port = 3000;
const leaderboard = [];
app.use(express.json());

// array of emoji objects
const emojis = [
    { emoji: '😀', name: 'Smile' },
    { emoji: '🐶', name: 'Dog' },
    { emoji: '🌮', name: 'Taco' },
];

let gameState = {
    score: 0,
    currentEmoji: null,
};
// Shuffle the emojis for random selection
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

app.get('/api/game', (req, res) => {
    shuffleArray(emojis);

    const correctEmoji = emojis[0];
    const options = emojis.map((e) => e.name);

    res.json({ emoji: correctEmoji.emoji, options });
});

app.post('/api/guess', (req, res) => {
    const { guess } = req.body;

    if (guess === gameState.currentEmoji.name) {
        gameState.score += 1;
        res.json({ message: 'Correct guess!', score: gameState.score });
    } else {
        res.json({ message: 'Incorrect guess.', score: gameState.score });
    }
});


app.get('/api/leaderboard', (req, res) => {
    const sortedLeaderboard = leaderboard.sort((a, b) => b.score - a.score);
    res.json(sortedLeaderboard);
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
