LOAD DATA
INFILE 'C:\20205-lab\project\Climate\Climate-change\excel\sealevel.CSV'
TRUNCATE
INTO TABLE slevel
fields terminated by ","
(
	year,
	sealevel
)