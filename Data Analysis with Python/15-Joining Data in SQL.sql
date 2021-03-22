------ Joining Data in SQL

----- Introduction to INNER JOIN

--- INNER JOIN only includes records in which the key is in both tables.

---- Inner join
Select *
FROM cities

SELECT * 
FROM cities
  INNER JOIN countries
    ON cities.country_code = countries.code;
	
SELECT cities.name AS city, countries.name as country,region
FROM cities
INNER JOIN countries 
ON cities.country_code = countries.code;

---- Inner join (2)

SELECT c.code as country_code, c.name, e.year, e.inflation_rate
FROM countries AS c
INNER JOIN economies as e
ON c.code=e.code;

---- Inner join (3)

SELECT c.code, c.name, c.region, p.year, p.fertility_rate
FROM countries AS c
INNER JOIN populations AS p
ON c.code = p.country_code


SELECT c.code, name, region, e.year, fertility_rate, unemployment_rate
FROM countries AS c
INNER JOIN populations AS p
ON c.code = p.country_code
INNER JOIN economies AS e
ON c.code = e.code;

SELECT c.code, name, region, e.year, fertility_rate, unemployment_rate
FROM countries AS c
INNER JOIN populations AS p
ON c.code = p.country_code
INNER JOIN economies AS e
ON c.code = e.code AND p.year = e.year;


---- INNER JOIN via USING
--- When the key field you'd like to join on is the same name in both table
--- USING can be used instead of ON clause.  

SELECT c.name AS country, c.continent, l.name as language, l.official
FROM countries AS c
INNER JOIN languages AS l
USING (code)

----- Self-ish joins, just in CASE
--- Inner join the table itself for self-joins

SELECT p1.country AS country1, p2.country AS country2, p1.continent
FROM prime_ministers AS p1
INNER JOIN prime_ministers AS p2
ON p1.continent = p2.continent
LIMIT 14;


SELECT p1.country AS country1, p2.country AS country2, p1.continent
FROM prime_ministers AS p1
INNER JOIN prime_ministers AS p2
ON p1.continent = p2.continent AND p1.country <> p2.country
LIMIT 14;

--- CASE is a way to do multiple if-then-else statements in simplified way.

SELECT name, continents, indep_year,
CASE WHEN indep_year < 1900 THEN 'before 1900'
WHEN indep_year <= 1930 THEN 'between 1900 and 1930'
ELSE 'after 1930' END
AS indep_year_group
FROM states
ORDER BY indep_year_group;

---- Self-join

SELECT p1.country_code, p1.size AS size2010, p2.size AS size2015
((p2.size - p1.size)/p1.size*100.0) AS growth_perc
FROM populations AS p1
INNER JOIN populations AS p2
ON p1.country_code = p2.country_code AND p1.year = p2.year -5;


----- Case when and then

SELECT name, continent, code, surface_area,
CASE WHEN surface_area > 2000000 THEN 'large'
WHEN surface_area > 350000 THEN 'medium'
ELSE 'small' END
AS geosize_group
FROM countries;

----- Inner challenge

SELECT country_code, size, 
CASE WHEN size > 50000000 THEN 'large'
WHEN size > 1000000 THEN 'medium'
ELSE 'small' END
AS popsize_group
INTO pop_plus
FROM populations
WHERE year = 2015;

SLEECT c.name, c.continent, c.geosize_group, p.popsize_group
FROM countries_plus AS c
INNER JOIN pop_plus AS p
ON c.code = p.country_code
ORDER BY geosize_group;


----- LEFT and RIGHT JOINs
--- 3 types of outer joins: Left, right and full. It isn't always the case
--- that each key value in the left table corresponds to exactly on record in
--- the key column of the right table.

SELECT c1.name AS city, code, c2.name AS country, region, city_proper_pop
FROM cities AS c1 
INNER JOIN countries AS c2
ON c1.country_code = c2.code
ORDER BY code DESC;

