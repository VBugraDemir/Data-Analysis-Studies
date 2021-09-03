# Beyond window functions

## Pivoting

Pivoting transforms a table by making columns out of the unique values
out of the values of one of its columns. CROSSTAB allows you to pivot a table.
Use CREATE EXTENSION to make extra functions in an extension available for use.
tablefunc extension contains the CROSSTAB function. Place your query between
2 dollar signs pairs.

### A basic pivot

```
CREATE EXTENSION IF NOT EXISTS tablefunc; 
SELECT * FROM CROSSTAB($$ SELECT Gender, Year, Country
  			  FROM Summer_Medals
  			  WHERE Year IN (2008, 2012) AND Medal = 'Gold'
    			  	AND Event = 'Pole Vault'
  			  ORDER By Gender ASC, Year ASC;$$) AS ct (Gender VARCHAR,
           							   "2008" VARCHAR,
           							   "2012" VARCHAR)
ORDER BY Gender ASC;
```

### Pivoting with ranking

```
CREATE EXTENSION IF NOT EXISTS tablefunc;
SELECT * FROM CROSSTAB($$ WITH Country_Awards AS (SELECT Country, Year, COUNT(*) AS Awards
    						  FROM Summer_Medals
    						  WHERE Country IN ('FRA', 'GBR', 'GER')
   							AND Year IN (2004, 2008, 2012)
     						        AND Medal = 'Gold'
    							GROUP BY Country, Year)

  			  SELECT Country, Year, RANK() OVER (PARTITION BY Year
       							     ORDER BY Awards DESC) :: INTEGER AS rank
  			  FROM Country_Awards
  			  ORDER BY Country ASC, Year ASC;$$) AS ct (country VARCHAR,
           							    "2004" INTEGER,
           							    "2008" INTEGER,
          							    "2012" INTEGER)

Order by Country ASC;
```

## ROLLUP and CUBE

ROLLUP is used to calculate group-level totals and grand totals. It is GROUP BY subclause that
includes extra rows for group-level aggregations. ROLLUP is hierarchical, the order of the columns
affects the output. CUBE is like ROLLUP but it is not hierarchical and generates all group-level 
aggregations. You can use ROLLUP when you have hierarchical data like date parts. Use CUBE when
you want all possible group-level aggregations.

### Country-level subtotals

```
SELECT Country, Gender, COUNT(*) AS Gold_Awards
FROM Summer_Medals
WHERE Year = 2004 AND Medal = 'Gold' AND Country IN ('DEN', 'NOR', 'SWE')
GROUP BY Country, ROLLUP(gender)
ORDER BY Country ASC, Gender ASC;
```

### All group-level subtotals

```
SELECT gender, medal, COUNT(*) AS Awards
FROM Summer_Medals
WHERE Year = 2012 AND Country = 'RUS'
GROUP BY CUBE(gender, medal)
ORDER BY Gender ASC, Medal ASC;
```

## A survey of useful functions

COALESCE is used when replace null value (pivoting, ROLLUP and CUBE, LAG and LEAD)

STRING_AGG takes all the values of a column and concatenates them, with a separtor in between
each value. It is useful when you want to reduce the number of the rows returned.

### Cleaning up results

```
SELECT COALESCE(Country, 'All countries') AS Country, COALESCE(Gender, 'All genders') AS Gender,
       COUNT(*) AS Awards
FROM Summer_Medals 
WHERE Year = 2004 AND Medal = 'Gold' AND Country IN ('DEN', 'NOR', 'SWE')
GROUP BY ROLLUP(Country, Gender)
ORDER BY Country ASC, Gender ASC
```

### Summarizing results

```
WITH Country_Medals AS (SELECT Country, COUNT(*) AS Medals
  			FROM Summer_Medals
  			WHERE Year = 2000 AND Medal = 'Gold'
  			GROUP BY Country),

     Country_Ranks AS (SELECT Country, RANK() OVER (ORDER BY Medals DESC) AS Rank
  		       FROM Country_Medals
                       ORDER BY Rank ASC)
SELECT STRING_AGG(country, ', ')
FROM Country_Ranks
WHERE Rank <= 3;
```