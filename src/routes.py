from flask import redirect, render_template, jsonify, request, url_for
from bson import json_util
from bson.objectid import ObjectId
from src import app, mongo

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/new_game', methods=['GET'])
def new_game():
    return render_template('new_game.html'), 200

@app.route('/update', methods=['POST'])
def update():
    game_data = request.get_json()
    if game_data:
        return render_template('update.html', game=game_data), 200
    else:
        return jsonify({"success": False, "message": "Invalid data"}), 404

  
#CREATE
@app.route('/games/create', methods=['POST'])
def insert_game():
    name = request.form['name']
    min_players = int(request.form['min_players'])
    max_players = int(request.form['max_players'])
    age_limit = int(request.form['age_limit'])
    country = request.form['country']
    cost = float(request.form['cost'])
    
    if name and min_players > 0 and max_players > 0 and age_limit > 0 and country and cost > 0:
        try:
            game = list(mongo.db.games.find({'name': name}))
            
            if not game:    
                result = mongo.db.games.insert_one(
                    {
                        'name': name, 
                        'min_players': min_players, 
                        'max_players': max_players, 
                        'age_limit': age_limit, 
                        'country': country, 
                        'cost': cost
                    }
                )    
                
                if result.inserted_id:
                    return jsonify({"success": True, "message": "Juego insertado correctamente!"}), 200
            else:
                return jsonify({"success": False, "message": "Juego ya existe"}), 400
            
        except ValueError as e:
            return jsonify({"success": False, "message": f"Error al insertar el juego: {e}"}), 500
    else:
        return jsonify({"success": False, "message": "Datos inválidos"}), 400
    
    return render_template("form_game.html")
    

#READ
@app.route('/games/', methods=['GET'])
@app.route('/games', methods=['GET'])
def get_games():
    games = mongo.db.games.find()
    return render_template("games.html", games=games)

#READ
@app.route('/games/<id>', methods=['GET'])
def get_game(id):
    if id:
        try:
            game_id = ObjectId(id)
        except ValueError:
            return json_util.dumps({"message": "ID inválido"}), 400

        game = mongo.db.games.find_one({'_id': game_id})

        if game:
            return render_template('update.html', game=game), 200

    return redirect(url_for('get_games'))

#DELETE
@app.route('/games/<id>', methods=['DELETE'])
def delete_game(id):
    result = mongo.db.games.delete_one({'_id': ObjectId(id)})
    if result.deleted_count == 1:
        return jsonify({"success": True, "message": "Se elimino correctamente!"}), 200
    else:
        return jsonify({"success": False, "message": "Juego no encontrado"}), 404



#Metodo PUT actualizamos objeto completo
#Metodo PATCH actualizamos un campo del objeto

#UPDATE -> Uso metodo POST porque tuve complicaciones al no reconocer el metodo PUT
@app.route('/games/update/<id>', methods=['POST'])
def update_game(id):
    name = request.form['name']
    min_players = int(request.form['min_players'])
    max_players = int(request.form['max_players'])
    age_limit = int(request.form['age_limit'])
    country = request.form['country']
    cost = float(request.form['cost'])
    
    if name and min_players and max_players and age_limit and country and cost:
        response = mongo.db.games.update_one(
            {'_id': ObjectId(id)}, 
            {'$set': {
                'name': name,
                'min_players': min_players,
                'max_players': max_players,
                'age_limit': age_limit,
                'country': country,
                'cost': cost
            }})
        if response.modified_count == 1:
            return jsonify({"success": True, "message": "Se actualizo correctamente"}), 200
        else:
            return jsonify({"success": False, "message": "No se encontro juego para actualizar"}), 404
    else:
        return jsonify({"message": "Falta informacion, datos inválidos"}),400
