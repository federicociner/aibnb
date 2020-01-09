#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import pandas as pd
#import MySQLdb as my
import mysql.connector as my

db = my.connect(host="aibnbdb.c9v9a7trklsr.us-east-1.rds.amazonaws.com",
user="aibnb",
passwd="cse6242aibnb",
db="aibnb"
)

cursor = db.cursor()

sql = "INSERT INTO airbnblistings(listing_id , host_id , host_response_rate, host_acceptance_rate, host_is_superhost, host_listings_count, host_total_listings_count, host_identity_verified, neighbourhood_cleansed, calculated_host_listings_count, city, state, zipcode, country, latitude, longitude, property_type, room_type, accommodates, bathrooms, bedrooms, beds, price, availability_30, availability_60, availability_90, availability_365, number_of_reviews, review_scores_rating, reviews_per_month) VALUES(%s, %s, %s, %s, %s, %s, %s, %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s,  %s)"

filename =  "/data/listings.csv"

def get_bin(r):
	if (r == 't'):
		return 1
	else:
		return 0

for chunk in pd.read_csv(filename, chunksize=1000):
	try:
		data =[]
		df = chunk
		#print(df.info())
		for i in range(0,len(df)):
			row = df.iloc[i,:]
			listing_id = row['listing_id']
			listing_id = int(listing_id)
			host_id = row['host_id']
			host_id = int(host_id)

			# clean host_response_rate
			host_response_rate = row['host_response_rate']
			host_response_rate = str(host_response_rate).replace("%",'')
			host_response_rate = host_response_rate.replace("nan",'0')
			host_response_rate = float(host_response_rate) / 100
			# clean host_acceptance_rate
			host_acceptance_rate = row['host_acceptance_rate']
			host_acceptance_rate = str(host_acceptance_rate).replace("%",'')
			host_acceptance_rate = host_acceptance_rate.replace("nan",'0')
			host_acceptance_rate = float(host_acceptance_rate) / 100
			# clean host_is_superhost
			host_is_superhost = row['host_is_superhost']
			host_is_superhost = get_bin(host_is_superhost)

			# clean host_listings_count
			host_listings_count = row['host_listings_count']
			host_listings_count = str(row['host_listings_count']).replace("nan",'0')
			host_listings_count = float(host_listings_count)

			host_total_listings_count = row['host_total_listings_count']
			host_total_listings_count = str(row['host_total_listings_count']).replace("nan",'0')
			host_total_listings_count = float(host_total_listings_count)


			host_identity_verified = row['host_identity_verified']
			host_identity_verified = get_bin(host_identity_verified)

			neighbourhood_cleansed = row['neighbourhood_cleansed']
			neighbourhood_cleansed = str(neighbourhood_cleansed).lower()
			neighbourhood_cleansed = neighbourhood_cleansed.replace("nan",'other')

			calculated_host_listings_count = row['calculated_host_listings_count']
			calculated_host_listings_count = str(calculated_host_listings_count).replace("nan",'0')
			calculated_host_listings_count = int(calculated_host_listings_count)

			city = row['city']
			city = str(city).lower()
			city = city.replace("nan",'other')

			state = row['state']
			state = str(state).lower()
			state = state.replace("nan",'other')

			zipcode = row['zipcode']
			zipcode = str(zipcode).lower()
			zipcode = zipcode.replace("nan",'other')

			country = row['country']
			country = str(country).lower()
			country = country.replace("nan",'other')


			latitude = row['latitude']
			latitude = str(row['latitude']).replace("nan",'0.00')
			latitude = float(latitude)

			longitude = row['longitude']
			longitude = str(row['longitude']).replace("nan",'0.00')
			longitude = float(longitude)


			property_type = row['property_type']
			property_type = str(property_type).lower()
			property_type = property_type.replace("&",'and')
			property_type = property_type.replace("nan",'other')


			room_type = row['room_type']
			room_type = str(room_type).lower()
			room_type = room_type.replace("/",'_')
			room_type = room_type.replace("nan",'other')


			accommodates = row['accommodates']
			accommodates = str(accommodates).replace("nan",'0')
			accommodates = int(accommodates)


			bathrooms = row['bathrooms']
			bathrooms = str(row['bathrooms']).replace("nan",'0.00')
			bathrooms = float(bathrooms)

			bedrooms = row['bedrooms']
			bedrooms = str(row['bedrooms']).replace("nan",'0.00')
			bedrooms = float(bedrooms)

			beds = row['beds']
			beds = str(row['beds']).replace("nan",'0.00')
			beds = float(beds)


			price = row['price']
			price = str(row['price']).replace("$",'')
			price = price.replace('"','')
			price = price.replace(',','')
			price = price.replace("nan",'0.0')
			price = float(price)

			availability_30 = row['availability_30']
			availability_30 = str(availability_30).replace("nan",'0')
			availability_30 = int(availability_30)

			availability_60 = row['availability_60']
			availability_60 = str(availability_60).replace("nan",'0')
			availability_60 = int(availability_60)

			availability_90 = row['availability_90']
			availability_90 = str(availability_90).replace("nan",'0')
			availability_90 = int(availability_90)

			availability_365 = row['availability_365']
			availability_365 = str(availability_365).replace("nan",'0')
			availability_365 = int(availability_365)


			number_of_reviews = row['number_of_reviews']
			number_of_reviews = str(number_of_reviews).replace("nan",'0')
			number_of_reviews = int(number_of_reviews)


			review_scores_rating = row['review_scores_rating']
			review_scores_rating = str(row['review_scores_rating']).replace("nan",'0.0')
			review_scores_rating = float(review_scores_rating)

			reviews_per_month = row['reviews_per_month']
			reviews_per_month = str(row['reviews_per_month']).replace("nan",'0.0')
			reviews_per_month = float(reviews_per_month)

			record = (listing_id , host_id , host_response_rate, host_acceptance_rate, host_is_superhost, host_listings_count, host_total_listings_count, host_identity_verified, neighbourhood_cleansed, calculated_host_listings_count, city, state, zipcode, country, latitude, longitude, property_type, room_type, accommodates, bathrooms, bedrooms, beds, price, availability_30, availability_60, availability_90, availability_365, number_of_reviews, review_scores_rating, reviews_per_month)
			data.append(record)

		cursor.executemany(sql, data)
		#print(data)
		db.commit()
	except Exception as e:
		print(e)
db.close()
