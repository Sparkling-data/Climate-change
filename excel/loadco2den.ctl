LOAD DATA
INFILE 'C:\20205-lab\project\Climate\Climate-change\excel\co2den.CSV'
TRUNCATE
INTO TABLE co2
fields terminated by ","
(
	year,
	co2den
)