SELECT c1.name AS city, code, c2.name AS country, region, city_proper_pop
FROM cities AS c1 
LEFT JOIN countries AS c2
ON c1.country_code = c2.code
ORDER BY code DESC;
--- The rows are increased.

---- Left join (2)

SELECT c.name AS country, local_name, l.name AS language, percent
FROM countries AS c
INNER JOIN languages AS l
ON c.code = l.code
ORDER BY country DESC;

SELECT c.name AS country, local_name, l.name AS language, percent
FROM countries AS c
LEFT JOIN languages AS l
ON c.code = l.code
ORDER BY country DESC;

---- Left join (3)

SELECT name, region, gdp_percapita
FROM countries AS c
LEFT JOIN economies AS e
ON c.code = e.code
WHERE year=2010;

SELECT region, AVG(gdp_percapita) AS avg_gdp
FROM countries AS c
LEFT JOIN economies AS e
ON c.code = e.code
WHERE year=2010
GROUP BY region
ORDER BY avg_gdp DESC;


---- Right join

SELECT cities.name AS city, urbanarea_pop, countries.name AS country,
indep_year, languages.name AS language, percent
FROM languages
RIGHT JOIN countries
ON languages.code = countries.code
RIGHT JOIN cities
ON countries.code = cities.country_code
ORDER BY city, language;


----- FULL JOINs
--- last type of the outer joins. 

---- Full join

SELECT name AS country, code, region, basic_unit
FROM countries
FULL JOIN currencies 
USING (code)
WHERE region = 'North America' OR region IS NULL
ORDER BY region;

SELECT name AS country, code, region, basic_unit
FROM countries
LEFT JOIN currencies 
USING (code)
WHERE region = 'North America' OR region IS NULL
ORDER BY region;

SELECT name AS country, code, region, basic_unit
FROM countries
INNER JOIN currencies 
USING (code)
WHERE region = 'North America' OR region IS NULL
ORDER BY region;


---- Full join (2)

SELECT countries.name, code, languages.name AS language
FROM languages
FULL JOIN countries
USING (code)
WHERE countries.name LIKE 'V%' OR countries.name IS NULL
ORDER BY countries.name;

SELECT countries.name, code, languages.name AS language
FROM languages
LEFT JOIN countries
USING (code)
WHERE countries.name LIKE 'V%' OR countries.name IS NULL
ORDER BY countries.name;

SELECT countries.name, code, languages.name AS language
FROM languages
INNER JOIN countries
USING (code)
WHERE countries.name LIKE 'V%' OR countries.name IS NULL
ORDER BY countries.name;


---- Full join (3)

SELECT c1.name AS country, region, l.name AS language,
basic_unit, frac_unit
FROM countries AS c1
FULL JOIN languages AS l
USING (code)
FULL JOIN currencies AS c2
USING (code)
WHERE region LIKE 'M%esia';


----- CROSSing the rubicon
--- Creates all possible combinations of two tables.

---- A table of two cities

SELECT c.name AS city, l.name AS languages
FROM cities AS c
CROSS JOIN languages AS l
WHERE c.name LIKE 'Hyder%';

SELECT c.name AS city, l.name AS languages
FROM cities AS c
INNER JOIN languages AS l
ON c.country_code = l.code
WHERE c.name LIKE 'Hyder%';


---- Outer challenge

SELECT c.name AS country, region, life_expectancy AS life_exp
FROM countries AS c
LEFT JOIN populations AS p
ON c.code = p.country_code
WHERE year = 2010
ORDER BY life_exp 
LIMIT 5;


------ Set theory clauses
--- Venn diagrams and introduction to union, union all, intersect, and except clauses.
--- Semi joins and anti-joins.


----- State of the UNION
--- Union includes every records in both tables but does not double count.
--- but Union All replicates. INTERSECT results in only those found in both
--- of the two tables. EXCEPT results in only those records in one table but not
--- the other.

