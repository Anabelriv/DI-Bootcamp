const { getAbout, getHome } = require('../controllers/about.js');
const express = require('express');
const a_router = express.Router();

a_router.get('/about', getAbout);
a_router.get('/', getHome);
module.exports = { a_router };