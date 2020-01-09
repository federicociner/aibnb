from sqlalchemy import text
from rest.connect_db import db
from flask import request, jsonify, session
from datetime import datetime


def search(country, neighborhood, page, count, start_at, end_at, listing_id):
    results = []
    row_count = 0
    try:
        cursor = db.cursor()
        sql = "SELECT "
        if page is not None and count is not None:
            sql += " SQL_CALC_FOUND_ROWS "

        sql += " ls.latitude,ls.longitude,ls.listing_id,ls.price,ls.beds," \
               "ls.bathrooms,ls.room_type,ls.availability_30,ls.availability_60, " \
               "ls.availability_90,ls.availability_365, " \
               "lss.compound," \
               "lss.positive,lss.negative,lss.neutral "
        if start_at is not None:
            "c.date,"

        sql += "FROM listings ls " \
               "LEFT JOIN listings_sentiment lss ON  ls.listing_id=lss.listing_id "

        if start_at is not None:
            sql += "LEFT JOIN calendar c ON c.listing_id=ls.listing_id "

        sql += "WHERE 1=1 "
        parameter_tuple = ()

        if listing_id is not None:
            sql += " AND ls.listing_id= %s;"
            parameter_tuple += (int(listing_id),)
        else:
            if start_at is not None:
                start_at_value = int(start_at)/1000.0
                if end_at is not None:
                    end_at_value = int(start_at) / 1000.0
                    sql += " AND c.date BETWEEN %s AND %s "
                    parameter_tuple += (datetime.fromtimestamp(start_at_value).strftime('%Y-%m-%d %H:%M:%S'),
                                        datetime.fromtimestamp(end_at_value).strftime('%Y-%m-%d %H:%M:%S'),)
                else:
                    sql += " AND c.date >= %s "
                    parameter_tuple += (datetime.fromtimestamp(start_at_value).strftime('%Y-%m-%d %H:%M:%S'),)
            if country is not None:
                sql += " AND country LIKE %s "
                parameter_tuple += ("%" + country + "%",)

            if neighborhood is not None:
                sql += " AND neighbourhood_cleansed LIKE %s "
                parameter_tuple += ("%" + neighborhood + "%",)
            if page is not None and count is not None:
                sql += "limit %s offset %s;"

                parameter_tuple += (int(count), (int(page) - 1) * int(count),)
            else:
                sql += ";"

        cursor.execute(sql, parameter_tuple)
        columns = cursor.description

        results = []
        for value in cursor.fetchall():
            tmp = {}
            tmp['stats'] = {}
            for (index, column) in enumerate(value):
                if column != 'room_type' and column != 'availability_30' and column != 'availability_60'and column != 'availability_90' and column != 'availability_365':
                    tmp[columns[index][0]] = str(value.get(column))
                else:
                    tmp['stats'][column] = str(value.get(column))
            results.append(tmp)

        if page is not None and count is not None:
            cursor.execute("SELECT FOUND_ROWS();")
            row_count = cursor.fetchone().get('FOUND_ROWS()')
    except:
        print("Error: fail to fetch tables from db")
    return results, row_count

def getStates(country):
    results = []
    row_count = 0
    try:
        cursor = db.cursor()
        sql =  '''SELECT DISTINCT state FROM listings WHERE listings.country="%s"''' % country
        cursor.execute(sql)
        results = cursor.fetchall()

    except:
        print("Error Getting States")

    return results, row_count

def getNeighborhoods(state):
    results = []
    row_count = 0
    try:
        cursor = db.cursor()
        sql =  '''SELECT DISTINCT neighbourhood_cleansed FROM listings WHERE listings.state="%s"''' % state
        cursor.execute(sql)
        results = cursor.fetchall()

    except:
        print("Error Getting Neighborhoods")

    return results, row_count

def getAllListings(country, state, neighborhood, bds, bths, date):
    results = []
    row_count = 0
    try:
        cursor = db.cursor()
        sql =  '''SELECT DISTINCT ls.listing_id, latitude, longitude, CAST(CAST(cp.predicted_price AS DECIMAL(10,2)) as char) as price, bedrooms, bathrooms, room_type, availability_365, city, state, zipcode, accommodates, compound, number_of_reviews, review_scores_rating, property_type
                  FROM listings ls
                  LEFT JOIN listings_sentiment lss 
                  ON  ls.listing_id=lss.listing_id
                  LEFT JOIN calendar_predicted cp
                  ON  cp.listing_id=ls.listing_id
                   
                  WHERE country='%s' AND state='%s' AND neighbourhood_cleansed='%s' AND bedrooms='%s' AND bathrooms='%s' AND cp.date='%s';''' % (country, state, neighborhood, bds, bths, str(datetime.fromtimestamp(int(date)/1000).strftime('%Y-%m-%d')))
        cursor.execute(sql)
        print(sql)
        results = cursor.fetchall()
    except Exception as e:
        print(e)
        print("Error Getting Listings")

    return results, row_count

def getListingById(listing_id):
    results = []
    row_count = 0
    try:
        cursor = db.cursor()
        sql =  '''SELECT ls.listing_id, latitude, longitude, price, beds, bathrooms, room_type, availability_365, compound,
               lss.positive, negative, neutral, neighbourhood_cleansed FROM  listings ls 
               LEFT JOIN listings_sentiment lss 
               ON  ls.listing_id=lss.listing_id 
               WHERE ls.listing_id="%s"''' % listing_id
        cursor.execute(sql)
        results = cursor.fetchall()

    except:
        print("Error Getting Listings")

    return results, row_count
