########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

advertisers = Blueprint('advertisers', __name__)

# Get all ad information posted by a specific advertiser
@advertisers.route('/advertisers/adinfo/<advertiser_id>', methods=['GET'])
def get_ads(advertiser_id):
    cursor = db.get_db().cursor()
    cursor.execute(f"""select id as 'Ad ID', title as 'Title'
                   from adInfo where advertiser_id = {advertiser_id}""") 

    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# gets all ad ids made by a specific advertiser
@advertisers.route('/advertisers/adids/<adver_id>', methods=['GET'])
def get_ad_ids(adver_id):
    cursor = db.get_db().cursor()
    cursor.execute(f"""select id as 'Ad ID' from adInfo where advertiser_id = {adver_id}""") 

    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response



# Get specific ad information posted by a specific advertiser
@advertisers.route('/advertisers/adinfospecific/<advertiser_id>/<ad_id>', methods=['GET'])
def get_ad_specific(ad_id, advertiser_id):
    cursor = db.get_db().cursor()
    cursor.execute(f"""select distinct date as 'Date', title as 'Title', description as 'Description', price as 'Price'
                   from adInfo JOIN advertisers where adInfo.id = {ad_id} AND advertiser_id = {advertiser_id}""") 

    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Get all ad impressioms of a specific ad and posted by a specific advertiser
@advertisers.route('/advertisers/adimp/<advertiser_id>/<ad_id>', methods=['GET'])
def get_adImps(ad_id, advertiser_id):
    
    cursor = db.get_db().cursor()
    cursor.execute(f"""select adImpressions.date as 'Date',  
    clicked  as   'Clicked',
    traveler_id  as 'Traveler'   from adImpressions JOIN adInfo ON adInfo.id = adImpressions.ad_id
                   where ad_id = {ad_id} AND adInfo.advertiser_id = {advertiser_id}""") 

 
    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Get all ad impressioms made by a specific traveler and posted by a specific advertiser
@advertisers.route('/advertisers/adimp/trav/<advertiser_id>/<traveler_id>', methods=['GET'])
def get_adImpsTrav(traveler_id, advertiser_id):
    
    cursor = db.get_db().cursor()
    cursor.execute(f"""select adInfo.id as 'Ad ID', adImpressions.date as 'Date Interacted', 
                   title as 'Title', description as 'Description' 
       from adImpressions JOIN adInfo ON adImpressions.ad_id = adInfo.id WHERE traveler_id = {traveler_id}
        AND adInfo.advertiser_id = {advertiser_id}""") 

    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Posts a new ad for a specific advertiser 
@advertisers.route('/advertisers/adinfo', methods=['POST'])
def add_new_ad():
    
    # collecting data from the request object 
    the_data = request.json

    #extracting the variable
    cursor = db.get_db().cursor()
    cursor.execute("SELECT MAX(id) as 'id' FROM adInfo")
    max_id = cursor.fetchone()['id']
    
    if max_id is None:
        max_id = 0
    id = max_id + 1

    date = the_data['date']
    adver_id = the_data['adver_id']
    description = the_data['description']
    price = the_data['price']
    title = the_data['title']

    # Constructing the query
    query = f"""INSERT INTO adInfo (id, date, advertiser_id, description, price, title) 
               VALUES ({id}, '{str(date)}', {adver_id}, '{description}', {price}, '{title}')"""

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    return 'Success!'

# Deletes a specific ad made by a specific advertiser 
@advertisers.route('/advertisers/adinfo/<ad_id>', methods=['DELETE'])
def delete_ad(ad_id):
    cursor = db.get_db().cursor()
    
    # Execute the DELETE statement
    cursor.execute(f"DELETE FROM adInfo WHERE id = {ad_id}") 
    db.get_db().commit()
    
    return "success"


