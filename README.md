# Radiant Insights — Dota 2 Analytics  

## 📖 Overview  
Radiant Insights is a fictional **esports analytics company**.  
This project analyzes **50,000 Dota 2 matches** from a Kaggle dataset to study:  
- Player performance (kills, assists, GPM, etc.)  
- Hero popularity  
- Item usage  
- Match outcomes and team trends  

---

## 📊 Dataset  
The dataset is available on Kaggle:  
👉 [Dota 2 Matches (50k)](https://www.kaggle.com/datasets/devinanzelmo/dota-2-matches)  

⚠️ The dataset is **too large for GitHub**, so it is **not stored in this repository**.  

To use it:  
1. Download the dataset from Kaggle.  
2. Extract all CSV files.  
3. Place them in a local folder (e.g., `datasets/`).  
4. Run `import.sql` to load the data into PostgreSQL.  

---

## 🛠 Tools Used  
- **PostgreSQL** → database  
- **pgAdmin / psql** → database management  
- **Python 3.x + psycopg2** → run queries programmatically  
- **dbdiagram.io** → create ER diagram  
- **GitHub** → repository & documentation  

---

## 📂 Repository Contents  

Radiant-Insights-Dota2/
│── schema.sql # CREATE TABLE statements
│── import.sql # \COPY commands for importing CSVs
│── queries.sql # 10 SQL queries with explanations
│── main.py # Python script that runs queries
│── ERD.png # Database ER diagram
│── images/ # Query result screenshots
│── README.md # Project documentation


---

#  Project Documentation  

##  Database Setup  

1. **Create the database**  
   ```sql
   CREATE DATABASE dota2;```

2.  Apply schema (create tables)
 ```psql -U postgres -d dota2 -p 5433 -f schema.sql```

3.  Import data from CSVs
 ```psql -U postgres -d dota2 -p 5433 -f import.sql```

4. Verify the tables
 ```\dt
   SELECT * FROM match LIMIT 5;```   

Example SQL Queries

Here are a few of the 10 queries included in queries.sql:

1. First 10 matches
```SELECT * FROM match LIMIT 10;```

2. Players with more than 10 kills
```SELECT account_id, kills, deaths, assists
   FROM players
   WHERE kills > 10
   LIMIT 5; ```

3. Top 10 most picked heroes
```SELECT h.localized_name, COUNT(*) AS picks
   FROM players p
   JOIN hero_names h ON p.hero_id = h.hero_id
   GROUP BY h.localized_name
   ORDER BY picks DESC
   LIMIT 10;```

 **Running the Python Script**
1. Install dependencies:
```pip install psycopg2-binary```

2. Run the script:
```python main.py```

Author Dalu
Astana IT university 






