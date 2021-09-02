# Introduction to window functions

## Introduction

With window funtions you can calculate running totals and fetch previous rows' values.
Calculating growth over time, running totals, moving averages, assigning ranks. OVER()
clause indicates that it is a window function. You can enter row number by useing window
functions.

### Numbering rows

```
SELECT *, ROW_NUMBER() OVER() AS Row_N
FROM Summer_Medals
ORDER BY Row_N ASC;
```

### Numbering Olympic games in ascending order

```
SELECT Year, ROW_NUMBER() OVER() AS Row_N
FROM (SELECT DISTINCT year
      FROM Summer_Medals
      ORDER BY Year ASC) AS Years
ORDER BY Year ASC;
```

## ORDER BY

ORDER BY is a subcluse of OVER(). Multiple columns can be ordered in the OVER clause.
ORDER BY inside OVER takes effect before ORDER BY outside OVER

LAG returns columns's value at the row n rows before the current row.

* LAG() OVER(column_name, 1)

### Numbering Olympic games in descending order

```
SELECT Year, ROW_NUMBER() OVER (ORDER BY year DESC) AS Row_N
FROM (SELECT DISTINCT Year
      FROM Summer_Medals) AS Years
      ORDER BY Year;
``` 

### Numbering Olympic athletes by medals earned

``` 
WITH Athlete_Medals AS (SELECT Athlete, COUNT(*) AS Medals
  			FROM Summer_Medals
  			GROUP BY Athlete)

SELECT athlete, ROW_NUMBER() OVER(ORDER BY medals DESC) AS Row_N
FROM Athlete_Medals
ORDER BY Medals DESC;
``` 

### Reigning weightlifting champions

``` 
WITH Weightlifting_Gold AS (SELECT Year, Country AS champion
  			    FROM Summer_Medals
  			    WHERE Discipline = 'Weightlifting' AND
    				  Event = '69KG' AND Gender = 'Men' AND
    				  Medal = 'Gold')

SELECT Year, Champion,
LAG(Champion) OVER(ORDER BY Champion ASC) AS Last_Champion
FROM Weightlifting_Gold
ORDER BY Year ASC;
``` 

## PARTITION BY

Window functions behaviour can be change with the PARTITION BY subclause.

### Reigning champions by gender

``` 
WITH Tennis_Gold AS (SELECT DISTINCT Gender, Year, Country
  		     FROM Summer_Medals
                     WHERE Year >= 2000 AND Event = 'Javelin Throw' AND
                     Medal = 'Gold')

SELECT Gender, Year, Country AS Champion, 
       LAG(Country) OVER (PARTITION BY gender ORDER BY year ASC) AS Last_Champion
FROM Tennis_Gold
ORDER BY Gender ASC, Year ASC;
``` 

### Reigning champions by gender and event

``` 
WITH Athletics_Gold AS (SELECT DISTINCT Gender, Year, Event, Country
  			FROM Summer_Medals
  			WHERE Year >= 2000 AND Discipline = 'Athletics' AND
    			Event IN ('100M', '10000M') AND
    			Medal = 'Gold')

SELECT Gender, Year, Event, Country AS Champion,
       LAG(Country) OVER (PARTITION BY gender, event
                          ORDER BY Year ASC) AS Last_Champion
FROM Athletics_Gold
ORDER BY Event ASC, Gender ASC, Year ASC;
``` 










