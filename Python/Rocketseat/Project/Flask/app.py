from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("description",""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso!"})

@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = []
    for task in tasks:
        task_list.append(task.to_dict())
    output = {
        "tasks": task_list,
        "total_tasks":0
    }
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)