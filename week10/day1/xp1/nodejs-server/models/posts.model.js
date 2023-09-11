const { db } = require("../config/db.js");

const _getAllPosts = () => {
    return db('posts')
        .select('id', 'title', 'content')
        .orderBy('title');
}

const _getPostbyId = (id) => {
    return db('posts')
        .select('id', 'title', 'content')
        .where({ id });
}


const _searchPost = (title) => {
    return db('posts')
        .select('id', 'title', 'content')
        .whereILike('title', `%${title}%`);
}

const _createPost = ({ title, content }) => {
    return db('posts')
        .insert({ title, content }, ['id', 'title', 'content']);
}

const _updatePost = ({ title, content }) => {
    return db("posts")
        .update({ title, content })
        .where({ id })
        .returning(['id', 'title', 'content']);
};

const _deletePosts = (id) => {
    return db('posts')
        .where({ id })
        .del()
        .returning(['id', 'title', 'content']);
}

module.exports = {
    _getAllPosts, _getPostbyId, _searchPost, _createPost, _updatePost, _deletePosts
}