
# Subqueries

## Subqueries inside WHERE and SELECT clauses
The most common type of subquery is one inside of a WHERE statement.

```
SELECT name, fert_rate
FROM states
WHERE continent = 'Asia'
AND fert_rate < (
	SELECT AVG(fert_rate)
	FROM states
);
```
```
SELECT continent, Count(*)
from states
WHERE continent IN (
	SELECT DISTINCT continent
	FROM prime_ministers
)
group by continent
```
Is the same with
```
SELECT DISTINCT continent,(
	SELECT COUNT(*)
	FROM states
	WHERE prime_ministers.continent = states.continent) AS countries_num
FROM prime_ministers;
)
```

### Subquery inside where
```
SELECT AVG(life_expectancy)
FROM populations
WHERE year = 2015
```
```
SELECT *
FROM populations
WHERE year = 2015 AND life_expectancy > 1.15 * (
	SELECT AVG(life_expectancy)
	FROM populations
	WHERE year=2015
)
```

### Subquery inside where (2)
```
SELECT name, country_code, urbanarea_pop
FROM cities
WHERE name IN(
	SELECT capital
	FROM countries
)
ORDER BY urbanarea_pop DESC;
```

### Subquery inside select
Some queries can be written using either a join or a subquery.
```
SELECT countries.name AS country, COUNT(*) AS cities_num
FROM cities
INNER JOIN countries
ON countries.code = cities.country_code
GROUP BY country
ORDER BY cities_num DESC, country
LIMIT 9;
```
```
SELECT countries.name AS country, (SELECT COUNT(*) AS cities_num
								  FROM cities
								  WHERE countries.code = cities.country_code
								  ) AS cities_num
FROM countries
ORDER BY cities_num DESC, country
LIMIT 9;
```

## Subquery inside FROM clause
```
SELECT continent, MAX(women_parli_perc) AS max_perc
FROM states
WHERE continent IN (SELECT continent
					FROM monarchs

)
GROUP BY continent
ORDER BY continent
```
is the same with
```
SELECT DISTINCT monarchs.continent, subquery.max_perc
FROM monarchs, (SELECT continent, MAX(women_parli_perc) AS max_perc
			   FROM states
			   GROUP BY continent) AS subquery
WHERE monarchs.continent = subquery.continent
ORDER BY continent;
```
From with different tables without where is the cross join...

### Subquery inside from
```
SELECT countries.local_name, COUNT(*) as lang_num
FROM countries
INNER JOIN languages
ON languages.code = countries.code
GROUP BY countries.code
ORDER BY lang_num DESC;
```
it is the same with
```
SELECT countries.local_name, subquery.lang_num
FROM countries, (SELECT code, COUNT(*) AS lang_num
				FROM languages
				GROUP BY code) AS subquery
WHERE countries.code = subquery.code
ORDER BY lang_num DESC;
```

### Advanced subquery

```
SELECT name, continent, inflation_rate
FROM countries
INNER JOIN economies
USING(code)
WHERE year = 2015 AND inflation_rate IN (SELECT MAX(inflation_rate) AS max_inf
										FROM (SELECT name, continent, inflation_rate
											 FROM countries
											 INNER JOIN economies
											 USING(code)
											 WHERE year = 2015) AS subquery
										 GROUP BY continent);

```

### Subquery challenge
```
SELECT code, inflation_rate, unemployment_rate
FROM economies
WHERE year = 2015 AND code NOT IN (SELECT code 
								  FROM countries
								  WHERE gov_form = 'Constitutional Monarchy' 
								   OR gov_form LIKE '%Republic')
ORDER BY inflation_rate;
```

### Final challenge
Filtering specific codes for joins
```
SELECT DISTINCT name, total_investment, imports
FROM countries AS c
LEFT JOIN economies AS e
ON (c.code = e.code AND c.code IN (SELECT l.code
								  FROM languages AS l
								  WHERE official = 'true'))
WHERE region = 'Central America' 
AND year = 2015
ORDER BY name;
```
```
SELECT DISTINCT c.name, total_investment, imports
FROM countries AS c
LEFT JOIN economies AS e
ON c.code = e.code 
LEFT JOIN languages as l
ON c.code = l.code
WHERE region = 'Central America' AND official = 'true' 
AND year = 2015
ORDER BY name;
```
Same with the previous one.

### Final challenge(2)
```
SELECT region, continent, AVG(fertility_rate) AS avg_fert_rate
FROM countries AS c
INNER JOIN populations AS p
ON c.code = p.country_code
WHERE year = 2015
GROUP BY region,continent
ORDER BY avg_fert_rate;
```
### Final challenge (3)
```
SELECT name, country_code, city_proper_pop, metroarea_pop,
city_proper_pop / metroarea_pop * 100 AS city_perc
FROM cities
WHERE name IN (SELECT capital
			  FROM countries
			  WHERE (continent = 'Europe' OR continent LIKE '%America')
			  AND metroarea_pop IS NOT NULL)
ORDER BY city_perc DESC
LIMIT 10;
```	
