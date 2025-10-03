import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sqlalchemy import create_engine

# ==============================
# Database Connection
# ==============================
DB_USER = "postgres"
DB_PASS = "dalu"       # change if needed
DB_HOST = "localhost"
DB_PORT = "5433"
DB_NAME = "dota2"

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Query: GPM by hero over months
query = """
SELECT DATE_TRUNC('month', to_timestamp(m.start_time)) AS month,
       h.localized_name AS hero,
       ROUND(AVG(p.gold_per_min), 2) AS avg_gpm
FROM players p
JOIN match m ON p.match_id = m.match_id
JOIN hero_names h ON p.hero_id = h.hero_id
GROUP BY month, h.localized_name
ORDER BY month, avg_gpm DESC;
"""
df = pd.read_sql(query, engine)

# Interactive scatter plot with time slider
fig = px.scatter(
    df,
    x="hero",
    y="avg_gpm",
    color="hero",
    size="avg_gpm",
    animation_frame=df["month"].dt.strftime("%Y-%m"),
    range_y=[0, df["avg_gpm"].max() * 1.1],
    title="Average GPM per Hero Over Time"
)

fig.update_layout(
    xaxis_title="Hero",
    yaxis_title="Average GPM",
    xaxis={'categoryorder':'total descending'}
)

fig.show()

# ==============================
# 1) Pie Chart – Radiant vs Dire Wins
# ==============================
query1 = """
SELECT CASE WHEN radiant_win THEN 'Radiant' ELSE 'Dire' END AS side,
       COUNT(*) AS wins
FROM match
GROUP BY radiant_win;
"""
df1 = pd.read_sql(query1, engine)
plt.figure(figsize=(6,6))
df1.set_index("side")["wins"].plot.pie(autopct="%1.1f%%", startangle=90)
plt.title("Radiant vs Dire Wins")
plt.ylabel("")
plt.savefig("charts/pie_radiant_vs_dire.png", dpi=150)
plt.close()
print(f"✅ Pie chart saved: Radiant vs Dire ({len(df1)} rows)")

# ==============================
# 2) Bar Chart – Top 10 Most Picked Heroes
# ==============================
query2 = """
SELECT h.localized_name AS hero, COUNT(*) AS picks
FROM players p
JOIN hero_names h ON p.hero_id = h.hero_id
GROUP BY h.localized_name
ORDER BY picks DESC
LIMIT 10;
"""
df2 = pd.read_sql(query2, engine)
df2.plot(kind="bar", x="hero", y="picks", legend=False, figsize=(10,6), color="skyblue")
plt.title("Top 10 Most Picked Heroes")
plt.xlabel("Hero")
plt.ylabel("Number of Picks")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("charts/bar_top_heroes.png", dpi=150)
plt.close()
print(f"✅ Bar chart saved: Top 10 heroes ({len(df2)} rows)")

# ==============================
# 3) Horizontal Bar Chart – Top 5 Most Purchased Items
# ==============================
query3 = """
SELECT account_id, SUM(kills) AS total_kills
FROM players
WHERE account_id != 0
GROUP BY account_id
ORDER BY total_kills DESC
LIMIT 10;
"""
df3 = pd.read_sql(query3, engine)
df3.plot(kind="barh", x="account_id", y="total_kills", legend=False, figsize=(10,6), color="green")
plt.title("Top 10 Accounts by Total Kills")
plt.xlabel("Total Kills")
plt.ylabel("Account ID")

plt.tight_layout()
plt.savefig("charts/hbar_top_accounts.png", dpi=150)
plt.close()

print(f"✅ Horizontal bar chart saved: Top 10 accounts ({len(df3)} rows)")

# ==============================
# 4) Line Chart – Average Match Duration Over Time
# ==============================
query4 = """
SELECT (to_timestamp(start_time) AT TIME ZONE 'UTC')::date AS match_date,
       ROUND(AVG(duration),2) AS avg_duration
FROM match
GROUP BY (to_timestamp(start_time) AT TIME ZONE 'UTC')::date
ORDER BY (to_timestamp(start_time) AT TIME ZONE 'UTC')::date;
"""
df4 = pd.read_sql(query4, engine)

plt.figure(figsize=(12,6))
plt.plot(df4["match_date"], df4["avg_duration"], marker="o", linestyle="-", color="green")
plt.title("Average Match Duration Over Time")
plt.xlabel("Date")
plt.ylabel("Average Duration (seconds)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/line_avg_duration_time.png", dpi=150)
plt.close()
print(f"✅ Line chart saved: Avg match duration over time ({len(df4)} rows)")


# ==============================
# 5) Histogram – Distribution of Player Kills
# ==============================
query5 = "SELECT kills FROM players;"
df5 = pd.read_sql(query5, engine)
df5["kills"].plot(kind="hist", bins=20, figsize=(8,6), color="purple", alpha=0.7)
plt.title("Distribution of Player Kills")
plt.xlabel("Kills")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("charts/hist_kills.png", dpi=150)
plt.close()
print(f"✅ Histogram saved: Kill distribution ({len(df5)} rows)")

# ==============================
# 6) Scatter Plot – Average GPM by Hero (Top 10)
# ==============================
query6 = """
SELECT h.localized_name, ROUND(AVG(p.gold_per_min),2) AS avg_gpm
FROM players p
JOIN hero_names h ON p.hero_id = h.hero_id
GROUP BY h.localized_name
ORDER BY avg_gpm DESC
LIMIT 10;
"""
df6 = pd.read_sql(query6, engine)
plt.figure(figsize=(10,6))
plt.scatter(df6["localized_name"], df6["avg_gpm"], c="red", alpha=0.7)
plt.title("Average Gold per Minute (Top 10 Heroes)")
plt.xlabel("Hero")
plt.ylabel("Average GPM")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("charts/scatter_gpm_heroes.png", dpi=150)
plt.close()
print(f"✅ Scatter plot saved: Avg GPM by hero ({len(df6)} rows)")
