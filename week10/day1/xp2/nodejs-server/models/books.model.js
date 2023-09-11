const { db } = require("../config/db.js");

const _getAllBooks = () => {
    return db('books')

        .select('id', 'title', 'author', 'publishedyear')
        .orderBy('title');
}

const _getBookbyId = (id) => {
    return db('books')
        .select('id', 'title', 'author', 'publishedyear')
        .where({ id });
}


const _searchBook = (title) => {
    return db('books')
        .select('id', 'title', 'author', 'publishedyear')
        .whereILike('title', `%${title}%`);
}

const _createBook = ({ title, author, publishedyear }) => {
    return db('books')
        .insert({ title, author, publishedyear }, ['id', 'title', 'author', 'publishedyear']);
}


module.exports = {
    _getAllBooks, _getBookbyId, _searchBook, _createBook
}