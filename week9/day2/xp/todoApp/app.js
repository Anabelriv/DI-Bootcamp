import TodoList from './todo.js';

// Create an instance of the TodoList class
const myTodoList = new TodoList();

// Add tasks to the todo list
myTodoList.addTask("Buy groceries");
myTodoList.addTask("Finish homework");
myTodoList.addTask("Go for a run");

// Mark some tasks as complete
myTodoList.markTaskAsComplete(0);
myTodoList.markTaskAsComplete(2);

// List all tasks
const tasks = myTodoList.listTasks();

// Display the tasks
console.log("All tasks:");
tasks.forEach((task, index) => {
    console.log(`${index + 1}. ${task.completed ? '[X]' : '[ ]'} ${task.task}`);
});
