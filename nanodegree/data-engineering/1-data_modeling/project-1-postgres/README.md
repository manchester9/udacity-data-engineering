# Introduction: Project: Data Modeling with Postgres
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

# Purpose
To understand the usage of songs by different users. Data is present in JSON format which is extracted, manipulated and then analyzed

# Database Schema: Fact and Dimension Tables
The database used in this exercise is Star Schema. Songplay is the center of the business logic which is why it is the fact table. The dimension table consists users, songs, artists, and time
 
Fact_table: songplays
songplayid: ID of each user song play
start_time: Timestamp of beggining of user activity
user_id: ID of user
level: User level {free | paid}
song_id: ID of Song played
artist_id: ID of Artist of the song played
session_id: ID of the user Session
location: User location
user_agent: Agent used by user to access Sparkify platform

Dimension_table: users
user_id: ID of user
first_name: First name of each user
last_name: Last name of each user
gender: Gender of each user
level: User level

Dimension_table: songs
song_id: ID of Song
title: Title of Song
artist_id: ID of song Artist
year: Year of song release
duration: Song duration in milliseconds

Dimension_table: artists
artist_id: ID of Artist
name: Name of Artist
location: Name of Artist city
lattitude: Lattitude location of artist
longitude: Longitude location of artist

Dimension_table: time
start_time: Timestamp of row
hour: Hour associated to start_time
day: Day associated to start_time
week: Week of year associated to start_time
month: Month associated to start_time
year: Year associated to start_time
weekday: Name of week day associated to start_time

# Project Description
In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

# Project datasets: 
## Song Dataset
The first dataset is a subset of real data from the Million Song Dataset [http://millionsongdataset.com/]. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.

song_data/A/B/C/TRABCEI128F424C983.json
song_data/A/A/B/TRAABJL12903CDCF1A.json

And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.

{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}

## Log Dataset
The second dataset consists of log files in JSON format generated by this event simulator [https://github.com/Interana/eventsim] based on the songs in the dataset above. These simulate activity logs from a music streaming app based on specified configurations.

The log files in the dataset you'll be working with are partitioned by year and month. For example, here are filepaths to two files in this dataset.

log_data/2018/11/2018-11-12-events.json
log_data/2018/11/2018-11-13-events.json

And below is an example of what the data in a log file, 2018-11-12-events.json, looks like.

* [Image Link]

If you would like to look at the JSON data within log_data files, you will need to create a pandas dataframe to read the data. Remember to first import JSON and pandas libraries.
df = pd.read_json(filepath, lines=True)
For example, df = pd.read_json('data/log_data/2018/11/2018-11-01-events.json', lines=True) would read the data file 2018-11-01-events.json.