--- UNIONs stack records on top of each other from one table to the next

---- Union

--- to create a table from a table 
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


---- Union (2)

SELECT country_code
FROM cities
UNION
SELECT code
FROM currencies
ORDER BY country_code;

---- Union all

SELECT code, year
FROM economies
UNION ALL
SELECT country_code, year
FROM populations
ORDER BY code, year
--- There are duplicates!


----- INTERSECTional data science
--- When INTERSECT looks at 2 columns it includes both columns in the search.
--- INTERSECT looks for records in common, not individual key fields like what a
--- join does to match.

---- Intersect

SELECT code, year
FROM economies
INTERSECT
SELECT country_code, year
FROM populations
ORDER BY code, year;

----- Intersect (2)

SELECT name
FROM countries
INTERSECT
SELECT name
FROM cities;


----- EXCEPTional
--- EXCEPT allows you to include only the records that are in one 
--- table but not the other.

---- Except

SELECT name 
FROM cities
EXCEPT
SELECT capital
FROM countries
ORDER BY name;

---- Except (2)

SELECT capital 
FROM countries
EXCEPT
SELECT name
FROM cities
ORDER BY capital;


----- Semi-joins and Anti-joins
--- The 6 joins so far are additive joins in that they add columns to the original
--- left table. The last ones use a right table to determine which records to keep in
--- in the left table. 

--- **Semi join chooses records in the first table where a condition 
--- is met in a second table. An anti-join chooses records in the first table where 
--- condition is not met in the second table.

-- EXAMPLES --
SELECT president, country, continent
FROM presidents
WHERE country IN (
	SELECT name
	FROM states
	WHERE indep_year < 1800
);

SELECT president, country, continent
FROM presidents
WHERE continent LIKE '%America'
AND country NOT IN (
	SELECT name
	FROM states
	WHERE indep_year < 1800
);


---- Semi-join

SELECT * 
FROM countries
WHERE region = 'Middle East';

SELECT DISTINCT name
FROM languages
ORDER BY name;

SELECT DISTINCT name
FROM languages
WHERE code IN (
	SELECT code
	FROM countries
	WHERE region = 'Middle East'
)
ORDER BY name;


---- Relating semi-join to a tweaked inner join

--- Sometimes problems solved with semi-joins can also 
--- be solved using an inner join.

SELECT DISTINCT languages.name AS language
FROM languages
INNER JOIN countries
ON languages.code = countries.code
WHERE region = 'Middle East'
ORDER BY language;


---- Diagnosing problems using anti-join

--- Another powerful join in SQL is the anti-join. It is particularly 
--- useful in identifying which records are causing an incorrect number 
--- of records to appear in join queries.

SELECT COUNT(*)
FROM countries
WHERE continent = 'Oceania'

SELECT c1.code, name, basic_unit AS currency
FROM countries AS c1
INNER JOIN currencies AS c2
ON c1.code = c2.code
WHERE continent = 'Oceania';

SELECT code, name
FROM countries
WHERE continent = 'Oceania'
AND code NOT IN(
	SELECT code
	FROM currencies
	WHERE continent = 'Oceania'
);


---- Set theory challenge
--- Identify the country codes that are included in either economies 
--- or currencies but not in populations.

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


------ Subqueries
----- Subqueries inside WHERE and SELECT clauses
--- The most common type of subquery is one inside of a WHERE statement.

SELECT name, fert_rate
FROM states
WHERE continent = 'Asia'
AND fert_rate < (
	SELECT AVG(fert_rate)
	FROM states
);


SELECT continent, Count(*)
from states
WHERE continent IN (
	SELECT DISTINCT continent
	FROM prime_ministers
)
group by continent
--- Is the same with

SELECT DISTINCT continent,(
	SELECT COUNT(*)
	FROM states
	WHERE prime_ministers.continent = states.continent) AS countries_num
