const { books } = require("../config/db.js");
const { _getAllBooks, _getBookbyId, _searchBook, _createBook } = require("../models/books.model.js");


const getAllBooks = (req, res) => {
    _getAllBooks()
        .then(data => {
            res.json(data)
        })
        .catch(err => {
            console.log(err)
            res.status(404).json({ msg: 'not found' });
        })
};

const searchBook = async (req, res) => {
    try {
        const data = await _searchBook(req.query.name)
        res.json(data);

    } catch (err) {
        console.log(error);
        res.status(404).json({ msg: 'not found' })
    }
};

const getBookbyID = async (req, res) => {
    try {
        const id = req.params.id;
        const data = await _getBookbyId(id);
        res.json(data)
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: 'no book found' })
    }
}

const createBook = async (req, res) => {
    const { title, author, publishedyear } = req.body;
    try {
        const data = await _createBook(req.body);
        res.json(data)
    } catch (err) {
        console.log(err)
        res.status(404).json({ msg: "book not found" })
    }
};


module.exports = {
    getAllBooks,
    getBookbyID,
    searchBook,
    createBook
};
