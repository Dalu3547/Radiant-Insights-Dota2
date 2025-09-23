import psycopg2

DB_NAME = "dota2"
DB_USER = "postgres"
DB_PASS = "dalu"
DB_HOST = "localhost"
DB_PORT = "5433"

QUERIES = {
    "1) First 10 matches": """
        SELECT * FROM match LIMIT 10;
    """,
    "2) 5 players with more than 10 kills": """
        SELECT account_id, kills, deaths, assists
        FROM players
        WHERE kills > 10
        LIMIT 5;
    """,
    "3) Top 10 most picked heroes": """
        SELECT h.localized_name AS hero, COUNT(*) AS picks
        FROM players p
        JOIN hero_names h ON p.hero_id = h.hero_id
        GROUP BY h.localized_name
        ORDER BY picks DESC
        LIMIT 10;
    """,
    "4) Average match duration": """
        SELECT ROUND(AVG(duration),2) AS avg_duration_seconds
        FROM match;
    """,
    "5) Radiant vs Dire wins": """
        SELECT CASE WHEN radiant_win THEN 'Radiant' ELSE 'Dire' END AS side,
               COUNT(*) AS wins
        FROM match
        GROUP BY radiant_win;
    """,
    "6) Top 5 most purchased items": """
        SELECT i.item_name, COUNT(*) AS purchases
        FROM purchase_log pl
        JOIN item_ids i ON pl.item = i.item_id
        GROUP BY i.item_name
        ORDER BY purchases DESC
        LIMIT 5;
    """,
    "7) Average number of kills per player": """
        SELECT ROUND(AVG(kills),2) AS avg_kills
        FROM players;
    """,
    "8) 5 matches with most chat messages": """
        SELECT match_id, COUNT(*) AS chat_count
        FROM chat
        GROUP BY match_id
        ORDER BY chat_count DESC
        LIMIT 5;
    """,
    "9) Top 5 accounts by total kills": """
        SELECT account_id, SUM(kills) AS total_kills
        FROM players
        GROUP BY account_id
        ORDER BY total_kills DESC
        LIMIT 5;
    """,
    "10) Average GPM by hero (top 10)": """
        SELECT h.localized_name, ROUND(AVG(p.gold_per_min),2) AS avg_gpm
        FROM players p
        JOIN hero_names h ON p.hero_id = h.hero_id
        GROUP BY h.localized_name
        ORDER BY avg_gpm DESC
        LIMIT 10;
    """
}

def main():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = conn.cursor()
        print("Connected to Database")

        for title, sql in QUERIES.items():
            print(title)
            cur.execute(sql)
            rows = cur.fetchall()
            for row in rows:
                print(row)
            print("\n")

        cur.close()
        conn.close()

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()