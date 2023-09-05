// // const http = require('http');

// // const server = http.createServer((req, res) => {
// //     console.log("url=>", req.url);
// //     console.log("headers=>", req.headers);
// //     console.log(('getting your request on my first server'))
// //     if (req, url == '/') {
// //         res.end('<h1>Home</h1>>>');
// //     } else if (req.url == "/about") {
// //         res.end("<h1>About</h1>>");
// //     } else {
// //         res.end("<h1> Page not found</h1>>");
// //     }
// // });

// // server.listen(5000), () => {
// //     console.log("run on port 5000");
// // };

// const express = require('express');
// const dotenv = require('dotenv');
// dotenv.config();
// const app = express();

// const { products } = require('db.js')

// // const PORT = 3001
// app.listen(process.env.PORT, () => {
//     console.log(`run on port ${process.env.PORT}`);
// });
// // CRUD - Read
// app.get('/api/products', (req, res) => {
//     res.json(products);
// });

// // CRUD - One product
// //params
// app.get('/api/products/:id', (req, res) => {
//     const id = req.params.id;
//     const product = products.find((item.id) == id);
//     if (!product) return res.sendStatus(404);//.json({ msg: "Product not found" });
//     res.status(200).json(product);
// });

// // CRUD - query string
// // /api/product?name=ip

// app.get('/api/products/search', (req, res) => {
//     const query = req.query;
//     console.log(query);

//     res.status(200).json({ msg: "ok" });
// });
// // url + search?name=ip&price=800

// app.get("/api/query", (req, res) => {
//     const name = req.query.name.toLowerCase();
//     const products_result = products.filter((product) =>
//         product.name.toLowerCase().includes(name)
//     );

//     if (products_result.length < 1) {
//         return res.status(200).send("No products matched your search");
//     }
//     res.json(products_result);
// });

const express = require("express");
const app = express(); app.use(express.urlencoded({ extended: true }));
app.use(express.json());
const products = require("./data.js");


app.listen(3002, () => {
    console.log("server is listening on port 3002");
});

app.use(express.json()); // parse json body content

// app.post("/api/products", (req, res) => {
//     const newProduct = {
//         id: products.length + 1,
//         name: req.body.name,
//         price: req.body.price,
//     };
//     products.push(newProduct);
//     res.status(201).json(newProduct);
// });

//POST
app.post("/api/products", (req, res) => {
    const { name, price } = req.body;
    const newProduct = {
        id: products.length + 1,
        name,
        price
    }
    products.push(newProduct);
    res.status(201).json(products);
});
//GET
app.get("/api/products", (req, res) => {
    res.json(products);
});
//GET specific product
app.get("/api/products/:productID", (req, res) => {
    const id = Number(req.params.productID);
    const product = products.find((product) => product.id === id);

    if (!product) {
        return res.status(404).send("Product not found");
    }
    res.json(product);
});

app.use(express.json()); // parse json body content

//Update
app.put("/api/products/:productID", (req, res) => {
    const { id } = req.params;
    const { name, price } = req.body;
    const index = products.findIndex((item) => item.id == id);
    products[index] = { ...products[index], name, price };
    res.json(products);
    // if (index === -1) {
    //     return res.status(404).send("Product not found");
    // }
    // const updatedProduct = {
    //     id: products[index].id,
    //     name: req.body.name,
    //     price: req.body.price,
    // };
    // products[index] = updatedProduct;
    // res.status(200).json("Product updated");
});

// app.use(express.json()); // parse json body content

//delete
app.delete("/api/products/:productID", (req, res) => {
    const id = Number(req.params.productID);
    const index = products.findIndex((product) => product.id === id);
    if (index === -1) {
        return res.status(404).send("Product not found");
    }
    products.splice(index, 1);
    res.status(200).json("Product deleted");
});