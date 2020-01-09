# -*- coding: utf-8 -*-

from sklearn.metrics import make_scorer, r2_score
from sklearn.model_selection import (
    learning_curve,
    StratifiedShuffleSplit,
    validation_curve
)
from preprocess_data import preprocess_features
from train_model import split_data
from utils import (
    db_config,
    db_conn,
    get_abspath,
    ensure_dir_exists,
    load_pickled_model,
    rmse)
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def basic_results(grid, X_test, y_test, model_name):
    # Get best score, test score, scoring function and best parameters
    bs = grid.best_score_
    ts = grid.score(X_test, y_test)
    sf = grid.scorer_
    bp = grid.best_params_

    # Calculate R^2
    y_pred = grid.predict(X_test)
    r2 = r2_score(y_test, y_pred)

    # Write results to a combined results file
    resfile = get_abspath('basic_results.csv', 'outputs')
    ensure_dir_exists(resfile)
    with open(resfile, 'a') as f:
        f.write('{0},{1},{2},"{3}","{4}",{5}\n'.format(
            model_name, bs, ts, sf, bp, r2)
        )


def create_learning_curve(
    estimator,
    scorer,
    X_train,
    y_train,
    model_name,
    cv=3,
    save_file=True
):
    # Set training sizes and intervals
    train_sizes = np.arange(0.01, 1.0, 0.05)

    # Set cross validation strategy to use StratifiedShuffleSplit
    cv_strategy = StratifiedShuffleSplit(n_splits=cv, random_state=0)

    # Create learning curve object
    LC = learning_curve(
        estimator,
        X_train,
        y_train,
        cv=cv_strategy,
        train_sizes=train_sizes,
        scoring=scorer,
        n_jobs=-1
    )

    # Extract training and test scores as data frames
    train_scores = pd.DataFrame(index=LC[0], data=LC[1])
    test_scores = pd.DataFrame(index=LC[0], data=LC[2])

    # Save data frames to CSV
    if save_file:
        res_tgt = '{0}/{1}'.format('outputs', model_name)
        train_file = get_abspath('{}_LC_train.csv'.format(model_name), res_tgt)
        test_file = get_abspath('{}_LC_test.csv'.format(model_name), res_tgt)
        ensure_dir_exists(train_file)
        train_scores.to_csv(train_file, index=False)
        test_scores.to_csv(test_file, index=False)

    return train_scores, test_scores


def plot_learning_curve(model_name, train_scores, test_scores):
    # Set training sizes and intervals
    train_sizes = np.arange(0.01, 1.0, 0.05)

    # Create learning curve plot
    fig, ax = plt.subplots()
    ax.plot(train_sizes, np.mean(train_scores, axis=1),
            marker='.', color='b', label='Training score')
    ax.plot(train_sizes, np.mean(test_scores, axis=1),
            marker='.', color='g', label='Cross-validation score')
    ax.legend(loc='best')
    ax.grid(linestyle='dotted')
    ax.set_title('Learning curve - {} model'.format(model_name))
    ax.set_xlabel('Samples used for training as a percentage of total')
    ax.set_ylabel('RMSE (Negative)')

    # Save learning curve plot as PNG
    plot_tgt = '{0}/{1}'.format('graphs', model_name)
    plotpath = get_abspath('{}_LC.png'.format(model_name), plot_tgt)
    ensure_dir_exists(plotpath)
    plt.tight_layout(pad=1.0)
    plt.savefig(plotpath)
    plt.close()


def create_validation_curve(
    estimator,
    X_train,
    y_train,
    model_name,
    param_name,
    param_range,
    scorer
):
    # Generate validation curve results
    train_scores, test_scores = validation_curve(
        estimator,
        X_train,
        y_train,
        param_name=param_name,
        param_range=param_range,
        cv=3,
        scoring=scorer,
        n_jobs=-1
    )

    # Generate validation curve plot
    fig, ax = plt.subplots()
    ax.plot(param_range, np.mean(train_scores, axis=1),
            marker='.', color='b', label='Train Score')
    ax.plot(param_range, np.mean(test_scores, axis=1),
            marker='.', color='g', label='Cross-validation Score')
    ax.legend(loc='best')
    ax.grid(linestyle='dotted')
    ax.set_title('Validation curve - {} model'.format(model_name))
    ax.set_xlabel(param_name)
    ax.set_ylabel('RMSE (Negative)')

    # Save validation curve plot as PNG
    plot_tgt = '{0}/{1}'.format('graphs', model_name)
    plotpath = get_abspath('{}_VC.png'.format(model_name), plot_tgt)
    ensure_dir_exists(plotpath)
    plt.tight_layout(pad=1.0)
    plt.savefig(plotpath)
    plt.close()


def get_feature_importances(model_name, grid, features, save_file=True):
    # Get feature importance values
    feat_importance = pd.Series(
        grid.best_estimator_
        .get_booster()
        .get_fscore()).sort_values(ascending=False)

    # Get feature names
    feat_idxs = [i.strip('f') for i in feat_importance.keys()]
    feat_names = list(features.columns.values)
    feats = [x for _, x in sorted(zip(feat_idxs, feat_names))]

    # Add feature names
    df = feat_importance.to_frame(name='f_score')
    df.reset_index(drop=True, inplace=True)
    df['name'] = feats

    # Save feature importance to CSV
    if save_file:
        file_tgt = '{0}/{1}'.format('outputs', model_name)
        feats_file = get_abspath('{}_FI.csv'.format(model_name), file_tgt)
        df.to_csv(feats_file, index=False)

    return df


