# -*- coding: utf-8 -*-

from dotenv import load_dotenv
from pathlib import Path
import os
import sqlalchemy as sa
import pandas as pd


def get_abspath(filename, filepath):
    p = os.path.abspath(os.path.join(os.curdir))
    filepath = os.path.join(p, filepath, filename)

    return filepath


def ensure_dir_exists(filepath):
    directory = os.path.dirname(filepath)
    os.makedirs(directory, exist_ok=True)


def db_config():
    env_path = Path('..') / '.env'
    load_dotenv(dotenv_path=env_path)

    return {
        'host': os.getenv('MYSQL_SERVER'),
        'db': os.getenv('MYSQL_DB'),
        'port': os.getenv('MYSQL_PORT'),
        'username': os.getenv('MYSQL_USERNAME'),
        'password': os.getenv('MYSQL_PASSWORD')
    }


def db_conn(config):
    conn = 'mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}'.format(
        config['username'],
        config['password'],
        config['host'],
        config['port'],
        config['db']
    )
    engine = sa.create_engine(conn)

    return engine.connect()


def db_table(conn, sql):
    result = conn.execute(sql)
    cursor = result.cursor
    cols = cursor.column_names
    table = cursor.fetchall()
    df = pd.DataFrame(table)
    df.columns = cols

    return df


def write_to_db(conn, df, name, dtypes, if_exists='replace'):
    df.to_sql(name, conn, if_exists=if_exists, index=False, dtype=dtypes)
