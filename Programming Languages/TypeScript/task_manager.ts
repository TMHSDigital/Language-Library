import * as readline from "readline";

interface Task {
    id: number;
    description: string;
}

class TaskManager {
    private tasks: Task[] = [];
    private nextId: number = 1;

    addTask(description: string): void {
        this.tasks.push({ id: this.nextId++, description });
    }

    viewTasks(): void {
        if (this.tasks.length === 0) {
            console.log("No tasks available.");
        } else {
            this.tasks.forEach(task => {
                console.log(`${task.id}. ${task.description}`);
            });
        }
    }

    deleteTask(id: number): void {
        const index = this.tasks.findIndex(task => task.id === id);
        if (index !== -1) {
            this.tasks.splice(index, 1);
            console.log(`Task ${id} deleted.`);
        } else {
            console.log(`Task ${id} not found.`);
        }
    }
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const taskManager = new TaskManager();

function mainMenu() {
    console.log("\nTask Manager");
    console.log("1. Add Task");
    console.log("2. View Tasks");
    console.log("3. Delete Task");
    console.log("4. Exit");
    rl.question("Choose an option: ", choice => {
        switch (choice.trim()) {
            case "1":
                rl.question("Enter task description: ", description => {
                    taskManager.addTask(description.trim());
                    mainMenu();
                });
                break;
            case "2":
                taskManager.viewTasks();
                mainMenu();
                break;
            case "3":
                rl.question("Enter task ID to delete: ", id => {
                    taskManager.deleteTask(Number(id.trim()));
                    mainMenu();
                });
                break;
            case "4":
                console.log("Exiting...");
                rl.close();
                break;
            default:
                console.log("Invalid option. Please try again.");
                mainMenu();
        }
    });
}

mainMenu();