def plot_feature_importances(model_name, feature_importances, nfeats=10):
    # Subset feature importances data frame
    subset = feature_importances.iloc[:nfeats, :]

    # Generate feature importance plot
    fig, ax = plt.subplots()
    sns.barplot(
        x='f_score',
        y='name',
        data=subset,
        ax=ax,
        palette=sns.color_palette('YlGnBu_r', n_colors=15),
        dodge=False)
    ax.tick_params(labelsize=8)
    ax.set_ylabel('')
    ax.set_xlabel('F score')
    ax.set_title('Feature importances - {} model'.format(model_name))

    # Save feature importance plot as PNG
    plot_tgt = '{0}/{1}'.format('graphs', model_name)
    plotpath = get_abspath('{}_FI.png'.format(model_name), plot_tgt)
    ensure_dir_exists(plotpath)
    plt.tight_layout(pad=1.0)
    plt.savefig(plotpath)
    plt.close()


def plot_lc_all():
    # Load test set learning curve values
    scores = {}
    models = ['linear', 'ridge', 'lasso', 'xgb_a']
    colors = ['green', 'c', 'orangered', 'mediumslateblue', 'saddlebrown']
    for i in range(0, len(models)):
        filepath = get_abspath(
            '{0}/{0}_LC_test.csv'.format(models[i]), 'outputs')
        scores[models[i]] = (np.mean(pd.read_csv(filepath), axis=1), colors[i])

    # Set training sizes and intervals
    train_sizes = np.arange(0.01, 1.0, 0.05)

    # Create learning curve plot
    fig, ax = plt.subplots()
    for k, v in scores.items():
        ax.plot(train_sizes, v[0], marker='.', color=v[1], label=k)
    ax.legend(loc='best')
    ax.grid(linestyle='dotted')
    ax.set_title('Learning curves - test score comparison')
    ax.set_xlabel('Samples used for training as a percentage of total')
    ax.set_ylabel('RMSE (Negative)')

    # Save learning curve plot as PNG
    plotpath = get_abspath('models_LC.png', 'graphs')
    ensure_dir_exists(plotpath)
    plt.tight_layout(pad=1.0)
    plt.savefig(plotpath)
    plt.close()


def main():
    config = db_config()
    conn = db_conn(config)

    # Remove basic results file
    try:
        combined = get_abspath('basic_results.csv', 'outputs')
        os.remove(combined)
    except IOError:
        pass

    # Load features
    features_a = preprocess_features(conn)
    features_b = preprocess_features(conn, with_sa=False)

    # Create scorer to train models using RMSE
    scorer = make_scorer(rmse, greater_is_better=False)

    # Load models in a dict
    models = {
        'linear': load_pickled_model('models/linear.model'),
        'ridge': load_pickled_model('models/ridge.model'),
        'lasso': load_pickled_model('models/lasso.model'),
        'xgb_a': load_pickled_model('models/xgb_a.model'),
        'xgb_b': load_pickled_model('models/xgb_b.model')
    }

    # Validation curve parameter names and ranges
    vc_params = {'xgb_a': ('max_depth', np.arange(1, 20, 1)),
                 'xgb_b': ('max_depth', np.arange(1, 20, 1))
                 }

    # Split into train and test sets
    X_train_a, X_test_a, y_train_a, y_test_a = split_data(features_a)
    X_train_b, X_test_b, y_train_b, y_test_b = split_data(features_b)

    # Generate basic results and learning curves for all models
    for name, grid in models.items():
        if name in ['linear', 'ridge', 'lasso']:
            basic_results(grid, X_test_a, y_test_a, name)
            train_scores, test_scores = create_learning_curve(
                grid.best_estimator_,
                scorer,
                X_train_a,
                y_train_a,
                model_name=name,
                cv=3
            )
            plot_learning_curve(name, train_scores, test_scores)
        if name == 'xgb_b':
            basic_results(grid, X_test_b, y_test_b, name)
            train_scores, test_scores = create_learning_curve(
                grid.best_estimator_,
                scorer,
                X_train_b,
                y_train_b,
                model_name=name,
                cv=3
            )
            plot_learning_curve(name, train_scores, test_scores)

    # Generate validation curves for XGBoost models
    create_validation_curve(
        models['xgb_a'].best_estimator_,
        X_train_a,
        y_train_a,
        model_name='xgb_a',
        param_name=vc_params['xgb_a'][0],
        param_range=vc_params['xgb_a'][1],
        scorer=scorer
    )

    create_validation_curve(
        models['xgb_b'].best_estimator_,
        X_train_b,
        y_train_b,
        model_name='xgb_b',
        param_name=vc_params['xgb_b'][0],
        param_range=vc_params['xgb_b'][1],
        scorer=scorer
    )

    # Generate XGBoost feature importance plots and results
    fi_a = get_feature_importances('xgb_a', models['xgb_a'], features_a)
    fi_b = get_feature_importances('xgb_b', models['xgb_b'], features_b)
    plot_feature_importances('xgb_a', fi_a, nfeats=15)
    plot_feature_importances('xgb_b', fi_b, nfeats=15)

    # Plot test set learning curves of all five models
    plot_lc_all()


if __name__ == '__main__':
    main()
