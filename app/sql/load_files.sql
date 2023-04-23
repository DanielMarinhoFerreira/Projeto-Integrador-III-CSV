use csgo;

-- load players.csv
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/players.csv'
INTO TABLE players
FIELDS TERMINATED BY ','
enclosed by '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- load picks.csv
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/picks.csv'
INTO TABLE picks
FIELDS TERMINATED BY ','
enclosed by '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- load econmy.csv
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/economy.csv'
INTO TABLE economy
FIELDS TERMINATED BY ','
enclosed by '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- load results.csv
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/results.csv'
INTO TABLE results
FIELDS TERMINATED BY ','
enclosed by '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;