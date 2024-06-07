########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

dealadmin = Blueprint('dealadmin', __name__)

# Get all the deals posted by a specific deal admin
@dealadmin.route('/dealadmin/deals/<dealadmin_id>', methods=['GET'])
def get_deals(dealadmin_id):
    current_app.logger.info('deal_routes.py: GET /dealadmin/deals/<dealadmin_id>')
   
    cursor = db.get_db().cursor()
    cursor.execute(f"""select date as 'Date', dealInfo.id as 'Deal ID', dealInfo.name as 'Name'
                   from dealInfo JOIN hotels where dealInfo.hotel_id = hotels.id AND admin_id = {dealadmin_id}""") 

    theData = cursor.fetchall()
   
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# gets the deal info for a specific hotel which was posted by a specific deal admin
@dealadmin.route('/dealadmin/dealinfospecific/<dealAdmin>/<hotel_id>', methods=['GET'])
def get_deal_specific(hotel_id, dealAdmin):
    current_app.logger.info('deal_routes.py: GET /dealadmin/dealinfospecific/<hotel_id>')
   
    cursor = db.get_db().cursor()
    cursor.execute(f"""select date as 'Date', hotel_name as 'Hotel Name', description as 'Description', dealInfo.name as 'Name', city as 'City'
                   from dealInfo JOIN hotels ON dealInfo.hotel_id = hotels.id where hotels.id = {hotel_id}
                    AND dealInfo.admin_id = {dealAdmin}""") 
    
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# gets all of the deal impressions for deals posted by a specific deal admin
@dealadmin.route('dealadmin/dealimps/<admin>', methods=['GET'])
def get_dealImps(admin):
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

# gets all of the deal impressions made by a specific traveler for deals posted by a specific adminsitator
@dealadmin.route('/dealadmin/dealimps/trav/<admin>/<traveler_id>', methods=['GET'])
def get_dealImpsTrav(admin, traveler_id):
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

# Deletes a specific ad made by a specific advertiser 
@dealadmin.route('/deals/del/<deal_id>', methods=['DELETE'])
def delete_ad(deal_id):
    cursor = db.get_db().cursor()
    
    # Execute the DELETE statement
    cursor.execute(f"DELETE FROM dealInfo WHERE id = {deal_id}") 
    db.get_db().commit()
    
    return "success"

# gets all deal ids made by a specific deal admin
@dealadmin.route('/dealids/<admin>', methods=['GET'])
def get_deal_ids(admin):
    cursor = db.get_db().cursor()
    cursor.execute(f"""select id as 'Deal ID' from dealInfo where admin_id = {admin}""") 

    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# gets all hotel ids of deals made by a specific deal admin
@dealadmin.route('/hotelids/<admin>', methods=['GET'])
def get_hotelDeal_ids(admin):
    cursor = db.get_db().cursor()
    cursor.execute(f"""select hotel_id as 'Hotel ID' from dealInfo where admin_id = {admin}""") 

    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# gets all hotel ids in a specific city with a specific name
@dealadmin.route('hotelids/<hotel_name>/<city>', methods=['GET'])
def get_hotel_ids(hotel_name, city):
    cursor = db.get_db().cursor()
    cursor.execute(f"""select id as 'Hotel ID' from hotels where city = '{city}' AND hotels.name = '{hotel_name}'""") 

    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Posts a new deal for a specific deal admin 
@dealadmin.route('/post', methods=['POST'])
def add_new_deal():
    
    # collecting data from the request object 
    the_data = request.json

    #extracting the variable
    cursor = db.get_db().cursor()
    cursor.execute("SELECT MAX(id) as 'id' FROM dealInfo")
    max_id = cursor.fetchone()['id']
    if max_id is None:
        max_id = 0
    id = max_id + 1

    date = the_data['date']
    hotel_id = the_data['hotel_id']
    description = the_data['description']
    admin = the_data['admin']
    hotel_name = the_data['hotel_name']
    deal_name = the_data['deal_name']

    # Constructing the query
    query = f"""INSERT INTO dealInfo (id, date,
            hotel_name, hotel_id, name, description, 
            admin_id) 
               VALUES ({id}, '{str(date)}', '{hotel_name}', {hotel_id}, '{deal_name}','{description}', {admin})"""

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

