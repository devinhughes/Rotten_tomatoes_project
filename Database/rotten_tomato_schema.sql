-- create tables from cleaned data
CREATE TABLE movie_info (
 rotten_tomatoes_link TEXT NOT NULL,
 movie_title  TEXT NOT NULL,
 movie_info  TEXT NOT NULL,
 content_rating  VARCHAR(5) NOT NULL,
 genres TEXT NOT NULL,
 directors TEXT NOT NULL,
 authors TEXT NOT NULL,
 actors  TEXT NOT NULL,
 runtime  FLOAT NOT NULL,
 production_company TEXT NOT NULL, 
 release_year INTEGER NOT NULL, 
 streaming_release_year INTEGER NOT NULL,
 release_month INTEGER NOT NULL,
 streaming_month INTEGER NOT NULL,
 PRIMARY KEY (rotten_tomatoes_link)
);
CREATE TABLE rating_info (
rotten_tomatoes_link TEXT NOT NULL,
tomatometer_status  VARCHAR(6) NOT NULL, 
tomatometer_rating FLOAT NOT NULL,
tomatometer_count  FLOAT NOT NULL,
audience_status    VARCHAR(8) NOT NULL,
audience_rating  FLOAT NOT NULL,
audience_count   FLOAT NOT NULL,
tomatometer_top_critics_count INTEGER NOT NULL,
tomatometer_fresh_critics_count INTEGER NOT NULL, 
tomatometer_rotten_critics_count  INTEGER NOT NULL, 
PRIMARY KEY (rotten_tomatoes_link)	
);
-- show imported data
SELECT * FROM rating_info;
SELECT * FROM movie_info;

-- Joining movie_info and rating_info needed for analysis

SELECT movie_info.rotten_tomatoes_link,
 movie_info.movie_title,
 movie_info.movie_info,
 movie_info.content_rating,
 movie_info.genres,
 movie_info.directors,
 movie_info.authors,
 movie_info.actors,
 movie_info.runtime,
 movie_info.production_company,
 movie_info.release_month,
 movie_info.streaming_month,
 movie_info.release_year,
 movie_info.streaming_release_year,
 rating_info.tomatometer_status
INTO rotten_tomato_data
FROM movie_info
INNER JOIN rating_info
ON movie_info.rotten_tomatoes_link = rating_info.rotten_tomatoes_link;
SELECT * FROM rotten_tomato_data;


-- Join all data for into one dataset
SELECT movie_info.rotten_tomatoes_link,
 movie_info.movie_title,
 movie_info.movie_info,
 movie_info.content_rating,
 movie_info.genres,
 movie_info.directors,
 movie_info.authors,
 movie_info.actors,
 movie_info.runtime,
 movie_info.production_company,
 movie_info.release_month,
 movie_info.streaming_month,
 movie_info.release_year,
 movie_info.streaming_release_year,
 rating_info.tomatometer_status,
 rating_info.tomatometer_rating,
 rating_info.tomatometer_count,
 rating_info.audience_status,
 rating_info.audience_rating,
 rating_info.audience_count,
 rating_info.tomatometer_top_critics_count,
 rating_info.tomatometer_fresh_critics_count,
 rating_info.tomatometer_rotten_critics_count 
INTO full_table_rotten_analysis
FROM movie_info
INNER JOIN rating_info
ON movie_info.rotten_tomatoes_link = rating_info.rotten_tomatoes_link;
SELECT * FROM full_table_rotten_analysis;
SELECT * FROM rotten_tomato_data;
