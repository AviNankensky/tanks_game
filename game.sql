use TanksGame

select * from PLAYERS

SELECT * FROM GameStats

SELECT 1 FROM PLAYERS WHERE PlayerName COLLATE Latin1_General_CI_AS = 'avi' AND PlayerPassword = '123' 

SELECT *
FROM PLAYERS AS P INNER JOIN GameStats AS G
	ON P.PlayerName=G.PlayerName;
	

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

INSERT  INTO PLAYERS (PlayerName,PlayerPassword) VALUES('avi',65);

INSERT INTO GameStats ( PlayerName,Score,Coins) VALUES ('ava',2,1567);

INSERT INTO GameStats (GameID, GameDate, Score,Coins)
VALUES ('JohnDoe', '2024-07-04', 200, 45);


UPDATE INTO GameStats (PlayerName, Score, Coins) VALUES (' meir', 1, 1);




SELECT * FROM GameStats as G where G.PlayerName = 'avi'

SELECT 1 FROM GameStats WHERE PlayerName COLLATE Latin1_General_CI_AS = ? "


SELECT 1 FROM PLAYERS WHERE PlayerName COLLATE Latin1_General_CI_AS = ' avi'

SELECT 1 FROM PLAYERS WHERE PlayerPassword COLLATE Latin1_General_CI_AS = '123'


SELECT 1 
FROM PLAYERS 
WHERE PlayerName COLLATE Latin1_General_CI_AS = ' aa'
AND PlayerPassword COLLATE Latin1_General_CI_AS = ' 22'


