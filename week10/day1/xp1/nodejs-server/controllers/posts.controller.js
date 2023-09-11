const { posts } = require("../config/db.js");
const { _getAllPosts, _getPostbyId, _searchPost, _createPost, _updatePost, _deletePost } = require("../models/posts.model.js");


const getAllPosts = (req, res) => {
    _getAllPosts()
        .then(data => {
            res.json(data)
        })
        .catch(err => {
            console.log(err)
            res.status(404).json({ msg: 'not found' });
        })
};


const searchPost = async (req, res) => {
    try {
        const data = await _searchPost(req.query.name)
        res.json(data);

    } catch (err) {
        console.log(error);
        res.status(404).json({ msg: 'not found' })
    }
};

const getPostbyID = async (req, res) => {
    try {
        const id = req.params.id;
        const data = await _getPostbyId(id);
        res.json(data)
    } catch (error) {
        console.log(error);
        res.status(404).json({ msg: 'no post found' })
    }
}

const createPost = async (req, res) => {
    const { title, content } = req.body;
    try {
        const data = await _createPost(req.body);
        res.json(data)
    } catch (err) {
        console.log(err)
        res.status(404).json({ msg: "post not found" })
    }
};

const updatePost = async (req, res) => {
    const { id } = req.params;
    const { title, content } = req.body;
    try {
        const data = await _updatePost(req.body, id);
        res.json(data);
    } catch (err) {
        console.log(err)
        res.status(404).json({ msg: "not found" })
    }

};


const deletePost = async (req, res) => {
    const { id } = req.params;

    try {
        const data = await _deletePost(id);
        res.json(data);
    } catch (err) {
        console.log(err)
        res.status(404).json({ msg: "not found" })
    }
};

module.exports = {
    getAllPosts,
    getPostbyID,
    searchPost,
    createPost,
    updatePost,
    deletePost
};
