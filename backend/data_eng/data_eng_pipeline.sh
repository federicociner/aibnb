#!/usr/bin/env bash


#Collection
./listings/collect.py
./reviews/collect.py
./calendar/collect.py

# Cleaning
./listings/clean.py
./reviews/clean.py
./calendar/clean.py

# Integration
./listings/integrate.sh
./reviews/integrate.sh
./calendar/integrate.sh
