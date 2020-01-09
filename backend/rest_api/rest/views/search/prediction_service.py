from sqlalchemy import text
from rest.connect_db import db
from flask import request, jsonify, session
from datetime import datetime


def search(listing_id,prediction_type, page, count):
    results = []
    row_count = 0
    try:
        cursor = db.cursor()
        sql = "SELECT "
        if page is not None and count is not None:
            sql += " SQL_CALC_FOUND_ROWS "

        if prediction_type is not None and prediction_type == 'sentiment':
            sql += " * FROM listings_sentiment"
        elif prediction_type is not None and prediction_type == 'price':
            sql += " * FROM calendar_predicted"
        else:
            return

        sql += " WHERE 1=1 "
        parameter_tuple = ()

        sql += " AND listing_id=%s;"
        parameter_tuple += (listing_id,)

        cursor.execute(sql, parameter_tuple)
        columns = cursor.description

        results = []
        for value in cursor.fetchall():
            tmp = {}
            for (index, column) in enumerate(value):
                    tmp[columns[index][0]] = str(value.get(column))
            results.append(tmp)

        if page is not None and count is not None:
            cursor.execute("SELECT FOUND_ROWS();")
            row_count = cursor.fetchone().get('FOUND_ROWS()')
    except:
        print("Error: fail to fetch tables from db")

    return results, row_count
