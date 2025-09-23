CREATE TABLE teamfights_players (
    match_id BIGINT,
    player_slot INT,
    buybacks INT,
    damage INT,
    deaths INT,
    gold_delta INT,
    xp_end INT,
    xp_start INT
);

CREATE TABLE test_player (
    match_id BIGINT,
    account_id BIGINT,
    hero_id INT,
	player_slot INT
);

CREATE TABLE match_outcomes (
    match_id BIGINT,
    account_id_0 BIGINT,
    account_id_1 BIGINT,
    account_id_2 BIGINT,
    account_id_3 BIGINT,
    account_id_4 BIGINT,
    start_time BIGINT,       
    parser_version VARCHAR(50),
    win SMALLINT,             
    rad SMALLINT              
);

CREATE TABLE player_time (
    match_id BIGINT,
    times INT,
    gold_t_0 INT,
    lh_t_0 INT,
    xp_t_0 INT
);

CREATE TABLE player_ratings (
    match_id BIGINT,
    account_id BIGINT,
    hero_id INT,
    solo_competitive_rank FLOAT,
    competitive_rank FLOAT
);
CREATE TABLE patch_dates (
    patch_date TIMESTAMP,
    patch VARCHAR(10)
);


CREATE TABLE chat (
    match_id BIGINT,
    key TEXT,         
    slot INT NULL,
    time INT NULL,
    unit VARCHAR(100)
);

CREATE TABLE objectives (
    match_id BIGINT,
    key VARCHAR(100),
    player1 FLOAT NULL,
    player2 FLOAT NULL,
    slot FLOAT NULL,
    subtype VARCHAR(100),
    team VARCHAR(50),
    time FLOAT NULL,
    value FLOAT NULL
);

CREATE TABLE teamfights (
    match_id BIGINT,
    start INT,
    "end" INT,
    last_death INT,
    deaths INT
);


CREATE TABLE ability_upgrades (
    match_id BIGINT,
    account_id BIGINT,
    ability INT,
    time INT,
    level INT
);

CREATE TABLE purchase_log (
    match_id BIGINT,
    account_id BIGINT,
    item INT,
    time INT
);

CREATE TABLE match (
    match_id BIGINT PRIMARY KEY,
    start_time BIGINT,
    duration INT,
    tower_status_radiant INT,
    tower_status_dire INT,
    barracks_status_dire INT,
    barracks_status_radiant INT,
    first_blood_time INT,
    game_mode INT,
    radiant_win BOOLEAN,
    negative_votes INT,
    positive_votes INT,
    cluster INT
);

CREATE TABLE players (
    match_id BIGINT,
    account_id BIGINT,
    hero_id INT,
    player_slot INT,
    gold INT,
    gold_spent INT,
    gold_per_min INT,
    xp_per_min INT,
    kills INT,
    deaths INT,
    assists INT,
    denies INT,
    last_hits INT,
    stuns VARCHAR(50),
    hero_damage INT,
    hero_healing INT,
    tower_damage INT,
    item_0 INT,
    item_1 INT,
    item_2 INT,
    item_3 INT,
    item_4 INT,
    item_5 INT,
    level INT,
    leaver_status INT
);

CREATE TABLE cluster_regions (
    cluster_id INT PRIMARY KEY,
    region VARCHAR(50)
);

CREATE TABLE hero_names (
    name VARCHAR(100),          
    hero_id INT PRIMARY KEY,
    localized_name VARCHAR(100) 
);

CREATE TABLE item_ids (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(100)
);

CREATE TABLE ability_ids (
    ability_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE test_labels (
    match_id BIGINT,
    radiant_win BOOLEAN
);
	