use TanksGame


INSERT INTO GameStats ( PlayerName,Score,Coins) VALUES ('ava',2,1567);

SELECT 1 
FROM PLAYERS 
WHERE PlayerName COLLATE Latin1_General_CI_AS = ' aa'
AND PlayerPassword = ' 22'

select * from PLAYERS

SELECT * FROM GameStats

SELECT 1 FROM PLAYERS WHERE PlayerName COLLATE Latin1_General_CI_AS = 'avi' AND PlayerPassword = '123' 

SELECT *
FROM PLAYERS AS P INNER JOIN GameStats AS G
	ON P.PlayerName=G.PlayerName;


SELECT COLUMN_NAME, DATA_TYPE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'GameStats';

SELECT * FROM GameStats 


SELECT 1 
    FROM PLAYERS 
    WHERE PlayerName COLLATE Latin1_General_CI_AS = ''
    AND PlayerPassword  = '' 

	

SELECT 1 
    FROM PLAYERS 
    WHERE  PlayerPassword COLLATE Latin1_General_CI_AS = '444'

SELECT * 
FROM PLAYERS AS P 
WHERE P.PlayerPassword='1'
--CREATE TABLE PLAYERS(
-- PlayerName VARCHAR(50),
-- PlayerPassword INT 
-- PRIMARY KEY (PlayerName)
--);


--CREATE TABLE GameStats (
--    GameID INT IDENTITY(1,1) PRIMARY KEY,  -- עמודת מזהה אוטומטי
--    PlayerName VARCHAR(50) NOT NULL,
--    GameDate DATE NOT NULL,
--    Score INT NOT NULL,
--    Coins INT NOT NULL,
--    FOREIGN KEY (PlayerName) REFERENCES Players(PlayerName)
--);
DELETE FROM PLAYERS
WHERE PlayerName = ' avi';
delete PLAYERS
INSERT  INTO PLAYERS (PlayerName,PlayerPassword) VALUES('avi',65);
DROP TABLE GameStats;
DROP TABLE PLAYERS;


--INSERT INTO GameStats (GameID, GameDate, Score,Coins)
--VALUES ('JohnDoe', '2024-07-04', 200, 45);


--UPDATE INTO GameStats (PlayerName, Score, Coins) VALUES (' meir', 1, 1);




--SELECT * FROM GameStats as G where G.PlayerName = 'avi'

--SELECT 1 FROM GameStats WHERE PlayerName COLLATE Latin1_General_CI_AS = ? "


--SELECT 1 FROM PLAYERS WHERE PlayerName COLLATE Latin1_General_CI_AS = ' avi'

--SELECT 1 FROM PLAYERS WHERE PlayerPassword COLLATE Latin1_General_CI_AS = '123'







CREATE TABLE PLAYERS (
    PlayerName VARCHAR(50) COLLATE Latin1_General_CI_AS NOT NULL,
    PlayerPassword INT NOT NULL,
    PRIMARY KEY (PlayerName)
);

CREATE TABLE GameStats (
    GameID INT IDENTITY(1,1) PRIMARY KEY,  -- עמודת מזהה אוטומטי
    PlayerName VARCHAR(50) COLLATE Latin1_General_CI_AS NOT NULL,
    GameDate DATE NOT NULL,
    Score INT NOT NULL,
    Coins INT NOT NULL,
    FOREIGN KEY (PlayerName) REFERENCES PLAYERS(PlayerName)
);

