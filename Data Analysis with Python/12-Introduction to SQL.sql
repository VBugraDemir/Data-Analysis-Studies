-- Introduction to SQL

--- 1-Selecting columns

---- Welcome to the course!
------ Onboarding | Tables

SELECT *
FROM people;

------ Onboarding | Query Result

SELECT name 
FROM people;

------ Onboarding | Errors

SELECT 'DataCamp <3 SQL'
AS result;

------ Onboarding | Bullet Exercises

SELECT 'SQL'
AS result;

SELECT 'SQL is'
AS result;

SELECT 'SQL is cool'
AS result;

------ SELECTing single columns
SELECT title
FROM films;

SELECT release_year
FROM films;

SELECT release_year
FROM films;

------ SELECTing multiple columns

SELECT title, release_year
FROM films;

SELECT title, release_year, country
FROM films;

------ SELECT DISTINCT

SELECT DISTINCT country
FROM films;

SELECT DISTINCT certification
FROM films;

SELECT DISTINCT role
FROM roles;

------ Learning to COUNT

SELECT COUNT(*)
FROM reviews;

------ Practice with COUNT

SELECT COUNT(*)
FROM people

SELECT COUNT(birthday)
FROM people;

SELECT COUNT(DISTINCT birthdate)
FROM people;

SELECT COUNT(DISTINCT language)
FROM films;

SELECT COUNT(DISTINCT country)
FROM films;

--- 2-Filtering rows

------ Filtering results

SELECT title
FROM films
WHERE release_year > 2000;

------ Simple filtering of numeric values

SELECT *
FROM films
WHERE release_year = 2016

SELECT COUNT(*)
FROM films
WHERE release_year < 2000

SELECT title, release_year
FROM films
WHERE release_year > 2000

------ Simple filtering of text

SELECT *
FROM films
WHERE language = 'French';

SELECT name, birthdate
FROM people
WHERE birthdate = '1974-11-11'

SELECT COUNT(*)
FROM films
WHERE language = 'Hindi'

SELECT *
FROM films
WHERE certification = 'R'

------ WHERE AND

SELECT title, release_year
FROM films
WHERE language = 'Spanish'
AND release_year < 2000

SELECT *
FROM films
WHERE language = 'Spanish'
AND release_year > 2000

SELECT *
FROM films
WHERE language = 'Spanish'
AND release_year > 2000
AND release_year < 2010

------ WHERE AND OR

SELECT title
FROM films
WHERE (release_year = 1994 OR release_year = 1995)
AND (certification = 'PG' OR certification = 'R');

------ WHERE AND OR (2)

SELECT title, release_year
FROM films
WHERE (release_year >= 1990 AND release_year < 2000)
AND (language = 'French' OR language = 'Spanish')
AND gross > 2000000

------ BETWEEN

SELECT title
FROM films
WHERE release_year
BETWEEN 1994 AND 2000;

------ BETWEEN (2)

SELECT title, release_year
FROM films
WHERE release_year BETWEEN 1990 AND 2000
AND budget > 100000000
AND language = 'Spanish';

------ WHERE IN

SELECT title, release_year
FROM films
WHERE release_year IN (1990, 2000)
AND duration > 120

SELECT title, language 
FROM films
WHERE language IN ('Spanish', 'English', 'French')

SELECT title, certification
FROM films
WHERE certification IN ('NC-17', 'R');

------ Introduction to NULL and IS NULL

SELECT COUNT(*)
FROM people
WHERE birthdate IS NULL;

SELECT name
FROM people
WHERE birthdate IS NOT NULL;

------ NULL and IS NULL

SELECT name
FROM people
WHERE deathdate IS NULL

SELECT title
FROM films 
WHERE budget IS NULL

SELECT COUNT(title)
FROM films
WHERE language IS NULL

------ LIKE and NOT LIKE

-------The % wildcard will match zero, one, or many characters in text.
------- The _ wildcard will match a single character. 

SELECT name
FROM people
WHERE name LIKE 'B%'

SELECT name
FROM people
WHERE name LIKE '_r%'

SELECT name
FROM people
WHERE name NOT LIKE 'A%'

----- Aggregate functions

------ Aggregate functions

SELECT SUM(duration)
FROM films;

