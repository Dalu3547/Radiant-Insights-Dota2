# Radiant Insights — Dota 2 Analytics  

## 📖 Overview  
Radiant Insights is a fictional **esports analytics company**.  
This project analyzes **50,000 Dota 2 matches** from a Kaggle dataset to study:  
- Player performance (kills, assists, GPM, etc.)  
- Hero popularity  
- Item usage  
- Match outcomes and team trends  

---

**ER Diagram**
<img width="5334" height="3000" alt="ERD" src="https://github.com/user-attachments/assets/04776b35-6b2e-430a-bb24-6c46f8c9aeeb" />


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

│── analytics.py     # Charts & Excel export

│── ERD.png # Database ER diagram

│── images/ # Query result screenshots

│── analytics.py     # Charts & Excel export

│── charts/          # Saved charts (PNG images)

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
```\dt```
 ```SELECT * FROM match LIMIT 5;```   

**Example SQL Queries**

Here are a few of the 10 queries included in queries.sql:

1. First 10 matches
```SELECT * FROM match LIMIT 10;```

2. Players with more than 10 kills
```SELECT account_id, kills, deaths, assists FROM players WHERE kills > 10 LIMIT 5; ```

3. Top 10 most picked heroes
```SELECT h.localized_name, COUNT(*) AS picks FROM players p JOIN hero_names h ON p.hero_id = h.hero_id GROUP BY h.localized_name ORDER BY picks DESC LIMIT 10;```

📈 Visualizations

Using analytics.py, SQL queries were transformed into charts:

🥧 Radiant vs Dire win ratio (Pie chart)

📊 Most picked heroes (Bar chart)

📉 Match duration trends (Line chart)

📜 Chat activity per match (Linechart)

🛒 Top purchased items (Horizontal bar chart)

⚔️ Distribution of player kills (Histogram)

💰 Avg GPM by hero (Scatter plot)

All charts are saved inside the charts/ folder.

 **Running the Python Script**
1. Install dependencies:
```pip install psycopg2-binary pandas matplotlib sqlalchemy openpyxl```

2. Run the script:
```python main.py```

3. Generate charts & Excel
```python analytics.py```

# ⚙️ Prometheus & Grafana Monitoring Assignment

## 📖 Overview
This project sets up a complete **monitoring system** using Docker Compose.  
It collects and visualizes metrics from:
- PostgreSQL database (`dota2`)
- Node Exporter (system metrics)
- Custom Exporter (OpenWeather API data)

Three Grafana dashboards were created:
1. **Database Monitoring** – PostgreSQL performance
2. **System Monitoring** – CPU, memory, disk, network
3. **External API Monitoring** – weather metrics

---

## 🧩 Components

| Service | Description | Port |
|----------|--------------|------|
| PostgreSQL | Database containing the Dota 2 dataset | 5433 |
| Postgres Exporter | Exposes PostgreSQL metrics | 9187 |
| Node Exporter | Host system metrics | 9100 |
| Custom Exporter | Collects weather data from OpenWeather API | 9000 |
| Prometheus | Scrapes & stores metrics | 9090 |
| Grafana | Visualizes metrics | 3000 |

---

## 🚀 How to Run

```bash
docker-compose up -d --build

Author Dalu
Astana IT university 













