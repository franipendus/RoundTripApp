########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

advertisers = Blueprint('advertisers', __name__)

# Get all customers from the DB
@advertisers.route('/advertisers/adinfo/<advertiser_id>', methods=['GET'])
def get_ads(advertiser_id):
    current_app.logger.info('advertisers_routes.py: GET /advertisers/adinfo/<advertiser_id>')
   
    cursor = db.get_db().cursor()
    cursor.execute(f"""select date as 'Date', title as 'Title', description as 'Description', price as 'Price'
                   from adInfo where advertiser_id= {advertiser_id}""") 
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@advertisers.route('/advertisers/adinfospecific/<ad_id>', methods=['GET'])
def get_ad_specific(ad_id):
    current_app.logger.info('advertisers_routes.py: GET /advertisers/adinfospecific/<ad_id>')
   
    cursor = db.get_db().cursor()
    cursor.execute(f"""select date as 'Date', title as 'Title', description as 'Description', price as 'Price'
                   from adInfo where id = {ad_id}""") 
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@advertisers.route('/advertisers/adimp/<ad_id>', methods=['GET'])
def get_adImps(ad_id):
    current_app.logger.info('advertisers_routes.py: GET /advertisers/adimp/<ad_id>')
   
    cursor = db.get_db().cursor()
    cursor.execute(f"""select date as 'Date',  
    clicked  as   'Clicked',
    traveler_id  as 'Traveler'   from adImpressions where ad_id = {ad_id}""") 

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@advertisers.route('/advertisers/adimp/trav/<traveler_id>', methods=['GET'])
def get_adImpsTrav(traveler_id):
    current_app.logger.info('advertisers_routes.py: GET /advertisers/adimp/trav/<traveler_id>')
   
    cursor = db.get_db().cursor()
    cursor.execute(f"""select adImpressions.date as 'Date Interacted', 
                   title as 'Title', description as 'Description' 
       from adImpressions JOIN adInfo where adImpressions.ad_id = adInfo.id AND traveler_id = {traveler_id}""") 

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response



