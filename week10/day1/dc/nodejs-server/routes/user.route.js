const express = require('express');
const router = express.Router();
const userController = require('../controllers/user.controller.js');

// Registration route
router.post('/register', userController.register);

// Login route
router.post('/login', userController.login);

// Get all users
router.get('/users', userController.getAllUsers);

// Get a specific user by ID
router.get('/users/:id', userController.getUserById);

// Update a user by ID
router.put('/users/:id', userController.updateUser);

module.exports = router;


// const express = require("express");
// // const { logger } = require("../middlewares/utils.js");

// const {
//     getAllPosts,
//     getPostbyID,
//     searchPost,
//     createPost,
//     updatePost,
//     deletePost
// } = require("../controllers/user.controller.js");

// const p_router = express.Router();

// // CRUD - Read - get all products
// p_router.get("/", getAllPosts);

// p_router.get("/search", searchPost);

// // CRUD - Read - get one products
// p_router.get("/:id", getPostbyID);

// // body - POST/PUT
// p_router.post("/", createPost);

// // CRUD - Update a product - PUT
// p_router.put("/:id", updatePost);

// // CRUD - Delete a product - DELETE
// p_router.delete("/:id", deletePost);

// module.exports = { p_router };
