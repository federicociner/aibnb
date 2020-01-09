# AIBNB: Sentiment Analysis and Price Prediction

## Overview

The "pricing" and "sentiment" modules contains the necessary code to perform the following steps:

* Generate sentiment scores for each listing in the "aibnb.listings" table that has a corresponding set of reviews in the "aibnb.reviews" table, and write the outputs to the "aibnb.listings_sentiment" table in the DB

* Train an XGBoost regression model to predict the price of a listing on a given date.

* Run experiments and produce graphs to compare the peformance of the XGboost model using the sentiment scores as additional features vs not using the sentiment scores.

* Use the XGBoost pricing model to predict rental prices for a set of listing IDs across various dates.

## Instructions

The instructions below assume the following pre-requisite steps have been followed:

1. Create a Python 3.6 virtual environment using virtualenv or similar tool.

2. Set your working directory to "backend/analytics" and install all required packages by running "pip install -r requirements.txt".

### Step 1 - Generate sentiment scores

1. Set your current working directory to the "backend/analytics/sentiment" folder by running "cd backend/analytics/sentiment."

2. Execute the "run_sa.sh" script to generate the sentiment scores table in the AIBNB database. This script will run the following sequence of steps:
    a. Runs the "initial_setup.py" file to install any required NLTK dependencies (e.g. stopwords).
    b. Runs the "main.py" file.

3. Once the Shell script has executed successfully, check that the "aibnb.listings_sentiment" table was created in the DB and that it was populated with data

### Step 2 - Train and score pricing model

1. Set your current working directory to the "backend/analytics/pricing" folder by running "cd backend/analytics/pricing."

2. Execute the "run_pricing_train.sh" script to generate and pre-process features, train two XGBoost models (one with sentiment score features and one without) and plot graphs for experiments. This script will run the following sequence of steps:
    a. Runs the "preprocess_data.py" file, which generates a cleaned up feature set on the AIBNB database. This feature set requires further pre-processing, which is handled in subsequent Python scripts.
    b. Runs the "train_model.py" file, which trains two XGBoost models and saves the model binaries to the local filesystem. It will create the "<working_dir>/models" directory if it does not exist.
    c. Runs the "evaluate_model.py" file, which generates various graphs comparing the performance of the two models across a variety of metrics. This script will create the following folders and subfolders:
        <working_dir>/graphs/{linear, lasso, ridge, xgb_a, xgb_b}
        <working_dir>/outputs/{linear, lasso, ridge, xgb_a, xgb_b}

3. Execute the "run_pricing_score.sh" script to load the a pre-trained XGBoost model (based on outcomes from the experiments in step 2 above) and batch score all of the records in the "calendar" table. This script will run the following sequence of steps:
    a. Runs the "score_model.py" file, which loads a pre-defined XGBoost model and batch scores records from the "calendar_features" table. Once these scores have been generated, they are written back to the DB to the "calendar_predicted" table.