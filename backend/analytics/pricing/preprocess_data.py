# -*- coding: utf-8 -*-

from utils import db_config, db_conn, db_table
from mysql.connector.errors import Error


def execute_sql(conn, sql_file):
    # Read SQL file
    with open(sql_file, 'r') as f:
        sql_file = f.read()

    # Parse commands and execute on target DB
    sql_commands = [l.replace('\n', ' ').strip() for l in sql_file.split(';')]
    for command in sql_commands:
        try:
            conn.execute(command)
        except Error as e:
            print('Something went wrong: {}'.format(e))


def preprocess_features(conn, with_sa=True):
    """Cleans and returns AIBNB features. Uses one-hot encoding for
    categorical features.

    """
    features = db_table(conn, 'SELECT * FROM features')

    # Drop entity columns
    features.drop(columns=['listing_id', 'full_date'], inplace=True)

    # Drop sentiment score features if with_sa option is set to False
    if not with_sa:
        sa_features = ['compound', 'positive', 'neutral', 'negative']
        features.drop(columns=sa_features, inplace=True)

    return features


def preprocess_calendar_features(conn, limit, offset):
    """Cleans and returns AIBNB calendar features to be used for scoring. Uses
    one-hot encoding for categorical features.

    """
    sql = '''SELECT * FROM calendar_features
             LIMIT {0} OFFSET {1}'''.format(limit, offset)
    features = db_table(conn, sql)

    # Split out entity columns and drop from features
    entity_cols = ['listing_id', 'date', 'available', 'actual_price']
    entities = features[entity_cols]
    features.drop(columns=entity_cols, inplace=True)

    return entities, features


if __name__ == '__main__':
    # Get DB connection
    config = db_config()
    conn = db_conn(config)

    # Generate features table in the AIBNB DB
    execute_sql(conn, sql_file='sql/generate_features.sql')
