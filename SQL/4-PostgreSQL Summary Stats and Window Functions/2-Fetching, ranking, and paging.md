# Fetching, ranking, and paging

## Fetching

LAG is a fetching function and LEAD is reverse of it. These are relative fetching functions.
Asolute fetching functions are FIRST_VALUE and LAST_VALUE which return first value and last value
respectively. LAST_VALUE has RANGE BETWEEN clause in its OVER clause.

### Future gold medalists

```
WITH Discus_Medalists AS (SELECT DISTINCT Year, Athlete
  			  FROM Summer_Medals
  			  WHERE Medal = 'Gold' AND Event = 'Discus Throw'
    			  AND Gender = 'Women' AND Year >= 2000)
SELECT year, athlete, LEAD(athlete,3) OVER (ORDER BY year ASC) AS Future_Champion
FROM Discus_Medalists
ORDER BY Year ASC;
```

### First athlete by name

```
WITH All_Male_Medalists AS (SELECT DISTINCT Athlete 
 			    FROM Summer_Medals
 			    WHERE Medal = 'Gold'
    			    AND Gender = 'Men')

SELECT athlete, FIRST_VALUE(athlete) OVER (ORDER BY athlete ASC) AS First_Athlete
FROM All_Male_Medalists;
```

### Last country by name

```
WITH Hosts AS (SELECT DISTINCT Year, City
	       FROM Summer_Medals)
SELECT Year, City, LAST_VALUE(city) OVER (ORDER BY year ASC
                                          RANGE BETWEEN UNBOUNDED PRECEDING AND
     					  UNBOUNDED FOLLOWING) AS Last_City
FROM Hosts
ORDER BY Year ASC;
```

## Ranking

* ROW_NUMBER()

Always assigns unique numbers, even if two rows are the same

* RANK()

Assigns the same number to rows with identical values. Skips over the next number.

* DENSE_RANK()

Same as the RANK but does not skip over the next number.

### Ranking athletes by medals earned

```
WITH Athlete_Medals AS (SELECT Athlete, COUNT(*) AS Medals
  			FROM Summer_Medals
  			GROUP BY Athlete)
SELECT Athlete, Medals, RANK() OVER (ORDER BY Medals DESC) AS Rank_N
FROM Athlete_Medals
ORDER BY Medals DESC;
```

### Ranking athletes from multiple countries

```
WITH Athlete_Medals AS (SELECT Country, Athlete, COUNT(*) AS Medals
  			FROM Summer_Medals
 			WHERE Country IN ('JPN', 'KOR') AND Year >= 2000
  			GROUP BY Country, Athlete
  			HAVING COUNT(*) > 1)
SELECT Country, athlete, Medals,
       DENSE_RANK() OVER (PARTITION BY country ORDER BY Medals DESC) AS Rank_N
FROM Athlete_Medals
ORDER BY Country ASC, RANK_N ASC;
```

## Paging

Paging is splitting data into chunks. Use NTILE(n) for paging. It is useful to split data
into thirds or quartiles to find top, middle and bottom. By spliting you can make the data
set more manageable.

### Paging events

```
WITH Events AS (SELECT DISTINCT Event
  		FROM Summer_Medals)
SELECT event, NTILE(111) OVER (ORDER BY event ASC) AS Page
FROM Events
ORDER BY Event ASC;
```

### Top, middle, and bottom thirds

```
WITH Athlete_Medals AS (SELECT Athlete, COUNT(*) AS Medals
  			FROM Summer_Medals
  			GROUP BY Athlete
  			HAVING COUNT(*) > 1),
     Thirds AS (SELECT Athlete, Medals, NTILE(3) OVER (ORDER BY Medals DESC) AS Third
  		FROM Athlete_Medals) 
SELECT third, AVG(medals) AS Avg_Medals
FROM Thirds
GROUP BY Third
ORDER BY Third ASC;
```