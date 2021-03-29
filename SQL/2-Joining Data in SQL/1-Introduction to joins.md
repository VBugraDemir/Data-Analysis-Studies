
# Introduction to joins

## Introduction to inner join

INNER JOIN only includes records in which the key is in both tables.

### Inner join
```
Select *
FROM cities
```
```
SELECT * 
FROM cities
INNER JOIN countries
ON cities.country_code = countries.code;
```
```	
SELECT cities.name AS city, countries.name as country,region
FROM cities
INNER JOIN countries 
ON cities.country_code = countries.code;
```

### Inner join (2)
```
SELECT c.code as country_code, c.name, e.year, e.inflation_rate
FROM countries AS c
INNER JOIN economies as e
ON c.code=e.code;
```

### Inner join (3)
```
SELECT c.code, c.name, c.region, p.year, p.fertility_rate
FROM countries AS c
INNER JOIN populations AS p
ON c.code = p.country_code
```
```
SELECT c.code, name, region, e.year, fertility_rate, unemployment_rate
FROM countries AS c
INNER JOIN populations AS p
ON c.code = p.country_code
INNER JOIN economies AS e
ON c.code = e.code;
```
```
SELECT c.code, name, region, e.year, fertility_rate, unemployment_rate
FROM countries AS c
INNER JOIN populations AS p
ON c.code = p.country_code
INNER JOIN economies AS e
ON c.code = e.code AND p.year = e.year;
```

### INNER JOIN via USING
When the key field you'd like to join on is the same name in both table you can use "USING" instead
of "ON".
 
```
SELECT c.name AS country, c.continent, l.name as language, l.official
FROM countries AS c
INNER JOIN languages AS l
USING (code)
```

### Self-ish joins, just in CASE
Inner join the table itself for self-joins. It is good practise when you alias tables with two different
names.
```
SELECT p1.country AS country1, p2.country AS country2, p1.continent
FROM prime_ministers AS p1
INNER JOIN prime_ministers AS p2
ON p1.continent = p2.continent
LIMIT 14;
```
```
SELECT p1.country AS country1, p2.country AS country2, p1.continent
FROM prime_ministers AS p1
INNER JOIN prime_ministers AS p2
ON p1.continent = p2.continent AND p1.country <> p2.country
LIMIT 14;
```
CASE is a way to do multiple if-then-else statements in simplified way.
```
SELECT name, continents, indep_year,
CASE WHEN indep_year < 1900 THEN 'before 1900'
WHEN indep_year <= 1930 THEN 'between 1900 and 1930'
ELSE 'after 1930' END
AS indep_year_group
FROM states
ORDER BY indep_year_group;
```

### Self-join
```
SELECT p1.country_code, p1.size AS size2010, p2.size AS size2015
((p2.size - p1.size)/p1.size*100.0) AS growth_perc
FROM populations AS p1
INNER JOIN populations AS p2
ON p1.country_code = p2.country_code AND p1.year = p2.year -5;
```

### Case when and then
```
SELECT name, continent, code, surface_area, CASE WHEN surface_area > 2000000 THEN 'large'
WHEN surface_area > 350000 THEN 'medium'
ELSE 'small' END
AS geosize_group
FROM countries;
```

### Inner challenge
Use INTO command to create table
```
SELECT country_code, size, 
CASE WHEN size > 50000000 THEN 'large'
WHEN size > 1000000 THEN 'medium'
ELSE 'small' END
AS popsize_group
INTO pop_plus
FROM populations
WHERE year = 2015;
```
```
SELECT country_code, size, 
CASE WHEN size > 50000000 THEN 'large'
WHEN size > 1000000 THEN 'medium'
ELSE 'small' END
AS popsize_group
INTO pop_plus
FROM populations
WHERE year = 2015;
```
```
SLEECT c.name, c.continent, c.geosize_group, p.popsize_group
FROM countries_plus AS c
INNER JOIN pop_plus AS p
ON c.code = p.country_code
ORDER BY geosize_group;
```
