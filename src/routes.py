from flask import render_template, jsonify, request, Response
from bson import json_util
from bson.objectid import ObjectId
from flask.cli import F
from src import app, mongo

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/form_game')
def form_game():
    return render_template('form_game.html')
  
  
#CREATE
@app.route('/games', methods=['POST'])
def insert_game():
    name = request.form['name']
    min_players = int(request.form['min_players'])
    max_players = int(request.form['max_players'])
    age_limit = int(request.form['age_limit'])
    country = request.form['country']
    cost = float(request.form['cost'])
    if name and min_players and max_players and age_limit and country and cost:
        try:
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
                return jsonify({"success": False, "message": "No se pudo insertar el juego"}), 400
                
        except ValueError as e:
            return jsonify({"success": False, "message": f"Error al insertar el juego: {e}"}), 500
        
    
    return render_template("form_game.html")
    
    

#READ
@app.route('/games/', methods=['GET'])
@app.route('/games', methods=['GET'])
def get_games():
    games = mongo.db.games.find()
    
    return render_template("games.html", games=games)
    # return Response(response, mimetype='application/json')

#READ
@app.route('/games/<id>', methods=['GET'])
def get_game(id):
    if id:
        try:
            game_id = ObjectId(id)
        except ValueError:
            return json_util.dumps({"message": "Invalid game ID. Must be a valid ObjectId."}), 400

        game = mongo.db.games.find_one({'_id': game_id})

        if not game:
            return json_util.dumps({"message": "Game not founded"}), 404

        response = json_util.dumps(game)
        return Response(response, mimetype='application/json')

    else:
        games = list(mongo.db.games.find())
        response = json_util.dumps(games)
        return Response(response, mimetype='application/json')
    
    # if not id:
    #     return jsonify({"message": "Id missing"}), 404
    
    # game = mongo.db.games.find_one({'_id': ObjectId(id)})
    # response = json_util.dumps(game)
    
    # return Response(response, mimetype='application/json')

#DELETE
@app.route('/games/<id>', methods=['DELETE'])
def delete_game(id):
    result = mongo.db.games.delete_one({'_id': ObjectId(id)})
    if result.deleted_count == 1:
        response = jsonify({"message": "The game was successfully deleted"}),200
        return response
    else:
        return jsonify({"message": "Game not founded"}),404



#Metodo PUT actualizamos objeto completo
#Metodo PATCH actualizamos un campo del objeto

#UPDATE
@app.route('/games/<id>', methods=['PUT'])
def update_game(id):
    name = request.json['name']
    min_players = request.json['min_players']
    max_players = request.json['max_players']
    age_limit = request.json['age_limit']
    country = request.json['country']
    cost = request.json['cost'] 
    
    if name and min_players and max_players and age_limit and country and cost:
        mongo.db.games.update_one(
            {'_id': ObjectId(id)}, 
            {'$set': {
                'name': name,
                'min_players': min_players,
                'max_players': max_players,
                'age_limit': age_limit,
                'country': country,
                'cost': cost
            }})
        response = jsonify({"message": "The game was updated successfully"}),200
        return response
    else:
        return jsonify({"message": "Missing data"}),400
    
    return jsonify({"message": "Game not found, or some input hasn't been completed"}), 400



if __name__ == '__main__':
#   app.run(debug=True)
  app.run(host='0.0.0.0')