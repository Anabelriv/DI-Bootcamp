const express = require("express");
// const { logger } = require("../middlewares/utils.js");

const {
    getAllPosts,
    getPostbyID,
    searchPost,
    createPost,
    updatePost,
    deletePost
} = require("../controllers/posts.controller.js");

const p_router = express.Router();

// CRUD - Read - get all products
p_router.get("/", getAllPosts);

p_router.get("/search", searchPost);

// CRUD - Read - get one products
p_router.get("/:id", getPostbyID);

// body - POST/PUT
p_router.post("/", createPost);

// CRUD - Update a product - PUT
p_router.put("/:id", updatePost);

// CRUD - Delete a product - DELETE
p_router.delete("/:id", deletePost);

module.exports = { p_router };
