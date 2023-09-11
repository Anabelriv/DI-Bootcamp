const express = require("express");
// const { logger } = require("../middlewares/utils.js");

const {
    getAllBooks,
    getBookbyID,
    searchBook,
    createBook,
} = require("../controllers/books.controller.js");

const p_router = express.Router();

// CRUD - Read - get all products
p_router.get("/", getAllBooks);

p_router.get("/search", searchBook);

// CRUD - Read - get one products
p_router.get("/:id", getBookbyID);

// body - POST/PUT
p_router.post("/", createBook);


module.exports = { p_router };
