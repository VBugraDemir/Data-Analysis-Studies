
# Set theory clauses
Venn diagrams and introduction to union, union all, intersect, and except clauses. Semi joins and anti-joins.

## State of the UNION
Union includes every records in both tables but does not double count but Union All replicates. INTERSECT results in only those found in both 
of the two tables. EXCEPT results in only those records in one table but not the other.
The fields included in the operation must be of the same data type since they come back as just
single field. UNIONs stack records on top of each other from one table to the next


### Union
to create a table from a table 
```
SELECT code, year, income_group, gross_savings
INTO economies2010
FROM economies
WHERE year = 2010

SELECT *
FROM economies2010
UNION
SELECT *
FROM economies2015
ORDER BY code, year;
```

### Union (2)
```
SELECT country_code
FROM cities
UNION
SELECT code
FROM currencies
ORDER BY country_code;
```

### Union all
As you saw, duplicates were removed from the previous two exercises by using UNION. To include 
duplicates, you can use UNION ALL.
```
SELECT code, year
FROM economies
UNION ALL
SELECT country_code, year
FROM populations
ORDER BY code, year
```
There are duplicates!


## INTERSECTional data science
When INTERSECT looks at 2 columns it includes both columns in the search.
INTERSECT looks for records in common, not individual key fields like what a
join does to match.

### Intersect
```
SELECT code, year
FROM economies
INTERSECT
SELECT country_code, year
FROM populations
ORDER BY code, year;
```

### Intersect (2)
```
SELECT name
FROM countries
INTERSECT
SELECT name
FROM cities;
```

## EXCEPTional
EXCEPT allows you to include only the records that are in one table but not the other.

### Except
```
SELECT name 
FROM cities
EXCEPT
SELECT capital
FROM countries
ORDER BY name;
```

### Except (2)
```
SELECT capital 
FROM countries
EXCEPT
SELECT name
FROM cities
ORDER BY capital;
```

## Semi-joins and Anti-joins
The 6 joins so far are additive joins in that they add columns to the original
left table. The last ones use a right table to determine which records to keep in
in the left table. 

Semi join chooses records in the first table where a condition 
is met in a second table. An anti-join chooses records in the first table where 
condition is not met in the second table.

```
SELECT president, country, continent
FROM presidents
WHERE country IN (
	SELECT name
	FROM states
	WHERE indep_year < 1800
);
```
```
SELECT president, country, continent
FROM presidents
WHERE continent LIKE '%America'
AND country NOT IN (
	SELECT name
	FROM states
	WHERE indep_year < 1800
);
```

### Semi-join
```
SELECT * 
FROM countries
WHERE region = 'Middle East';
```
```
SELECT DISTINCT name
FROM languages
ORDER BY name;
```
```
SELECT DISTINCT name
FROM languages
WHERE code IN (
	SELECT code
	FROM countries
	WHERE region = 'Middle East'
)
ORDER BY name;
```

### Relating semi-join to a tweaked inner join
Sometimes problems solved with semi-joins can also be solved using an inner join.

```
SELECT DISTINCT name
FROM languages
WHERE code IN
  (SELECT code
   FROM countries
   WHERE region = 'Middle East')
ORDER BY name;
```
```
SELECT DISTINCT languages.name AS language
FROM languages
INNER JOIN countries
ON languages.code = countries.code
WHERE region = 'Middle East'
ORDER BY language;
```

### Diagnosing problems using anti-join
Another powerful join in SQL is the anti-join. It is particularly 
useful in identifying which records are causing an incorrect number 
of records to appear in join queries.
```
SELECT COUNT(*)
FROM countries
WHERE continent = 'Oceania'
```
```
SELECT c1.code, name, basic_unit AS currency
FROM countries AS c1
INNER JOIN currencies AS c2
ON c1.code = c2.code
WHERE continent = 'Oceania';
```
```
SELECT code, name
FROM countries
WHERE continent = 'Oceania'
AND code NOT IN(
	SELECT code
	FROM currencies
	WHERE continent = 'Oceania'
);
```

### Set theory challenge
Identify the country codes that are included in either economies  or currencies but not in populations.
```
SELECT name
FROM cities AS c1
WHERE country_code IN(
	SELECT e.code
	FROM economies AS e
	
	UNION
	SELECT c.code
	FROM currencies AS c
	
	EXCEPT
	SELECT p.country_code
	FROM populations AS p
);
```