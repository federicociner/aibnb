#!/usr/bin/env bash


/usr/bin/mysqlimport --port=3306 --host=aibnbdb.c9v9a7trklsr.us-east-1.rds.amazonaws.com --fields-terminated-by=',' --lines-terminated-by='\n' --columns='listing_id,id,date,reviewer_id,reviewer_name,comments' --local  --force  -u aibnb -p  aibnb /data/reviews.csv
