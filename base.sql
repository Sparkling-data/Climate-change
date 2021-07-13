SQL> desc atmo_tem;
 Name                                                                                                              Null?    Type
 ----------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------
 A_YEAR                                                                                                                     NUMBER(4)
 A_TEM                                                                                                                      NUMBER(3)

SQL> desc sea_tem;
 Name                                                                                                              Null?    Type
 ----------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------
 T_YEAR                                                                                                                     NUMBER(4)
 T_TEM                                                                                                                      NUMBER(3)

SQL> desc sea_height;
 Name                                                                                                              Null?    Type
 ----------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------
 H_YEAR                                                                                                                     NUMBER(4)
 H_WORLD                                                                                                                    NUMBER(4,1)

SQL> desc co2_annual;
 Name                                                                                                              Null?    Type
 ----------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------
 C_YEAR                                                                                                                     NUMBER(4)
 C_WORLD                                                                                                                    NUMBER(5,1)


create view co2tem as select c_year as year, c_world as co2_den, A_tem as temgap  from co2_annual c, atmo_tem a
where c. c_year = a.a_year;

SQL> select * from co2tem;

      YEAR    CO2_DEN     TEMGAP
---------- ---------- ----------
      1984      344.3         -2
      1985      345.7         -3
      1986      347.2         -2
      1987        349          0
      1988      351.4          0
      1989        353         -1
      1990      354.2          0
      1991      355.5          0
      1992      356.2         -2
      1993        357         -2
      1994      358.5         -1
      1995      360.4          0
      1996      362.1         -1
      1997      363.3          1
      1998        366          2
      1999        368          0
      2000      369.5          0
      2001        371          1
      2002      372.9          2
      2003      375.3          2
      2004      377.1          1
      2005      379.2          2
      2006      381.3          2
      2007      383.1          1
      2008      385.2          1
      2009      386.7          2
      2010      388.9          2
      2011      390.9          1
      2012      393.1          2
      2013      395.7          2
      2014      397.7          3
      2015      400.1          4
      2016      403.3          5
      2017      405.5          4
      2018      407.8          3
      2019      410.5          4

36 rows selected.



chart 1 

이산화탄소 연평균 농도 


chart 2 
해수면 높이에 대한 그래프 

해수면 온도차와 기온차  ==> view 로 ?? 

chart 3 
이산화 탄소 연평균 농도와 기온차의 관계 
table 만들었음 
co2tem

