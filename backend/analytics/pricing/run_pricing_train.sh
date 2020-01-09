#!/bin/bash

# WARNING: This script will fail if you do not have the necessary Python packages installed

# Generate features
python preprocess_data.py

# Train models
python train_model.py

# Evaluate models
python evaluate_model.py