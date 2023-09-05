const express = require('express')
const app = express()
app.use(express.json());
app.listen(5000, () => {
    console.log('server is listening on port 5000')
})

const data = [
    {
        id: 1,
        title: 'First Blog Post',
        content: 'This is the content of the first blog post.',
    },
    {
        id: 2,
        title: 'Second Blog Post',
        content: 'This is the content of the second blog post.',
    },
    {
        id: 3,
        title: 'Third Blog Post',
        content: 'This is the content of the third blog post.',
    },
];


//   module.exports = data;

// GET /posts: Return a list of all blog posts.
app.get("/api/posts", (req, res) => {
    res.json(data);
})
// GET /posts/:id: Return a specific blog post based on its id.
app.get("/api/posts/:postId", (req, res) => {
    const id = Number(req.params.postId);
    const post = data.find((post) => post.id === id)
    if (!post) {
        return res.status(404).send("post not found");
    }
    res.json(post);
});
// POST /posts: Create a new blog post.

app.post("/api/posts", (req, res) => {
    const { title, content } = req.body;
    const newPost = {
        id: posts.length + 1,
        title,
        content
    };
    data.push(newPost);
    res.status(201).json(newPost);
});
// PUT /posts/:id: Update an existing blog post.
app.put("api/posts/:postId", (req, res) => {
    const id = Number(req.params.postID);
    // const { title, content } = req.body;
    const index = data.findIndex((post) => post.id === id);
    if (index === -1) {
        return res.status(404).send("Post not found");
    }
    const updatedPost = {
        id: data[index].id,
        title: req.body.title,
        content: req.body.content,
    };
    data[index] = updatedPost;
    res.status(200).json("Post updated");
});
// DELETE /posts/:id: Delete a blog post.
app.delete("api/posts/:postId", (req, res) => {
    const id = Number(req.params.postId);
    const index = data.findIndex((post) => post.id === id);
    if (index === -1) {
        return res.status(404).send("Post not found");
    }
    data.splice(index, 1);
    res.status(200).json("Post deleted");
});
