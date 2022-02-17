from deta import Deta
from flask import Flask, jsonify, request
from flask_cors import CORS

deta = Deta("a0bbqsrh_c2bH4it9HCzFC5r6GPbqRtq2EXrR46Jx")
todosDB = deta.Base("activity")
goalsDB = deta.Base("waiting")
app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET', 'POST', 'DELETE', 'PUT'])
def home():

  if request.method == 'GET':
    todos = todosDB.fetch()
    todos = todos.items
    return jsonify(todos, 201)

  if request.method == 'PUT':
    todo = todosDB.put(request.json)
    return jsonify(todo, 201)

  if request.method == 'POST':
    todo = todosDB.put({
      'name': request.json.get('name'),
      'complete': False,
    })
    return jsonify(todo, 201)

  if request.method == 'DELETE':
    todo = todosDB.delete(request.json.get('key'))
    return jsonify(todo, 201)

  else :
    return jsonify(None, 201)