SELECT AVG(duration)
FROM films;

SELECT MIN(duration)
FROM films;

SELECT MAX(duration)
FROM films;

------ Aggregate functions practice

SELECT SUM(gross)
FROM films;

SELECT AVG(gross)
FROM films;

SELECT MIN(gross)
FROM films;

SELECT MAX(gross)
FROM films;

------ Combining aggregate functions with WHERE

SELECT SUM(gross)
FROM films
WHERE release_year >= 2000

SELECT AVG(gross)
FROM films
WHERE title LIKE 'A%'

SELECT MIN(gross)
FROM films
WHERE release_year = 1994

SELECT MAX(gross)
FROM films
WHERE release_year BETWEEN 2000 AND 2012;

------ A note on arithmetic

SELECT (10 / 3);

SELECT (10 / 3.);

----- It's AS simple AS aliasing

SELECT title,gross - budget AS net_profit
FROM films;

SELECT title,duration/60.0 AS duration_hours
FROM films;

SELECT AVG(duration) /60.0 AS avg_duration_hours
FROM films;

----- Even more aliasing

SELECT COUNT(deathdate) * 100.0 / COUNT(*) AS percentage_dead
FROM people

SELECT MAX(release_year) - MIN(release_year)  AS difference
FROM films;

SELECT (MAX(release_year) - MIN(release_year)) / 10.0 as number_of_decades
FROM films;

---- 4-Sorting and grouping

----- ORDER BY

SELECT title
FROM films
ORDER BY release_year DESC;

----- Sorting single columns

SELECT name
FROM people
ORDER BY name;

SELECT name
FROM people
ORDER BY birthdate;

SELECT name, birthdate
FROM people
ORDER BY birthdate;

----- Sorting single columns (2)

SELECT title
FROM films
WHERE release_year IN (2000, 2012)
ORDER BY release_year;

SELECT *
FROM films
WHERE release_year <> 2015
ORDER BY duration;

SELECT title, gross
FROM films
WHERE title LIKE 'M%'
ORDER BY title;

----- Sorting single columns (DESC)

SELECT imdb_score, film_id
FROM reviews
ORDER BY imdb_score DESC

SELECT title
FROM films
ORDER BY title DESC

SELECT title, duration
FROM films
ORDER BY duration DESC

----- Sorting multiple columns

SELECT birthdate, name
FROM people
ORDER BY birthdate, name;

SELECT release_year, duration, title 
FROM films
ORDER BY release_year, duration;

SELECT certification, release_year, title
FROM films
ORDER BY certification, release_year;

SELECT name, birthdate
FROM people
ORDER BY name, birthdate

----- GROUP BY practice

SELECT release_year, COUNT(*)
FROM films 
GROUP BY release_year

SELECT release_year, AVG(duration)
FROM films 
GROUP BY release_year

SELECT release_year, MAX(budget)
FROM films 
GROUP BY release_year

SELECT imdb_score, COUNT(*)
FROM reviews 
GROUP BY imdb_score

----- GROUP BY practice (2)

SELECT release_year, MIN(gross)
FROM films
GROUP BY release_year

SELECT language, SUM(gross)
FROM films
GROUP BY language

SELECT country, SUM(budget)
FROM films
GROUP BY country

SELECT release_year, country, MAX(budget)
FROM films
GROUP BY release_year,country
ORDER BY release_year, country

SELECT country, release_year, MIN(gross)
FROM films
GROUP BY release_year, country
ORDER BY country, release_year

----- HAVING a great time

SELECT release_year
FROM films
GROUP BY release_year
HAVING COUNT(title) > 10;

----- All together now

SELECT release_year, budget, gross
FROM films
WHERE release_year > 1990;

SELECT release_year
FROM films
WHERE release_year > 1990
GROUP BY release_year;

----- All together now (2)

SELECT country, AVG(budget) as avg_budget,  AVG(gross) as avg_gross
FROM films
GROUP BY country
HAVING COUNT(*) > 10 
ORDER BY country
LIMIT 5

----- A taste of things to come

SELECT title, imdb_score
FROM films
JOIN reviews
ON films.id = reviews.film_id
WHERE title = 'To Kill a Mockingbird';
