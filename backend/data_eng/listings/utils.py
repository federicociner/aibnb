


def getDirectory(datafolder):
	import os
	data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", datafolder)
	return data_dir

def getFiles(filepattern,topdir):
    import os
    import fnmatch
    for path, dirlist, filelist in os.walk(topdir):
        for name in fnmatch.filter(filelist,filepattern):
            yield os.path.join(path,name)

def openFiles(filenames):
    import gzip, bz2
    for name in filenames:
        if name.endswith(".gz"):
            yield gzip.open(name)
        elif name.endswith(".bz2"):
            yield bz2.BZ2File(name)
        else:
            yield open(name)


def streamFiles(sources):
	for s in sources:
		linenumber = -1
		for item in s:
			linenumber +=1
			if linenumber == 0:
				continue
			else:
				yield item


import numpy as np

dtypes = {
'accommodates' :  np.str,
'amenities' : np.str,
'availability_30' :  np.str,
'availability_365' :  np.str,
'availability_60' :  np.str,
'availability_90' :  np.str,
'bathrooms' :  np.str,
'bedrooms' :  np.str,
'beds' :  np.str,
'bed_type' : np.str,
'calculated_host_listings_count' :  np.str ,
'calendar_last_scraped' : np.str,
'calendar_updated' : np.str,
'cancellation_policy' : np.str,
'city' : np.str,
'cleaning_fee' : np.str,
'country' : np.str,
'country_code' : np.str,
'description' : np.str,
'experiences_offered' : np.str,
'extra_people' : np.str,
'first_review' : np.str,
'guests_included' :  np.str,
'has_availability' : np.str,
'host_about' : np.str,
'host_acceptance_rate' : np.str,
'host_has_profile_pic' : np.str,
'host_id' :  np.str,
'host_identity_verified' : np.str,
'host_is_superhost' : np.str,
'host_listings_count' :  np.str,
'host_location' : np.str,
'host_name' : np.str,
'host_neighbourhood' : np.str,
'host_picture_url' : np.str,
'host_response_rate' : np.str,
'host_response_time' : np.str,
'host_since' : np.str,
'host_thumbnail_url' : np.str,
'host_total_listings_count' :  np.str,
'host_url' : np.str,
'host_verifications' : np.str,
'id' :  np.str,
'instant_bookable' : np.str,
'is_location_exact' : np.str,
'jurisdiction_names' :  np.str,
'last_review' : np.str,
'last_scraped' : np.str,
'last_searched' : np.str,
'latitude' :  np.str,
'license' :  np.str,
'listing_url' : np.str,
'longitude' :  np.str,
'market' : np.str,
'maximum_nights' :  np.str,
'medium_url' : np.str,
'minimum_nights' :  np.str,
'monthly_price' : np.str,
'name' : np.str,
'neighborhood_overview' : np.str,
'neighbourhood' :  np.str,
'neighbourhood_cleansed' : np.str,
'notes' : np.str,
'number_of_reviews' :  np.str,
'picture_url' : np.str,
'price' : np.str,
'property_type' : np.str,
'region_id' :  np.str,
'region_name' : np.str,
'region_parent_id' :  np.str,
'region_parent_name' : np.str,
'region_parent_parent_id' :  np.str,
'region_parent_parent_name' :  np.str,
'require_guest_phone_verification' : np.str,
'require_guest_profile_picture' : np.str,
'requires_license' : np.str,
'review_scores_accuracy' :  np.str,
'review_scores_checkin' :  np.str,
'review_scores_cleanliness' :  np.str,
'review_scores_communication' :  np.str,
'review_scores_location' :  np.str,
'review_scores_rating' :  np.str,
'review_scores_value' :  np.str,
'reviews_per_month' :  np.str,
'room_type' : np.str,
'scrape_id' :  np.str,
'security_deposit' : np.str,
'smart_location' : np.str,
'space' : np.str,
'square_feet' :  np.str,
'state' : np.str,
'street' : np.str,
'summary' : np.str,
'thumbnail_url' : np.unicode,
'transit' : np.str,
'weekly_price' : np.str,
'xl_picture_url' : np.unicode,
'zipcode' :  np.str
}


selected= ['id','host_id','host_response_rate','host_acceptance_rate','host_is_superhost','host_listings_count','host_total_listings_count','host_identity_verified','neighbourhood_cleansed','calculated_host_listings_count','city','state','zipcode','country','latitude','longitude','property_type','room_type','accommodates','bathrooms','bedrooms','beds','price','availability_30','availability_60','availability_90','availability_365','number_of_reviews','review_scores_rating','reviews_per_month']
