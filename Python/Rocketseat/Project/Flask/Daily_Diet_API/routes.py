from flask import jsonify, request
from main import app, db
from datetime import datetime 
from models import Meal

@app.route('/meals', methods=['POST'])
def add_meal():
    """
    Adiciona uma nova refeição.
    Exemplo de payload JSON:
    {
        "name": "Almoço",
        "description": "Frango grelhado com salada",
        "date_time": "2024-01-24T12:30:00",
        "is_within_diet": true
    }
    """
    data = request.get_json()

    new_meal = Meal(
        name=data['name'],
        description=data.get('description', ''),
        date_time=data.get('date_time', datetime.utcnow()),
        is_within_diet=data.get('is_within_diet', True)
    )

    db.session.add(new_meal)
    db.session.commit()

    return jsonify({'message': 'Refeição adicionada com sucesso'}), 201

@app.route('/meals/<int:meal_id>', methods=['PUT'])
def edit_meal(meal_id):
    """
    Edita uma refeição existente.
    Exemplo de payload JSON:
    {
        "name": "Jantar",
        "description": "Peixe assado com legumes",
        "date_time": "2024-01-24T19:00:00",
        "is_within_diet": true
    }
    """
    meal = Meal.query.get(meal_id)

    if not meal:
        return jsonify({'message': 'Refeição não encontrada'}), 404

    data = request.get_json()

    meal.name = data['name']
    meal.description = data.get('description', '')
    meal.date_time = data.get('date_time', datetime.utcnow())
    meal.is_within_diet = data.get('is_within_diet', True)

    db.session.commit()

    return jsonify({'message': 'Refeição atualizada com sucesso'})

@app.route('/meals/<int:meal_id>', methods=['DELETE'])
def delete_meal(meal_id):
    """
    Apaga uma refeição existente.
    """
    meal = Meal.query.get(meal_id)

    if not meal:
        return jsonify({'message': 'Refeição não encontrada'}), 404

    db.session.delete(meal)
    db.session.commit()

    return jsonify({'message': 'Refeição deletada com sucesso'})

@app.route('/meals', methods=['GET'])
def get_all_meals():
    """
    Retorna todas as refeições do usuário.
    """
    meals = Meal.query.all()

    meal_list = []
    for meal in meals:
        meal_list.append({
            'id': meal.id,
            'name': meal.name,
            'description': meal.description,
            'date_time': meal.date_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'is_within_diet': meal.is_within_diet
        })

    return jsonify({'meals': meal_list})

@app.route('/meals/<int:meal_id>', methods=['GET'])
def get_meal(meal_id):
    """
    Retorna uma única refeição pelo ID.
    """
    meal = Meal.query.get(meal_id)

    if not meal:
        return jsonify({'message': 'Refeição não encontrada'}), 404

    meal_data = {
        'id': meal.id,
        'name': meal.name,
        'description': meal.description,
        'date_time': meal.date_time.strftime('%Y-%m-%dT%H:%M:%S'),
        'is_within_diet': meal.is_within_diet
    }

    return jsonify({'meal': meal_data})

if __name__ == '__main__':
    app.run(debug=True)
