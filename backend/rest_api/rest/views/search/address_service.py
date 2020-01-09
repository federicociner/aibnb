from sqlalchemy import text
from rest.connect_db import db
from flask import request, jsonify, session
from datetime import datetime


def search(country, state, page, count):
    results = []
    row_count = 0
    try:
        cursor = db.cursor()
        sql = "SELECT "
        if page is not None and count is not None:
            sql += " SQL_CALC_FOUND_ROWS "

        if country is not None and state is not None:
            sql += " DISTINCT neighbourhood_cleansed FROM listings"
        elif country is not None:
            sql += " DISTINCT state FROM listings"
        elif state is not None:
            sql += " DISTINCT neighbourhood_cleansed FROM listings"

        sql += " WHERE 1=1 "
        parameter_tuple = ()

        if country is not None and state is not None:
            sql += " AND country LIKE %s AND state LIKE %s"
            parameter_tuple += (country,state,)
        elif country is not None:
            sql += " AND country LIKE %s"
            parameter_tuple += (country,)
        elif state is not None:
            sql += " AND state LIKE %s"
            parameter_tuple += (state,)
        sql += ";"

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
