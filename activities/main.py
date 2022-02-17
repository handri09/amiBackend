from deta import Deta
from flask import Flask, jsonify, request
from flask_cors import CORS

deta = Deta("a0bbqsrh_c2bH4it9HCzFC5r6GPbqRtq2EXrR46Jx")

drive = deta.Drive("images") # access to your drive

actionsD = deta.Drive('actions')
photos = deta.Drive('photos')

actionsDB = deta.Base("actions")
waitDB = deta.Base("waiting")

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET', 'POST', 'DELETE', 'PUT'])
def home():

  if request.method == 'GET':
    actions = actionsDB.fetch()
    actions = actions.items

    return jsonify(actions, 201)

  if request.method == 'POST':

    # Drive
    photos.put('enf1.jpg', path='./enf1.jpg')

    actions = actionsDB.put({
      'name': request.json.get('name'),
      'picture': request.json.get('picture'),
      'story': request.json.get('story')
    })
    return jsonify(actions, 201)

  else :
    return jsonify(None, 201)

@app.route('/pic', methods = ['GET', 'POST', 'DELETE', 'PUT'])
def picture():
  if request.method == 'GET':
    hello = drive.get('1.jpg')
    content = hello.read()
    hello.close()
    return drive.get('1.jpg')