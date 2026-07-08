const API = "/api/tasks";

// LOAD TASKS
async function loadTasks() {

    const res = await fetch(API);
    const tasks = await res.json();

    const list = document.getElementById("taskList");

    list.innerHTML = "";

    let completed = 0;
    let pending = 0;

    tasks.forEach(t => {

        if (t.status === "Done") completed++;
        else pending++;

        list.innerHTML += `
        <div class="task-card priority-${t.priority.toLowerCase()}">
            <div>
                <h5>${t.title}</h5>
                <small>${t.description || ""}</small>
                <p><b>${t.status}</b> | ${t.due_date || "No date"}</p>
            </div>

            <button class="btn btn-danger btn-sm" onclick="deleteTask(${t.id})">
                <i class="fa fa-trash"></i>
            </button>
        </div>`;
    });

    document.getElementById("total").innerText = tasks.length;
    document.getElementById("completed").innerText = completed;
    document.getElementById("pending").innerText = pending;
}

// CREATE TASK
async function createTask() {

    const data = {
        title: title.value,
        description: description.value,
        status: status.value,
        priority: priority.value,
        due_date: due.value
    };

    await fetch(API, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    loadTasks();
}

// DELETE
async function deleteTask(id) {
    await fetch(`${API}/${id}`, { method: "DELETE" });
    loadTasks();
}

loadTasks();