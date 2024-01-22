import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_create_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json['id']

def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "completed": True,
            "description": "Nova descrição",
            "title": "Passear atualizar"
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        if response.status_code != 200:
            print(response.text)  # Adicione esta linha para imprimir o corpo da resposta em caso de erro
        
        # Verifica se o código de status é o esperado
        assert response.status_code == 200

        response_json = response.json()
        assert "message" in response_json

        if response.status_code != 200:
            print(response.text)  # Adicione esta linha para imprimir o corpo da resposta em caso de erro

        # Verifica a tarefa atualizada fazendo outra solicitação GET
        updated_response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert updated_response.status_code == 200

        updated_response_json = updated_response.json()

        # Verifica os valores atualizados
        assert "title" in updated_response_json
        assert updated_response_json["title"] == payload["title"]

        assert "description" in updated_response_json
        assert updated_response_json["description"] == payload["description"]

        assert "completed" in updated_response_json
        assert updated_response_json["completed"] == payload["completed"]

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        response.status_code == 200

        response = requests.get(f'{BASE_URL}/tasks/{task_id}')
        assert response.status_code == 404