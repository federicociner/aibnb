#!/bin/bash

# WARNING: This script will fail if you do not have the necessary Python packages installed

# Run initial setup script
python initial_setup.py

# Run main script to generate sentiment analysis scores and write to DB on AWS
python sentiment_analysis.py