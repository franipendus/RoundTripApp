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

DROP TABLE IF EXISTS gdp;
CREATE TABLE gdp
(
    num     BIGINT        NOT NULL,
    country VARCHAR(50) NOT NULL,
    gdp     DOUBLE        NOT NULL,
    quarter VARCHAR(1024) NOT NULL,

    PRIMARY KEY (num)
);

DROP TABLE IF EXISTS exchangeRates;
CREATE TABLE IF NOT EXISTS exchangeRates
(
    name_to       VARCHAR(255)  NOT NULL,
    name_from     VARCHAR(255)  NOT NULL,
    exchange_rate FLOAT               NOT NULL,

    PRIMARY KEY (name_to, name_from),
    FOREIGN KEY (name_to) REFERENCES countries (name)
        ON UPDATE cascade
        ON DELETE cascade,
    FOREIGN KEY (name_from) REFERENCES countries (name)
        ON UPDATE cascade
        ON DELETE cascade
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
    clicks        INTEGER        NOT NULL,
    price         DECIMAL(2)     NOT NULL,
    image_name    VARCHAR(255)   NOT NULL,

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

DROP TABLE IF EXISTS hotelStats;
CREATE TABLE hotelStats (
  num BIGINT,
  avg_price DOUBLE NOT NULL,
  avg_rating DOUBLE NOT NULL,
  month VARCHAR(1024) NOT NULL,
  city VARCHAR(1024) NOT NULL,
  country VARCHAR(1024) NOT NULL,
  quarter VARCHAR(1024) NOT NULL,

    PRIMARY KEY (num)
);