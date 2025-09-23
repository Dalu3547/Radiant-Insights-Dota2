select * from match limit 10;

SELECT account_id, kills, deaths, assists
FROM players
WHERE kills > 10
LIMIT 5;

SELECT h.localized_name AS hero, COUNT(*) AS picks
FROM players p
JOIN hero_names h ON p.hero_id = h.hero_id
GROUP BY h.localized_name
ORDER BY picks DESC
LIMIT 10;

SELECT ROUND(AVG(duration),2) AS avg_duration_seconds
FROM match;

SELECT CASE WHEN radiant_win THEN 'Radiant' ELSE 'Dire' END AS side,
       COUNT(*) AS wins
FROM match
GROUP BY radiant_win;

SELECT i.item_name, COUNT(*) AS purchases
FROM purchase_log pl
JOIN item_ids i ON pl.item = i.item_id
GROUP BY i.item_name
ORDER BY purchases DESC
LIMIT 5;

SELECT ROUND(AVG(kills),2) AS avg_kills
FROM players;

SELECT match_id, COUNT(*) AS chat_count
FROM chat
GROUP BY match_id
ORDER BY chat_count DESC
LIMIT 5;

SELECT account_id, SUM(kills) AS total_kills
FROM players
GROUP BY account_id
ORDER BY total_kills DESC
LIMIT 5;

SELECT h.localized_name, ROUND(AVG(p.gold_per_min),2) AS avg_gpm
FROM players p
JOIN hero_names h ON p.hero_id = h.hero_id
GROUP BY h.localized_name
ORDER BY avg_gpm DESC
LIMIT 10;