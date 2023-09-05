const express = require('express');
const app = express();
const port = 5000;
const fetchPosts = require('./data/dataService');


app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});


app.get('/api/posts', async (req, res) => {
    try {
        const posts = await fetchPosts();
        res.json(posts);
        console.log('Data has been successfully retrieved and sent.');
    } catch (error) {
        console.error('Error fetching data:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});
