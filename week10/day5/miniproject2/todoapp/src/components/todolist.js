import { useState } from 'react';
function Todo() {
    const [tasks, setTasks] = useState([]);
    const [newTask, setNewTask] = useState([]);

    const addTask = () => {
        if (newTask.trim() !== '') {
            const newTaskObject = {
                id: Date.now(),
                text: newTask,
                completed: false,
            };
            setTasks([...tasks, newTaskObject]);
            setNewTask('');
        }
    };
    const toggleTaskCompletion = (taskId) => {
        const updatedTasks = tasks.map((task) => {
            if (task.id === taskId) {
                return { ...task, completed: !task.completed };
            }
            return task;
        });
        setTasks(updatedTasks);
    };

    const deleteTask = (taskId) => {
        const updatedTasks = tasks.filter((task) => task.id !== taskId);
        setTasks(updatedTasks);
    };


    return (
        <div>
            <h1 className="text-2xl">To Do's</h1>
            <input
                type="text"
                placeholder="Enter a task"
                value={newTask}
                onChange={(e) => setNewTask(e.target.value)}
            />
            <button onClick={addTask}>Add Task</button>
            {tasks.length === 0 ? (
                <p>You have no tasks left yay</p>
            ) : (
                <ul >
                    {tasks.map((task) => (
                        <li
                            key={task.id}
                            style={{
                                textDecoration: task.completed ? 'line-through' : 'none',
                                cursor: 'pointer',
                            }}
                            onMouseOver={() => toggleTaskCompletion(task.id)}
                            onClick={() => deleteTask(task.id)}
                        >
                            {task.text}
                        </li>

                    ))}
                </ul>)}
        </div >

    )
};
export default Todo;


