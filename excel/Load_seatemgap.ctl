LOAD DATA
INFILE 'C:\20205-lab\project\Climate\Climate-change\excel\seatemgap.CSV'
TRUNCATE
INTO TABLE seatempergap
fields terminated by ","
(
	year,
	seatemgap
)