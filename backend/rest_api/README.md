### AIBNB REST API

| Action| HTTP | URL Path | Description |
| ------ | ------ |------ |------ |
| Search by Country, Neighborhood, Checkin Date (required)| GET | http://[hostname]/home/search?country=&neighbourhood_cleansed=&date=&page=1| country, neighborhood and date are required on the homepage
| Search by Bathrooms (optional)| GET | [http://[hostname]/home/search?country=&neighbourhood_cleansed=&date=&bathrooms=&page=1]| Can be 1, 1.5, 2, 2.5, etc.
| Search by Bedrooms (optional)| GET | [http://[hostname]/home/search?country=&neighbourhood_cleansed=&date=&bedrooms=&page=1]| Can be 1, 1.5, 2, 2.5, etc.
| Search by min/max prices (optional)| GET | [http://[hostname]/home/search?country=&neighbourhood_cleansed=&date=&min_price=&max_price=&page=1]|
| Search by RoomType (optional)| GET | [http://[hostname]/home/search?country=&neighbourhood_cleansed=&date=&roomtype=&page=1]| apartment or private room
| Search by Sentiment (optional)| GET | [http://[hostname]/home/search?country=&neighbourhood_cleansed=&date=&sentiment=&page=1]| three level of sentiments.
