const express = require('express');
const app = express();
const port = 5000;


const books = [
    { id: 1, title: 'Book 1', author: 'Author 1', publishedYear: 2022 },
    { id: 2, title: 'Book 2', author: 'Author 2', publishedYear: 2021 },
];

// parse JSON body 
app.use(express.json());

// Read all books (GET /api/books)
app.get('/api/books', (req, res) => {
    res.json(books);
});

// Read a single book by ID (GET /api/books/:bookId)
app.get('/api/books/:bookId', (req, res) => {
    const bookId = parseInt(req.params.bookId);
    const book = books.find((b) => b.id === bookId);

    if (book) {
        res.json(book);
    } else {
        res.status(404).json({ message: 'Book not found' });
    }
});

// Create a new book (POST /api/books)
app.post('/api/books', (req, res) => {
    const { title, author, publishedYear } = req.body;
    const newBook = {
        id: books.length + 1,
        title,
        author,
        publishedYear,
    };

    books.push(newBook);
    res.status(201).json(newBook);
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
