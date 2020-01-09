touch /data/listings.csv

fields="listing_id,host_id,host_response_rate,host_acceptance_rate,host_is_superhost,host_listings_count,host_total_listings_count,host_identity_verified,neighbourhood_cleansed,calculated_host_listings_count,city,state,zipcode,country,latitude,longitude,property_type,room_type,accommodates,bathrooms,bedrooms,beds,price,availability_30,availability_60,availability_90,availability_365,number_of_reviews,review_scores_rating,reviews_per_month"

#hostname=aibnbdb.c9v9a7trklsr.us-east-1.rds.amazonaws.com

echo $fields > /data/listings.csv
# merge the csv files
for filename in $(ls /data/*listings.csv.gz_0.csv); do sed 1d $filename >> /data/listings.csv; done

# load to mysql

#/usr/bin/mysqlimport --port=3306 --host=$hostname --fields-terminated-by=',' --lines-terminated-by='\n' --columns=$fields --local  --force  -v --default-character-set=utf8 -u root -p  airbnb ./listings.csv

./listings/2mysql.py
