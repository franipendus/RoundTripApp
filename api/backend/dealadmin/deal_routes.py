########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

dealadmin = Blueprint('dealadmin', __name__)

# Get all customers from the DB
@dealadmin.route('/dealadmin/deals/<dealadmin_id>', methods=['GET'])
def get_ads(dealadmin_id):
    current_app.logger.info('deal_routes.py: GET /dealadmin/deals/<dealadmin_id>')
   
    cursor = db.get_db().cursor()
    cursor.execute(f"""select date as 'Date', hotel_name as 'Hotel Name', description as 'Description'
                   from dealInfo where admin_id = {dealadmin_id}""") 
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@dealadmin.route('/dealadmin/dealinfospecific/<hotel_id>', methods=['GET'])
def get_ad_specific(hotel_id):
    current_app.logger.info('deal_routes.py: GET /dealadmin/dealinfospecific/<hotel_id>')
   
    cursor = db.get_db().cursor()
    cursor.execute(f"""select date as 'Date', hotel_name as 'Hotel Name', description as 'Description'
                   from dealInfo JOIN hotels ON dealInfo.hotel_id = hotels.id where hotels.id = {hotel_id}""") 
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@dealadmin.route('dealadmin/dealimps/<deal_id>', methods=['GET'])
def get_adImps(deal_id):
    current_app.logger.info('deal_routes.py: GET dealadmin/dealimps/<deal_id>')
   
    cursor = db.get_db().cursor()
    cursor.execute(f"""select date as 'Date',  
    clicked  as   'Clicked',
    traveler_id  as 'Traveler'   from dealImpressions where deal_id = {deal_id}""") 

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@dealadmin.route('/dealadmin/dealimps/trav/<traveler_id>', methods=['GET'])
def get_adImpsTrav(traveler_id):
    current_app.logger.info('deal_routes.py: GET /dealadmin/dealimps/trav/<traveler_id>')
   
    cursor = db.get_db().cursor()
    cursor.execute(f"""select dealImpressions.date as 'Date Interacted', 
                   hotel_name as 'Hotel Name', description as 'Description' 
       from dealImpressions JOIN dealInfo on dealImpressions.deal_id = dealInfo.id where traveler_id = {traveler_id}""") 

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response



