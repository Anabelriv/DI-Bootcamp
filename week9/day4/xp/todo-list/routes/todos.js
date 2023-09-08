const express = require('express');
const router = express.Router();

const todos = [];

router.get('/', (req, res) => {
    res.json(todos);
});

// Add a new to-do item
router.post('/', (req, res) => {
    const { task } = req.body;
    if (!task) {
        return res.status(400).json({ error: 'Task is required' });
    }

    const newTodo = {
        id: todos.length + 1,
        task,
        completed: false,
    };

    todos.push(newTodo);
    res.status(201).json(newTodo);
});

// Update a to-do item by ID
router.put('/:id', (req, res) => {
    const todoId = parseInt(req.params.id);
    const { task, completed } = req.body;

    const todoToUpdate = todos.find((todo) => todo.id === todoId);

    if (!todoToUpdate) {
        return res.status(404).json({ error: 'To-do item not found' });
    }

    if (task !== undefined) {
        todoToUpdate.task = task;
    }

    if (completed !== undefined) {
        todoToUpdate.completed = completed;
    }

    res.json(todoToUpdate);
});

// Delete a to-do item by ID
router.delete('/:id', (req, res) => {
    const todoId = parseInt(req.params.id);
    const todoIndex = todos.findIndex((todo) => todo.id === todoId);

    if (todoIndex === -1) {
        return res.status(404).json({ error: 'To-do item not found' });
    }

    todos.splice(todoIndex, 1);
    res.json({ message: 'To-do item deleted' });
});

module.exports = router;
