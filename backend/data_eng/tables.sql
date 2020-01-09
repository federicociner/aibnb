CREATE TABLE IF NOT EXISTS reviews (
	listing_id INT,
	id INT,
	date TEXT,
	reviewer_id INT,
	reviewer_name TEXT,
	comments LONGTEXT,
	PRIMARY KEY(id)
);

CREATE TABLE `listings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `listing_id` int(11) NOT NULL,
  `host_id` int(11) NOT NULL,
  `host_response_rate` float DEFAULT NULL,
  `host_acceptance_rate` float DEFAULT NULL,
  `host_is_superhost` tinyint(1) DEFAULT NULL,
  `host_listings_count` float DEFAULT NULL,
  `host_total_listings_count` float DEFAULT NULL,
  `host_identity_verified` tinyint(1) DEFAULT NULL,
  `neighbourhood_cleansed` varchar(255) DEFAULT NULL,
  `calculated_host_listings_count` int(11) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `state` varchar(255) DEFAULT NULL,
  `zipcode` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  `property_type` varchar(255) DEFAULT NULL,
  `room_type` varchar(255) DEFAULT NULL,
  `accommodates` int(11) DEFAULT NULL,
  `bathrooms` float DEFAULT NULL,
  `bedrooms` float DEFAULT NULL,
  `beds` float DEFAULT NULL,
  `price` float DEFAULT NULL,
  `availability_30` int(11) DEFAULT NULL,
  `availability_60` int(11) DEFAULT NULL,
  `availability_90` int(11) DEFAULT NULL,
  `availability_365` int(11) DEFAULT NULL,
  `number_of_reviews` int(11) DEFAULT NULL,
  `review_scores_rating` float DEFAULT NULL,
  `reviews_per_month` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `c_index` (`country`),
  KEY `n_cleansed_index` (`neighbourhood_cleansed`)
) DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS calendar (
	id INT NOT NULL AUTO_INCREMENT,
	listing_id INT,
	date TEXT,
	available ENUM('t', 'f'),
	price DECIMAL(12,2),
	PRIMARY KEY(id)
);
