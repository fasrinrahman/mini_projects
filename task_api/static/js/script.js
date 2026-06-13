console.log("app.js loaded successfully");

window.loadTasks = async function () {

    const response = await fetch("/tasks");

    const result = await response.json();

    const taskList =
        document.getElementById("task-list");

    taskList.innerHTML = "";

    result.data.forEach(task => {

        taskList.innerHTML += `
        <div class="task">

            <div>
                <strong>${task.title}</strong>
                <br>
                <small>${task.status}</small>
            </div>

            <button
                onclick="deleteTask(${task.id})"
            >
                Delete
            </button>

        </div>
        `;
    });
};

window.addTask = async function () {

    const title =
        document.getElementById("title").value;

    if (!title.trim()) {

        alert("Please enter a task");

        return;
    }

    await fetch("/tasks", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            title: title,

            status: "Pending"
        })
    });

    document.getElementById("title").value = "";

    loadTasks();
};

window.deleteTask = async function (id) {

    await fetch(`/tasks/${id}`, {

        method: "DELETE"
    });

    loadTasks();
};

loadTasks();

