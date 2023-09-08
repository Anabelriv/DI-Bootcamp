const express = require('express');
const dotenv = require("dotenv");
const app = express();
const todosRouter = require('./routes/todos');
app.use(express.json());

app.use('/todos', todosRouter);


dotenv.config();

app.listen(process.env.PORT, () => {
    console.log(`run on port ${process.env.PORT}`);
});



