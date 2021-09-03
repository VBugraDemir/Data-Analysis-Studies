# Aggregate window functions and frames
 
## Aggregate window functions

MAX Window function: Shows the max value for each row.

SUM Window function: Use for cumulative sum.

### Running totals of athlete medals

```
WITH Athlete_Medals AS (SELECT Athlete, COUNT(*) AS Medals
			FROM Summer_Medals
  			WHERE Country = 'USA' AND Medal = 'Gold'
  			      AND Year >= 2000
  			GROUP BY Athlete)

SELECT Athlete, medals, SUM(medals) OVER (ORDER BY athlete ASC) AS Max_Medals
FROM Athlete_Medals
ORDER BY Athlete ASC;
```

### Maximum country medals by year

```
WITH Country_Medals AS (SELECT Year, Country, COUNT(*) AS Medals
  			FROM Summer_Medals
  			WHERE Country IN ('CHN', 'KOR', 'JPN')
    			      AND Medal = 'Gold' AND Year >= 2000
  			GROUP BY Year, Country)
SELECT year, country, medals, MAX(medals) OVER (PARTITION BY country
                		  		ORDER BY year ASC) AS Max_Medals
FROM Country_Medals
ORDER BY Country ASC, Year ASC;
```

### Minimum country medals by year

```
WITH France_Medals AS (SELECT Year, COUNT(*) AS Medals
  	 	       FROM Summer_Medals
  		       WHERE Country = 'FRA'
   			     AND Medal = 'Gold' AND Year >= 2000
           	       GROUP BY Year)
SELECT year, medals, MIN(medals) OVER (ORDER BY year ASC) AS Min_Medals
FROM France_Medals
ORDER BY Year ASC;
```

## Frames

Frame is the range defined in OVER clause. A frame always starts with RANGE 
BETWEEN or ROWS BETWEEN.

* ROWS BETWEEN [START] AND [FINISH]
	* n PRECEDING: n rows before the current row
	* CURRENT ROW: the current row
	* n FOLLOWING: n rows after the current row

### Moving maximum of Scandinavian athletes' medals

```
WITH Scandinavian_Medals AS (SELECT Year, COUNT(*) AS Medals
  			     FROM Summer_Medals
                             WHERE Country IN ('DEN', 'NOR', 'FIN', 'SWE', 'ISL')
    				   AND Medal = 'Gold'
                  		   GROUP BY Year)
SELECT Year, Medals, MAX(Medals) OVER (ORDER BY Year ASC ROWS BETWEEN CURRENT ROW
                                       AND 1 FOLLOWING) AS Max_Medals
FROM Scandinavian_Medals
ORDER BY Year ASC;
```

### Moving maximum of Chinese athletes' medals

```
WITH Chinese_Medals AS (SELECT Athlete, COUNT(*) AS Medals
  			FROM Summer_Medals
  			WHERE Country = 'CHN' AND Medal = 'Gold'
    			      AND Year >= 2000
    			GROUP BY Athlete)
SELECT athlete, medals, MAX(medals) OVER (ORDER BY athlete ASC
            				  ROWS BETWEEN 2 PRECEDING
            				  AND CURRENT ROW) AS Max_Medals
FROM Chinese_Medals
ORDER BY Athlete ASC;
```

## Moving averages and totals

Moving average is the average of last n periods. Moving total is the sum of
last n periods. These metrics track the change in performance over time.

ROW BETWEEN is used for frame funtions since RANGE BETWEEN treats duplicates in 
the columns as single entities. In practice ROWS BETWEEN is almost always 
used over RANGE BETWEEN. 

### Moving average of Russian medals

```
WITH Russian_Medals AS (SELECT Year, COUNT(*) AS Medals
  			FROM Summer_Medals
  			WHERE Country = 'RUS' AND Medal = 'Gold' AND Year >= 1980
  			GROUP BY Year)
SELECT Year, Medals, AVG(Medals) OVER(ORDER BY Year ASC ROWS BETWEEN
     				      2 PRECEDING AND CURRENT ROW) AS Medals_MA
FROM Russian_Medals
ORDER BY Year ASC;
```

### Moving total of countries' medals

```
WITH Country_Medals AS (SELECT Year, Country, COUNT(*) AS Medals
  			FROM Summer_Medals
  			GROUP BY Year, Country)
SELECT Year, Country, Medals, SUM(Medals) OVER(PARTITION BY country ORDER BY Year ASC
     					       ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS Medals_MA
FROM Country_Medals
ORDER BY Country ASC, Year ASC;
```
