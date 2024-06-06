from backend.ml_models.model1 import predict
from backend.ml_models.model1 import train 
from backend.db_connection import db
import numpy as np
import logging
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

ml_models = Blueprint('ml_models', __name__)

# prediction model route 1: hotel cost per night
@ml_models.route('/ml_models/1/<v1>/<v2>/<v3>/<v4>/<v5>', methods=['GET'])
def get_m1(v1,v2, v3, v4, v5):

    # Execute prediction
    response = predict(v1, v2, v3, v4, v5)
    
    # format and return the response
    return_dict = {'result': response}

    #the_response = make_response(jsonify(return_dict))
    the_response = make_response(return_dict)
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    #return str(the_response)
    return return_dict

# training model 1
@ml_models.route('/ml_models/1', methods=['GET'])
def train_m1():
    # Execute training
    response = train()
    return 'Sucess!'