# Radiant-Insights-Dota2
Analytics of Dota 2 Matches dataset

Company Overview

Radiant Insights is a fictional esports analytics company.
The project focuses on analyzing Dota 2 match data to understand player performance, hero popularity, item usage, and match outcomes.


Put ERD picture

## Dataset
The dataset used in this project comes from Kaggle:
[Dota 2 Matches (50k)](https://www.kaggle.com/datasets/devinanzelmo/dota-2-matches)

Due to size limits, the dataset is not stored in this repository.  
To use it:
1. Download the dataset from Kaggle.
2. Extract all CSV files.
3. Place them in a local folder (e.g., `datasets/`).
4. Run `import.sql` to load the CSVs into PostgreSQL.


Project Description
The dataset comes from Kaggle (Dota 2 Matches, 50k rows). It contains information about:

Matches and outcomes
Players and statistics
Heroes, items, and abilities
Teamfights and objectives
Chat messages

This project builds a PostgreSQL database, imports the dataset, creates an ER diagram, and runs SQL analytics. A Python script is also included to connect to the database and execute queries.

Tools Used:

PostgreSQL
pgAdmin / psql
Python 3.x + psycopg2
dbdiagram.io (for ERD)
GitHub (repository)

Repository Contents:

datasets → dota 2 datasets
Images → images of query
schema.sql → table definitions
import.sql → data import commands
queries.sql → 10 SQL queries with comments
main.py → Python script for running queries
ERD.png → ER diagram
README.md → documentation

Database Setup:
CREATE DATABASE dota2;

Apply schema:
```psql -U postgres -d dota2 -p 5433 -f schema.sql```

Import data:
```psql -U postgres -d dota2 -p 5433 -f import.sql```

Verify:
```Select * from match limit 5;```

Queries

The following queries were written and tested:

First 10 matches.
Players with more than 10 kills.
Top 10 most picked heroes.
Average match duration.
Radiant vs Dire wins.
Top 5 purchased items.
Average kills per player.
Matches with most chat messages.
Top 5 accounts by kills.
Average GPM by hero.

Running Python Script
pip install psycopg2-binary 

Run:
python main.py

Author Dalu
Astana IT university 


