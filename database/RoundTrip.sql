DROP DATABASE IF EXISTS RoundTrip;
CREATE DATABASE IF NOT EXISTS RoundTrip;

USE RoundTrip;

DROP TABLE IF EXISTS travelers;
CREATE TABLE IF NOT EXISTS travelers
(
    id         INTEGER,
    first_name VARCHAR(255)        NOT NULL,
    last_name  VARCHAR(255)        NOT NULL,
    dob        DATE                NOT NULL,
    username   VARCHAR(255) UNIQUE NOT NULL,
    password   VARCHAR(255)        NOT NULL,

    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS countries;
CREATE TABLE IF NOT EXISTS countries
(
    name           VARCHAR(255) UNIQUE NOT NULL,
    safety_index   FLOAT               NOT NULL,
    safety_message VARCHAR(255),
    currency       VARCHAR(255)        NOT NULL,
    population     INTEGER             NOT NULL,
    capital        VARCHAR(255)        NOT NULL,
    language       VARCHAR(255)        NOT NULL,

    PRIMARY KEY (name)
);

DROP TABLE IF EXISTS airports;
CREATE TABLE IF NOT EXISTS airports
(
    code    VARCHAR(255) UNIQUE NOT NULL,
    name    VARCHAR(255)        NOT NULL,
    city    VARCHAR(255)        NOT NULL,
    country VARCHAR(255)        NOT NULL,

    PRIMARY KEY (code)
);

DROP TABLE IF EXISTS airlines;
CREATE TABLE IF NOT EXISTS airlines
(
    name VARCHAR(255) UNIQUE NOT NULL,
    url  VARCHAR(500)        NOT NULL,

    PRIMARY KEY (name)
);

DROP TABLE IF EXISTS flights;
CREATE TABLE IF NOT EXISTS flights
(
    number              INTEGER NOT NULL,
    airline             VARCHAR(255) NOT NULL,
    origin_airport      VARCHAR(255) NOT NULL,
    destination_airport VARCHAR(255) NOT NULL,
    price               FLOAT        NOT NULL,
    month VARCHAR(255) NOT NULL,

    PRIMARY KEY (number),
    FOREIGN KEY (origin_airport) REFERENCES airports (code)
        ON UPDATE cascade
        ON DELETE cascade,
    FOREIGN KEY (destination_airport) REFERENCES airports (code)
        ON UPDATE cascade
        ON DELETE cascade,
    FOREIGN KEY (airline) REFERENCES airlines (name)
        ON UPDATE cascade
        ON DELETE cascade
);


DROP TABLE IF EXISTS trips;
CREATE TABLE IF NOT EXISTS trips
(
    id          INTEGER UNIQUE NOT NULL,
    traveler_id INTEGER        NOT NULL,
    start_date  DATE           NOT NULL,
    end_date    DATE           NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (traveler_id) REFERENCES travelers (id)
        ON UPDATE cascade
        ON DELETE cascade
);

DROP TABLE IF EXISTS flightBookings;
CREATE TABLE IF NOT EXISTS flightBookings
(
    id            INTEGER UNIQUE NOT NULL,
    traveler_id   INTEGER        NOT NULL,
    flight_number INTEGER   NOT NULL,
    trip_id       INTEGER        NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (traveler_id) REFERENCES travelers (id)
        ON UPDATE cascade
        ON DELETE cascade,
    FOREIGN KEY (trip_id) REFERENCES trips (id)
        ON UPDATE cascade
        ON DELETE cascade,
    FOREIGN KEY (flight_number) REFERENCES flights (number)
        ON UPDATE cascade
        ON DELETE cascade
);

DROP TABLE IF EXISTS dealAdministrators;
CREATE TABLE IF NOT EXISTS dealAdministrators
(
    id         INTEGER UNIQUE      NOT NULL,
    username   VARCHAR(255) UNIQUE NOT NULL,
    password   VARCHAR(255)        NOT NULL,
    first_name VARCHAR(255)        NOT NULL,
    last_name  VARCHAR(255)        NOT NULL,
    hotel_name VARCHAR(255)        NOT NULL,

    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS hotels;
CREATE TABLE IF NOT EXISTS hotels
(
    id            INTEGER UNIQUE NOT NULL,
    name          VARCHAR(255)   NOT NULL,
    number_rooms  INTEGER        NOT NULL,
    amenities     VARCHAR(255)   NOT NULL,
    street_number INTEGER        NOT NULL,
    street        VARCHAR(255)   NOT NULL,
    city          VARCHAR(255)   NOT NULL,
    country       VARCHAR(255)   NOT NULL,

    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS hotelBookings;
CREATE TABLE IF NOT EXISTS hotelBookings
(
    id          INTEGER UNIQUE NOT NULL,
    trip_id     INTEGER        NOT NULL,
    traveler_id INTEGER        NOT NULL,
    hotel_id    INTEGER        NOT NULL,
    start       DATE           NOT NULL,
    end         DATE           NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (trip_id) REFERENCES trips (id)
        ON UPDATE cascade
        ON DELETE cascade,
    FOREIGN KEY (traveler_id) REFERENCES travelers (id)
        ON UPDATE cascade
        ON DELETE cascade,
    FOREIGN KEY (hotel_id) REFERENCES hotels (id)
        ON UPDATE cascade
        ON DELETE cascade
);

DROP TABLE IF EXISTS favHotels;
CREATE TABLE IF NOT EXISTS favHotels
(
    traveler_id INTEGER NOT NULL,
    hotel_id    INTEGER NOT NULL,

    PRIMARY KEY (traveler_id, hotel_id),
    FOREIGN KEY (traveler_id) REFERENCES travelers (id)
        ON UPDATE cascade
        ON DELETE cascade,
    FOREIGN KEY (hotel_id) REFERENCES hotels (id)
        ON UPDATE cascade
        ON DELETE cascade
);

DROP TABLE IF EXISTS dealInfo;
CREATE TABLE IF NOT EXISTS dealInfo
(
    id          INTEGER UNIQUE NOT NULL,
    date        DATE           NOT NULL,
    hotel_name  VARCHAR(255)   NOT NULL,
    hotel_id    INTEGER        NOT NULL,
    name        VARCHAR(255)   NOT NULL,
    description VARCHAR(255)   NOT NULL,
    admin_id    INTEGER        NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (admin_id) REFERENCES dealAdministrators (id)
        ON UPDATE cascade
        ON DELETE cascade,
    FOREIGN KEY (hotel_id) REFERENCES hotels (id)
        ON UPDATE cascade
        ON DELETE cascade
);

DROP TABLE IF EXISTS dealImpressions;
CREATE TABLE IF NOT EXISTS dealImpressions
(
    id          INTEGER UNIQUE NOT NULL,
    date        DATE           NOT NULL,
    time        TIME           NOT NULL,
    clicked     BOOLEAN        NOT NULL,
    deal_id     INTEGER        NOT NULL,
    traveler_id INTEGER        NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (deal_id) REFERENCES dealInfo (id)
        ON UPDATE cascade
        ON DELETE cascade,
    FOREIGN KEY (traveler_id) REFERENCES travelers (id)
        ON UPDATE cascade
        ON DELETE cascade
);

DROP TABLE IF EXISTS advertisers;
CREATE TABLE IF NOT EXISTS advertisers
(
    id         INTEGER UNIQUE      NOT NULL,
    username   VARCHAR(255) UNIQUE NOT NULL,
    password   VARCHAR(255)        NOT NULL,
    company    VARCHAR(255)        NOT NULL,
    first_name VARCHAR(255)        NOT NULL,
    last_name  VARCHAR(255)        NOT NULL,

    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS adInfo;
CREATE TABLE IF NOT EXISTS adInfo
(
    id            INTEGER UNIQUE NOT NULL,
    date          DATE           NOT NULL,
    advertiser_id INTEGER        NOT NULL,
    description   VARCHAR(255)        NOT NULL,
    price         DECIMAL(2)     NOT NULL,
    title         VARCHAR(255)   NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (advertiser_id) REFERENCES advertisers (id)
        ON UPDATE cascade
        ON DELETE cascade
);

DROP TABLE IF EXISTS adImpressions;
CREATE TABLE IF NOT EXISTS adImpressions
(
    id          INTEGER UNIQUE NOT NULL,
    date        DATE           NOT NULL,
    time        TIME           NOT NULL,
    clicked     BOOLEAN        NOT NULL,
    ad_id       INTEGER        NOT NULL,
    traveler_id INTEGER        NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (ad_id) REFERENCES adInfo (id)
        ON UPDATE cascade
        ON DELETE cascade,
    FOREIGN KEY (traveler_id) REFERENCES travelers (id)
        ON UPDATE cascade
        ON DELETE cascade
);

DROP TABLE IF EXISTS main_df;
CREATE TABLE IF NOT EXISTS main_df
(
    num                 BIGINT,
    Unnamed             BIGINT,
    city_origin          VARCHAR(255),
    city_destination    VARCHAR(255),
    destination_country VARCHAR(255),
    quarter             VARCHAR(255),
    hotel_rating        DOUBLE,
    hotel_price         DOUBLE,
    flight_price        DOUBLE,
    gdp                 DOUBLE,
    city_origin_Madrid INT,
    city_origin_Paris INT,
    city_origin_Rome INT,
    city_destination_Madrid INT,
    city_destination_Paris INT,
    city_destination_Rome INT,
    quarter_Q2 INT,
    quarter_Q3 INT,
    quarter_Q4 INT,

    PRIMARY KEY (num)
);

DROP TABLE IF EXISTS hotel_params;
CREATE TABLE IF NOT EXISTS hotel_params
(
    row_num INT NOT NULL,
    intercept          FLOAT,
    slope1          FLOAT,
    slope2          FLOAT,
    slope3          FLOAT,
    slope4         FLOAT,
    slope5          FLOAT,
    slope6         FLOAT,
    slope7          FLOAT,
    slope8          FLOAT,
    slope9          FLOAT,
    slope10          FLOAT,
    slope11          FLOAT,
    slope12         FLOAT,

    PRIMARY KEY (row_num)
);

DROP TABLE IF EXISTS flight_params;
CREATE TABLE IF NOT EXISTS flight_params
(
    row_num INT NOT NULL,
    intercept          FLOAT,
    slope1          FLOAT,
    slope2          FLOAT,
    slope3          FLOAT,
    slope4         FLOAT,
    slope5          FLOAT,
    slope6         FLOAT,
    slope7          FLOAT,
    slope8          FLOAT,
    slope9          FLOAT,
    slope10          FLOAT,
    slope11          FLOAT,
    slope12         FLOAT,

    PRIMARY KEY (row_num)
);