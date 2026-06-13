async function loadTasks() {

    const response =
        await fetch("/tasks");

    const result =
        await response.json();

    const taskList =
        document.getElementById(
            "task-list"
        );

    taskList.innerHTML = "";

    result.data.forEach(task => {

        taskList.innerHTML += `
        
        <div class="task">

            <span>
                ${task.title}
            </span>

            <button
                onclick="deleteTask(${task.id})"
            >
                Delete
            </button>

        </div>
        `;
    });
}

async function addTask() {

    const title =
        document.getElementById(
            "title"
        ).value;

    await fetch(
        "/tasks",
        {
            method: "POST",

            headers: {
                "Content-Type":
                "application/json"
            },

            body: JSON.stringify({

                title: title,

                status: "Pending"
            })
        }
    );

    loadTasks();
}

async function deleteTask(id) {

    await fetch(

        `/tasks/${id}`,

        {
            method: "DELETE"
        }
    );

    loadTasks();
}

loadTasks();

