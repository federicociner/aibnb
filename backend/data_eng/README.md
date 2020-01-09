# Data Engineering Module

## Overview

This  module contains  code to perform the following tasks:

* Collect listings, review and calendar datasets from www.insideairbnb.com.
* Clean the data by removing invalid records, duplicates, and invalid string characters
* Import the data to a relational database on AWS.
* Publish the data via a REST API


## Instructions

The instructions below assume the following pre-requisites have been met:

1. Create a Python 3.6 virtual environment using `virtualenv` or similar tool.
2. Install all required packages by running `pip install -r requirements.txt` in the `data_eng`  and `rest_api` root folders.

### Step 1 - Collect, clean, and import data to Database

 Execute  `data_eng_pipeline.sh`  in the data_eng root folder. This script will perform the following tasks in sequence :

a) Collection
  ./listings/collect.py
  ./reviews/collect.py
  ./calendar/collect.py

b) Cleaning
  ./listings/clean.py
  ./reviews/clean.py
  ./calendar/clean.py

c) Import data to Database
  ./listings/integrate.sh
  ./reviews/integrate.sh
  ./calendar/integrate.sh

### Step 2 - Deploy REST API

Execute `python run.py`  in the rest_api root folder to run the REST API. Please see the  README.md in the same folder for the user-guide.
