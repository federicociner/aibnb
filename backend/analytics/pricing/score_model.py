# -*- coding: utf-8 -*-

from utils import db_config, db_conn, db_table, load_pickled_model, write_to_db
from preprocess_data import execute_sql, preprocess_calendar_features
from sqlalchemy.dialects.mysql import INTEGER, FLOAT, VARCHAR, DATE
import math


def write_scores(conn, entities, scores):
    # Get data types for output table
    dtypes = {'listing_id': INTEGER,
              'date': DATE,
              'available': VARCHAR(length=10),
              'actual_price': FLOAT,
              'predicted_price': FLOAT}

    # Concatenate entity and score columns
    entities['predicted_price'] = scores

    # Write data frame to DB
    name = 'calendar_predicted'
    write_to_db(conn, entities, name, dtypes, if_exists='append')


def batch_scoring(conn, tbl_size, rows=1000000):
    # Load model trained with sentiment score features
    model = load_pickled_model('models/xgb_a.model')

    # Score listings and write to MySQL DB in batches
    batches = math.ceil(tbl_size / rows)
    for i in range(0, batches):
        entities, features = preprocess_calendar_features(conn, rows, i * rows)
        scores = model.predict(features.values)
        write_scores(conn, entities, scores)


if __name__ == '__main__':
    # Get DB connection
    config = db_config()
    conn = db_conn(config)

    # Generate calendar features to be used for scoring the final model
    execute_sql(conn, sql_file='sql/generate_calendar_features.sql')

    # Get table size to determine batch scoring strategy
    tbl_size = db_table(conn, 'SELECT COUNT(*) FROM calendar_features')

    # Score model
    batch_scoring(conn, tbl_size=int(tbl_size.iloc[0]))
