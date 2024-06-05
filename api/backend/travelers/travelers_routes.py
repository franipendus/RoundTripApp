########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint, request, jsonify, make_response, current_app
import json
from backend.db_connection import db

travelers = Blueprint('travelers', __name__)

# Get all customers from the DB
@travelers.route('/travelers/trips/<traveler_id>', methods=['GET'])
def get_trips(traveler_id):
    current_app.logger.info('travelers_routes.py: GET /travelers/trips/<traveler_id>')
   
    cursor = db.get_db().cursor()
    cursor.execute(f"""select distinct sd as 'start date', ed as 'end date', oa as 'flight origin', da as 'flight destination',
       hotels.name as 'hotel name' from hotels JOIN
(select fn,origin_airport as oa, destination_airport as da, sd, ed, hotel_id as hi, i  from hotelBookings JOIN
(select flight_number as fn, sd, ed, i from flightBookings JOIN
 (select trips.id as i, start_date as sd, end_date as ed, traveler_id
         from trips JOIN travelers ON travelers.id = trips.traveler_id
      ) as t
ON t.i = flightBookings.trip_id) as t2 JOIN flights
ON t2.fn = flights.number AND t2.i = hotelBookings.trip_id) as t3 JOIN airports
where hotels.id = t3.hi AND t3.i = {traveler_id}""") 
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

@travelers.route('/travelers/trips/<sdate>/<edate>/<trip_id>', methods=['PUT'])
def update_trips():
    current_app.logger.info('PUT /travelers/trips/<sdate>/<edate>/<trip_id>')
    trips = request.json
    # current_app.logger.info(cust_info)
    s = trips['start_date']
    e = trips['end_date']
    ti = trips['id']
    

    query = 'update trips SET start_date = %s, end_date = %s where trip_id = %s'
    data = (s, e, ti)
    cursor = db.get_db().cursor()
    r = cursor.execute(query, data)
    db.get_db().commit()
    return 'Hotel Bookings updated!'

# Get customer detail for customer with particular userID
@travelers.route('/travelers/countries/<country>', methods=['GET'])
def get_country(country):
    current_app.logger.info('GET /travelers/countries/<country> route')
    cursor = db.get_db().cursor()
    cursor.execute("select * from countries where name = '{0}'".format(country))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    current_app.logger.info(f'theData = {theData}')
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    current_app.logger.info(f'json_data = {json_data}')
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Get customer detail for customer with particular userID
@travelers.route('/travelers/promotions/<city>', methods=['GET'])
def get_promos(city):
    current_app.logger.info('GET /travelers/promotions/<city> route')
    cursor = db.get_db().cursor()
    cursor.execute( f"""select distinct dealInfo.date as 'Date', hotel_name as 'Hotel Name', 
                   dealInfo.name as 'Deal Information',dealInfo.description as 'Deal Description', 
                   amenities as 'Amentities', city as 'City'
from dealInfo Join hotels
ON hotels.id = dealInfo.hotel_id WHERE city = '{city}'""")
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    current_app.logger.info(f'theData = {theData}')
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    current_app.logger.info(f'json_data = {json_data}')
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


@travelers.route('/travelers/favhotels/<city>/<traveler_id>', methods=['GET'])
def get_favHotels(city, traveler_id):
    current_app.logger.info('GET /travelers/favhotels/<city>/<traveler_id> route')
    cursor = db.get_db().cursor()
    cursor.execute( f""" select distinct hotels.id as 'Hotel ID', name  as 'Name',
    number_rooms  as 'Number of Rooms',
    amenities     as 'Amentities',
    street_number as 'Street Number',
    street        as 'Street' from hotels 
                    JOIN favHotels JOIN travelers 
                   ON favHotels.hotel_id = hotels.id 
                   WHERE hotels.city = '{city}'
                    AND favHotels.traveler_id = '{traveler_id}'""")
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    current_app.logger.info(f'theData = {theData}')
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    current_app.logger.info(f'json_data = {json_data}')
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response