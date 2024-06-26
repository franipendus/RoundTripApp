########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

travelers = Blueprint('travelers', __name__)

# Get all trips for a spceific traveler
@travelers.route('/travelers/trips/<traveler_id>', methods=['GET'])
def get_trips(traveler_id):
    current_app.logger.info('travelers_routes.py: GET /travelers/trips/<traveler_id>')
    cursor = db.get_db().cursor()
    cursor.execute(f"""select trips.id as 'Trip Id', start_date as 'Start Date', end_date as 'End Date'
         from trips where trips.traveler_id = {traveler_id}
   """) 
    
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Gets specific trip information 
@travelers.route('/travelers/spectrips/<traveler_id>/<trip_id>', methods=['GET'])
def get_specific_trips(traveler_id, trip_id):
    current_app.logger.info('travelers_routes.py: GET /travelers/trips/<traveler_id>')
    cursor = db.get_db().cursor()
    cursor.execute(f"""select distinct sd as 'Start date', ed as 'End date', oa as 'Flight Origin', da as 'Flight Destination', 
                   hotels.city as 'Hotel City', hotels.country as 'Hotel Country',
       hotels.name as 'Hotel Name' from hotels JOIN
(select fn,origin_airport as oa, destination_airport as da, sd, ed, hotel_id as hi, i, ti  from hotelBookings JOIN
(select flight_number as fn, sd, ed, i, ti from flightBookings JOIN
 (select trips.id as i, start_date as sd, end_date as ed, traveler_id as ti
         from trips JOIN travelers where travelers.id = trips.traveler_id AND trips.id = {trip_id}
      ) as t
where t.i = flightBookings.trip_id) as t2 JOIN flights
where t2.fn = flights.number AND t2.i = hotelBookings.trip_id) as t3 JOIN airports
where  hotels.id = t3.hi AND t3.ti = {traveler_id}""") 
    
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get all trip ids for a spceific traveler
@travelers.route('/travelers/tripid/<traveler_id>', methods=['GET'])
def get_tripIds(traveler_id):
    current_app.logger.info('travelers_routes.py: GET /travelers/tripid/<traveler_id>')
    cursor = db.get_db().cursor()
    cursor.execute(f"""
 select distinct trips.id as 'Id' from trips JOIN travelers where travelers.id = trips.traveler_id
      AND travelers.id = {traveler_id}""") 
    
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# updates a trip for a specific traveler 
@travelers.route('/travelers/trips', methods=['PUT'])
def update_trips():
    current_app.logger.info('PUT /travelers/trips')
    trips = request.json
    start = trips['s']
    end = trips['e']
    tripId = trips['ti']
    
    query = f"""update trips SET start_date = '{start}', end_date = '{end}' where id = {tripId}"""
   
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    return 'Trips updated!'

# Get information about a spceific country
@travelers.route('/travelers/countries/<country>', methods=['GET'])
def get_country(country):
    current_app.logger.info('GET /travelers/countries/<country> route')
    cursor = db.get_db().cursor()
    cursor.execute(f"select * from countries where name = '{country}'")
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    current_app.logger.info(f'theData = {theData}')
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Get all promotions in a specific city 
@travelers.route('/travelers/promotions/<city>', methods=['GET'])
def get_promos(city):
    current_app.logger.info('GET /travelers/promotions/<city> route')
    cursor = db.get_db().cursor()
    cursor.execute( f"""select distinct dealInfo.date as 'Date', hotel_name as 'Hotel Name', 
                   dealInfo.name as 'Deal Information',dealInfo.description as 'Deal Description', 
                   amenities as 'Amentities', city as 'City'
                   from dealInfo Join hotels
where hotels.id = dealInfo.hotel_id and city = '{city}'""")
    
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    current_app.logger.info(f'theData = {theData}')
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# gets all favorite hotels in a specific city for a specific traveler
@travelers.route('/travelers/favhotels/<city>/<traveler_id>', methods=['GET'])
def get_favHotels(city, traveler_id):
    cursor = db.get_db().cursor()
    cursor.execute( f""" select distinct hotels.id as 'Hotel ID', name  as 'Name',
    number_rooms  as 'Number of Rooms',
    amenities     as 'Amentities',
    street_number as 'Street Number',
    street        as 'Street' from hotels 
                    JOIN favHotels JOIN travelers 
                   where favHotels.hotel_id = hotels.id 
                   AND hotels.city = '{city}'
                    AND favHotels.traveler_id = '{traveler_id}'""")

    theData = cursor.fetchall()
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response