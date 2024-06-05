# """
# model01.py is an example of how to access model parameter values that you are storing
# in the database and use them to make a prediction when a route associated with prediction is
# accessed. 
# """
from backend.db_connection import db
import numpy as np
import logging

from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

ml_models = Blueprint('ml_models', __name__)

# def train():
#   """
#   You could have a function that performs training from scratch as well as testing (see below).
#   It could be activated from a route for an "administrator role" or something similar. 
#   """
#   return 'Training the model'

# def test():
#   return 'Testing the model'

def predict(var01, var02, var03, var04, var05):
    
    params_array = np.array([ 109.73406702,   -0.83074924,    1.05019437,  -51.15928322,
         -0.88402242,   -1.28998772,   -0.90016681, -110.61999534,
         18.93146962,  -36.8372952 ,    4.76581827,   23.73717024,
         39.02418511])
    
    mean_flights = 323.81361111111113
    std_flights = 64.21462998123202
    mean_ratings = 4.762450341836946
    std_ratings = 0.08312695791275146
    mean_gdp = 57354.14375
    std_gdp = 2837.564499920837
    
    flight = (float(var01) - mean_flights)/std_flights
    rating = (float(var02) - mean_ratings)/std_ratings
    
    if var03 == 'London':
        co = np.array([0,0,0])
    if var03 == 'Madrid':
        co = np.array([1,0,0])
    if var03 == 'Paris':
        co = np.array([0,1,0])
    if var03 == 'Rome':
        co = np.array([0,0,1])

    if var04 == 'London':
        gdp = 51070
        cd = np.array([0,0,0])
    if var04 == 'Madrid':
        gdp = 34050
        cd = np.array([1,0,0])
    if var04 == 'Paris':
        gdp = 47360
        cd = np.array([0,1,0])
    if var04 == 'Rome':
        gdp = 39580
        cd = np.array([0,0,1])
  
    if var05 in ('January', 'February', 'March'):
        quarter = np.array([0,0,0])
    if var05 in ('April', 'May', 'June'):
        quarter = np.array([1,0,0])
    if var05 in ('July', 'August', 'September'):
        quarter = np.array([0,1,0])
    if var05 in ('October', 'November', 'December'):
        quarter = np.array([0,0,1])
        
    gdp = (gdp - mean_gdp)/std_gdp
    #input_array = np.array([1.0, float(var01), float(var02), float(gdp), co, cd, quarter])

    numerical_values = np.array([1.0, flight, rating, gdp])
    input_array = np.concatenate((numerical_values, co, cd, quarter))
  
    prediction = np.dot(params_array, input_array)

    return prediction


@ml_models.route('/ml_models/1/<v1>/<v2>/<v3>/<v4>/<v5>', methods=['GET'])
def get_m1(v1,v2, v3, v4, v5):
    current_app.logger.info(f'model 1 prediction')
    
    cursor = db.get_db().cursor()
    
    # Execute the DELETE statement
    response = str(predict(v1, v2, v3, v4, v5))
    
    return response

  ##############################################################
  
  # # retreive the parameters from the appropriate table
  # cursor.execute('select beta_0, beta_1, beta_2 from model1_param_vals')
  # # fetch the first row from the cursor
  # data = cursor.fetchone()
  # # calculate the predicted result using this functions arguments as well as the model parameter values
  # result = data[0] + int(var01) * data[1] + int(var02) * data[2]

  # # return the result 
  # return result