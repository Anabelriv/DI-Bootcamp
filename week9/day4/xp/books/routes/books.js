const express = require('express');
const router = express.Router();

const books = [];

// all books
router.get('/', (req, res) => {
    res.json(books);
});

// add a new book 
router.post('/', (req, res) => {
    const { title, author } = req.body;
    if (!title || !author) {
        return res.status(400).json({ error: 'Title and author are required' });
    }

    const newBook = {
        id: books.length + 1,
        title,
        author,
    };

    books.push(newBook);
    res.status(201).json(newBook);
});

// Update a book by ID
router.put('/:id', (req, res) => {
    const bookId = parseInt(req.params.id);
    const { title, author } = req.body;

    const bookToUpdate = books.find((book) => book.id === bookId);

    if (!bookToUpdate) {
        return res.status(404).json({ error: 'Book not found' });
    }

    if (title !== undefined) {
        bookToUpdate.title = title;
    }

    if (author !== undefined) {
        bookToUpdate.author = author;
    }

    res.json(bookToUpdate);
});

// Delete a book by ID
router.delete('/:id', (req, res) => {
    const bookId = parseInt(req.params.id);
    const bookIndex = books.findIndex((book) => book.id === bookId);

    if (bookIndex === -1) {
        return res.status(404).json({ error: 'Book not found' });
    }

    books.splice(bookIndex, 1);
    res.json({ message: 'Book deleted' });
});

module.exports = router;