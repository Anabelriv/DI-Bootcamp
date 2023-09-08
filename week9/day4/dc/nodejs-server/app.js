const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

const quizRoutes = require('./routes/quizRoutes.js');

app.use('/quiz', quizRoutes);

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
