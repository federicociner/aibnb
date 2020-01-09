# -*- coding: utf-8 -*-

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import make_scorer
from xgboost import XGBRegressor
from preprocess_data import preprocess_features
from utils import (
    db_config,
    db_conn,
    get_abspath,
    ensure_dir_exists,
    save_pickled_model,
    rmse)
import numpy as np


def _generate_param_grid(model_type):
    param_grid = {
        'xgb': {
            'n_estimators': [100, 200],
            'max_depth': [3, 6, 12],
            'learning_rate': [0.01, 0.1, 1.0]
        },
        'linear': {
            'fit_intercept': [True, False],
            'normalize': [True, False]
        },
        'ridge': {
            'fit_intercept': [True],
            'alpha': np.arange(0, 1, 0.01)
        },
        'lasso': {
            'fit_intercept': [True],
            'alpha': np.arange(0, 1, 0.01)
        }
    }

    return param_grid[model_type]


def split_data(features, test_size=0.3, seed=42):
    # Convert data frame to Numpy array and split X and y
    X_data = features.drop(columns='label').values
    y_data = features['label'].values

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X_data,
        y_data,
        test_size=test_size,
        random_state=seed
    )

    return X_train, X_test, y_train, y_test


def train_model(
    model_object,
    model_type,
    X_train,
    y_train,
    score_function,
    n_jobs=-1,
    cv=3
):
    # Get parameter grid
    param_grid = _generate_param_grid(model_type)

    # Run GridSearch using pre-defined parameter grid
    grid = GridSearchCV(
        model_object,
        cv=cv,
        n_jobs=n_jobs,
        param_grid=param_grid,
        scoring=score_function
    )
    grid.fit(X_train, y_train)

    return grid


def main():
    config = db_config()
    conn = db_conn(config)

    # Create scorer to train models using RMSE
    scorer = make_scorer(rmse, greater_is_better=False)

    # Load features
    features_a = preprocess_features(conn)
    features_b = preprocess_features(conn, with_sa=False)

    # Get train and test sets for both feature sets
    X_train_a, X_test_a, y_train_a, y_test_a = split_data(features_a)
    X_train_b, X_test_b, y_train_b, y_test_b = split_data(features_b)

    # Train regression models with sentiment score features
    modelpath = 'models'
    linear_models = {
        'linear': LinearRegression(),
        'ridge': Ridge(),
        'lasso': Lasso()
    }

    for name, model in linear_models.items():
        grid = train_model(
            model_object=model,
            model_type=name,
            X_train=X_train_a,
            y_train=y_train_a,
            score_function=scorer,
            cv=3
        )
        filename = get_abspath('{}.model'.format(name), modelpath)
        ensure_dir_exists(filename)
        save_pickled_model(grid, filename)

    # Train XGBoost model with sentiment score features
    xgb = XGBRegressor(objective='reg:linear')
    grid = train_model(
        model_object=xgb,
        model_type='xgb',
        X_train=X_train_a,
        y_train=y_train_a,
        score_function=scorer,
        cv=3
    )
    filename = get_abspath('xgb_a.model', modelpath)
    save_pickled_model(grid, filename)

    # Train XGBoost model without sentiment score features
    grid = train_model(
        model_object=xgb,
        model_type='xgb',
        X_train=X_train_b,
        y_train=y_train_b,
        score_function=scorer,
        cv=3
    )
    filename = get_abspath('xgb_b.model', modelpath)
    save_pickled_model(grid, filename)


if __name__ == '__main__':
    main()
