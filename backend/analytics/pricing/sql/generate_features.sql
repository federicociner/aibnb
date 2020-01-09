CREATE TABLE IF NOT EXISTS calendar_distinct_price AS
SELECT listing_id,
       full_date,
       MONTH(full_date) AS month,
       DAY(full_date) AS day,
       price
FROM (
  SELECT listing_id,
         price,
         CAST(MIN(date) AS date) AS full_date
  FROM calendar
  GROUP BY listing_id,
           price
) AS T1;

CREATE INDEX listing_id_index ON calendar_distinct_price (listing_id);

CREATE TABLE IF NOT EXISTS features_tmp AS
SELECT T1.*,
       T2.compound,
       T2.positive,
       T2.neutral,
       T2.negative
FROM listings AS T1
JOIN listings_sentiment AS T2
ON T1.listing_id = T2.listing_id;

CREATE INDEX listing_id_index ON features_tmp (listing_id);

DROP TABLE IF EXISTS features;

CREATE TABLE IF NOT EXISTS features AS
SELECT T1.listing_id,
       T2.full_date,
       T2.month,
       T2.day,
       T1.host_id,
       T1.host_response_rate,
       T1.host_acceptance_rate,
       T1.host_is_superhost,
       T1.host_listings_count,
       T1.host_total_listings_count,
       T1.host_identity_verified,
       T1.calculated_host_listings_count,
       T1.latitude,
       T1.longitude,
       T1.accommodates,
       T1.bathrooms,
       T1.bedrooms,
       T1.beds,
       T1.availability_30,
       T1.availability_60,
       T1.availability_90,
       T1.availability_365,
       T1.number_of_reviews,
       T1.review_scores_rating,
       T1.reviews_per_month,
       T1.compound,
       T1.positive,
       T1.neutral,
       T1.negative,
       T2.price + 0E0 AS label
FROM features_tmp AS T1
JOIN calendar_distinct_price AS T2
ON T1.listing_id = T2.listing_id;

DROP TABLE calendar_distinct_price;

DROP TABLE features_tmp;