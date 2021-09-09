from flask_cors import CORS
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
import numpy as np
import pandas as pd
import json


app = Flask(__name__)
CORS(app)

@app.route('/users', methods=['POST'])
def create_user():
    # se debe import de flash el request
    print(request)
    # capturo los valore del body
    print(request.json)
    # return {'mensaje': 'recibido'}
    response = {
        'haha': 122
    }
    return response
    # return not_found()

@app.route('/users', methods=['GET'])
def list_user():
    response = {
        'haha': 122
    }
    return response


# parmetrros params se usa <varianle>
@app.route('/users/<idUser>', methods=['GET'])
def get_user(idUser):
    response = {
        'haha': idUser
    }
    return response


# subir file por formData
@app.route('/haha', methods=['GET'])
def query_params():
    aaa = request.args
    bbb = request.query_string
    print('arg',aaa)
    print('string',bbb)
    # obtener valor del quety params
    print(request.args['kevin'])
    response = jsonify(
        {
        'mensaje': 'error pendejo',
        'status': 4004
    })
    return response

# subir file por formData
@app.route('/upload', methods=['POST'])
def subir_file():
    aaa = request.files['file']
    print(aaa)
    data = pd.read_csv(aaa)
    print(data['Name'])
    print(type(data['Name']))
    result = data.to_json(orient="split")
    parsed = json.loads(result)
    json.dumps(parsed, indent=4)  
    response = jsonify(
        {
        'mensaje': 'error pendejo',
        'status': 4004
    })
    return json.dumps(parsed, indent=4) 

# manejador de error
@app.errorhandler(404)
def not_found(error=None):
    response = jsonify(
        {
        'mensaje': 'error pendejo',
        'status': 4004
    }
    )
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True)