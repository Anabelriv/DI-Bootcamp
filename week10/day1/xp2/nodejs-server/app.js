const express = require("express");
const dotenv = require("dotenv");
// const cors = require("cors");
// const { auth } = require("./middlewares/utils.js");
const { p_router } = require("./routes/books.router.js");
// const { u_router } = require("./routes/users.router.js");

dotenv.config();

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());


app.listen(process.env.PORT, () => {
    console.log(`run on port ${process.env.PORT}`);
});

app.use("/api/books", p_router);