FROM prime_ministers;


)

---- Subquery inside where

SELECT AVG(life_expectancy)
FROM populations
WHERE year = 2015

SELECT *
FROM populations
WHERE year = 2015 AND life_expectancy > 1.15 * (
	SELECT AVG(life_expectancy)
	FROM populations
	WHERE year=2015
)


---- Subquery inside where (2)

SELECT name, country_code, urbanarea_pop
FROM cities
WHERE name IN(
	SELECT capital
	FROM countries
)
ORDER BY urbanarea_pop DESC;


----- Subquery inside select
---some queries can be written using either a join or a subquery.

SELECT countries.name AS country, COUNT(*) AS cities_num
FROM cities
INNER JOIN countries
ON countries.code = cities.country_code
GROUP BY country
ORDER BY cities_num DESC, country
LIMIT 9;

SELECT countries.name AS country, (SELECT COUNT(*) AS cities_num
								  FROM cities
								  WHERE countries.code = cities.country_code
								  ) AS cities_num
FROM countries
ORDER BY cities_num DESC, country
LIMIT 9;


----- Subquery inside FROM clause

SELECT continent, MAX(women_parli_perc) AS max_perc
FROM states
WHERE continent IN (SELECT continent
					FROM monarchs

)
GROUP BY continent
ORDER BY continent
--- is the same with


SELECT DISTINCT monarchs.continent, subquery.max_perc
FROM monarchs, (SELECT continent, MAX(women_parli_perc) AS max_perc
			   FROM states
			   GROUP BY continent) AS subquery
WHERE monarchs.continent = subquery.continent
ORDER BY continent;


---- Subquery inside from

SELECT countries.local_name, COUNT(*) as lang_num
FROM countries
INNER JOIN languages
ON languages.code = countries.code
GROUP BY countries.code
ORDER BY lang_num DESC;
--- it is the same with

SELECT countries.local_name, subquery.lang_num
FROM countries, (SELECT code, COUNT(*) AS lang_num
				FROM languages
				GROUP BY code) AS subquery
WHERE countries.code = subquery.code
ORDER BY lang_num DESC;

---- Advanced subquery


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


---- Subquery challenge

SELECT code, inflation_rate, unemployment_rate
FROM economies
WHERE year = 2015 AND code NOT IN (SELECT code 
								  FROM countries
								  WHERE gov_form = 'Constitutional Monarchy' 
								   OR gov_form LIKE '%Republic')
ORDER BY inflation_rate;


----- Course review

---- Final challenge
SELECT DISTINCT name, total_investment, imports
FROM countries AS c
LEFT JOIN economies AS e
ON (c.code = e.code AND c.code IN (SELECT l.code
								  FROM languages AS l
								  WHERE official = 'true'))
WHERE region = 'Central America' 
AND year = 2015
ORDER BY name;

/*
SELECT DISTINCT c.name, total_investment, imports
FROM countries AS c
LEFT JOIN economies AS e
ON c.code = e.code 
LEFT JOIN languages as l
ON c.code = l.code
WHERE region = 'Central America' AND official = 'true' 
AND year = 2015
ORDER BY name;*/ --- Same with the previous one.

---- Final challenge(2)

SELECT region, continent, AVG(fertility_rate) AS avg_fert_rate
FROM countries AS c
INNER JOIN populations AS p
ON c.code = p.country_code
WHERE year = 2015
GROUP BY region,continent
ORDER BY avg_fert_rate;


---- Final challenge (3)

SELECT name, country_code, city_proper_pop, metroarea_pop,
city_proper_pop / metroarea_pop * 100 AS city_perc
FROM cities
WHERE name IN (SELECT capital
			  FROM countries
			  WHERE (continent = 'Europe' OR continent LIKE '%America')
			  AND metroarea_pop IS NOT NULL)
ORDER BY city_perc DESC
LIMIT 10;






