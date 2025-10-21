import time
import random
import psycopg2

conn = psycopg2.connect(
    dbname="dota2",
    user="postgres",
    password="dalu",
    host="localhost",
    port="5433"
)
cur = conn.cursor()

while True:
    match_id = random.randint(10_000_000, 99_999_999)
    account_id = random.randint(100000, 999999)
    hero_id = random.randint(1, 138)
    kills = random.randint(0, 20)
    deaths = random.randint(0, 15)
    assists = random.randint(0, 25)
    gold = random.randint(1000, 20000)
    gold_spent = random.randint(1000, 20000)
    xp_per_min = random.randint(100, 800)
    gold_per_min = random.randint(100, 700)

    cur.execute("""
        INSERT INTO players (match_id, account_id, hero_id, player_slot, gold, gold_spent,
                             gold_per_min, xp_per_min, kills, deaths, assists, denies,
                             last_hits, stuns, hero_damage, hero_healing, tower_damage,
                             item_0, item_1, item_2, item_3, item_4, item_5, level, leaver_status)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (match_id, account_id, hero_id, random.randint(0, 9), gold, gold_spent, gold_per_min, xp_per_min,
          kills, deaths, assists, random.randint(0, 10), random.randint(0, 300), '0',
          random.randint(100, 30000), random.randint(0, 10000), random.randint(0, 20000),
          0, 0, 0, 0, 0, 0, random.randint(1, 30), 0))
    conn.commit()

    print(f"Inserted match {match_id}")
    time.sleep(10)
