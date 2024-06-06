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

    theData = cursor.fetchall()
   
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@dealadmin.route('/dealadmin/dealinfospecific/<dealAdmin>/<hotel_id>', methods=['GET'])
def get_ad_specific(hotel_id, dealAdmin):
    current_app.logger.info('deal_routes.py: GET /dealadmin/dealinfospecific/<hotel_id>')
   
    cursor = db.get_db().cursor()
    cursor.execute(f"""select date as 'Date', hotel_name as 'Hotel Name', description as 'Description'
                   from dealInfo JOIN hotels ON dealInfo.hotel_id = hotels.id where hotels.id = {hotel_id}
                    AND dealInfo.admin_id = {dealAdmin}""") 
    
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@dealadmin.route('dealadmin/dealimps/<admin>', methods=['GET'])
def get_adImps(admin):
    current_app.logger.info('deal_routes.py: GET dealadmin/dealimps/<admin>')
   
    cursor = db.get_db().cursor()
    cursor.execute(f"""select dealImpressions.date as 'Date',  
    clicked  as   'Clicked',
    traveler_id  as 'Traveler'   from dealImpressions JOIN dealInfo where deal_id = dealInfo.id AND dealInfo.admin_id = {admin}""") 

    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@dealadmin.route('/dealadmin/dealimps/trav/<admin>/<traveler_id>', methods=['GET'])
def get_adImpsTrav(admin, traveler_id):
    current_app.logger.info('deal_routes.py: GET /dealadmin/dealimps/trav/<traveler_id>')
   
    cursor = db.get_db().cursor()
    cursor.execute(f"""select dealImpressions.date as 'Date Interacted', 
                   hotel_name as 'Hotel Name', description as 'Description' 
       from dealImpressions JOIN dealInfo on dealImpressions.deal_id = dealInfo.id where traveler_id = {traveler_id}
        AND dealInfo.admin_id = {admin}""") 

    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response



