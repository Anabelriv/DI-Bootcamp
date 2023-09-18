const express = require("express");
const cors = require("cors");

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.listen(3000, () => {
    console.log(`run on port ${3000}`);
});
app.use(cors());

app.get('/api/hello', (req, res) => {
    res.json('Hello from Express')
});
app.post("/api/world", (req, res) => {
    const { input } = req.body;
    const responseMessage = `I received your POST request. This is what you sent me: ${input}`;
    console.log("Request Body:", req.body);
    res.json({ message: responseMessage });
});  
