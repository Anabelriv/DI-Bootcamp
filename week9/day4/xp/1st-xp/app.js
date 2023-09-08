const express = require("express");
const { a_router } = require("./nodejs-server/routes/index.routes.js");
const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use("api/", a_router);

