# -*- coding: utf-8 -*-

from sklearn.metrics import mean_squared_error
from dotenv import load_dotenv
from pathlib import Path
import os
import sqlalchemy as sa
import pandas as pd
import pickle
import math


def save_dataset(df, filename, sep=',', subdir='data'):
    tdir = os.path.join(os.getcwd(), os.pardir, subdir, filename)
    df.to_csv(path_or_buf=tdir, sep=sep, header=True, index=False)


def get_abspath(filename, filepath):
    p = os.path.abspath(os.path.join(os.curdir))
    filepath = os.path.join(p, filepath, filename)

    return filepath


def ensure_dir_exists(filepath):
    directory = os.path.dirname(filepath)
    os.makedirs(directory, exist_ok=True)


def save_pickled_model(model, filepath):
    with open(filepath, 'wb+') as model_file:
        pickler = pickle.Pickler(model_file)
        pickler.dump(model)


def load_pickled_model(filepath):
    with open(filepath, 'rb+') as model_file:
        model = pickle.load(model_file)

    return model


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


def rmse(y_true, y_pred):
    return math.sqrt(mean_squared_error(y_true, y_pred))
