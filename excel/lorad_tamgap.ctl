LOAD DATA
INFILE 'C:\20205-lab\project\Climate\Climate-change\excel\TEMGAP.CSV'
TRUNCATE
INTO TABLE tempergap
fields terminated by ","
(
	year,
	temgap
)