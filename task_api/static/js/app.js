console.log("TaskFlow JS Loaded");

// =====================
// LOAD TASKS
// =====================

async function loadTasks() {

    try {

        const response =
            await fetch("/tasks");

        const result =
            await response.json();

        const tasks =
            result.data;

        const taskList =
            document.getElementById(
                "task-list"
            );

        taskList.innerHTML = "";

        let completed = 0;
        let pending = 0;

        tasks.forEach(task => {

            if (
                task.status === "Completed"
            ) {

                completed++;

            } else {

                pending++;
            }

            taskList.innerHTML += `
            
            <div class="task-card">

                <div>

                    <h5>
                        ${task.title}
                    </h5>

                    <span
                        class="
                            status-badge
                            ${task.status.toLowerCase()}
                        "
                    >
                        ${task.status}
                    </span>

                </div>

                <button
                    class="btn btn-danger"

                    onclick="
                        deleteTask(
                            ${task.id}
                        )
                    "
                >

                    <i
                        class="
                        fa-solid
                        fa-trash
                        "
                    ></i>

                </button>

            </div>
            `;
        });

        document.getElementById(
            "totalTasks"
        ).textContent =
            tasks.length;

        document.getElementById(
            "completedTasks"
        ).textContent =
            completed;

        document.getElementById(
            "pendingTasks"
        ).textContent =
            pending;

    } catch (error) {

        console.error(error);
    }
}


// =====================
// ADD TASK
// =====================

window.addTask =
async function () {

    const title =
        document.getElementById(
            "title"
        ).value;

    const status =
        document.getElementById(
            "status"
        ).value;

    if (
        title.trim() === ""
    ) {

        alert(
            "Please enter a task"
        );

        return;
    }

    try {

        await fetch(
            "/tasks",
            {

                method: "POST",

                headers: {
                    "Content-Type":
                    "application/json"
                },

                body:
                JSON.stringify({

                    title: title,

                    status: status
                })
            }
        );

        document.getElementById(
            "title"
        ).value = "";

        loadTasks();

    } catch (error) {

        console.error(error);
    }
};


// =====================
// DELETE TASK
// =====================

window.deleteTask =
async function (id) {

    try {

        await fetch(
            `/tasks/${id}`,
            {
                method:
                    "DELETE"
            }
        );

        loadTasks();

    } catch (error) {

        console.error(error);
    }
};


// =====================
// INITIAL LOAD
// =====================

loadTasks();