# Sorting and grouping

## ORDER BY
ORDER BY keyword is used to sort results in ascending or descending order according to the 
values of one or more columns.
```
SELECT title
FROM films
ORDER BY release_year DESC;
```

## Sorting single columns
```
SELECT name
FROM people
ORDER BY name;
```
```
SELECT name
FROM people
ORDER BY birthdate;
```
```
SELECT name, birthdate
FROM people
ORDER BY birthdate;
```

## Sorting single columns (2)
```
SELECT title
FROM films
WHERE release_year IN (2000, 2012)
ORDER BY release_year;
```
```
SELECT *
FROM films
WHERE release_year <> 2015
ORDER BY duration;
```
```
SELECT title, gross
FROM films
WHERE title LIKE 'M%'
ORDER BY title;
```

## Sorting single columns (DESC)
```
SELECT imdb_score, film_id
FROM reviews
ORDER BY imdb_score DESC
```
```
SELECT title
FROM films
ORDER BY title DESC
```
```
SELECT title, duration
FROM films
ORDER BY duration DESC
```

## Sorting multiple columns
It will sort by the first column specified, then sort by the next, then the next, and so on.
```
SELECT birthdate, name
FROM people
ORDER BY birthdate, name;
```
```
SELECT release_year, duration, title 
FROM films
ORDER BY release_year, duration;
```
```
SELECT certification, release_year, title
FROM films
ORDER BY certification, release_year;
```
```
SELECT name, birthdate
FROM people
ORDER BY name, birthdate
```

## GROUP BY 
Commonly, GROUP BY is used with aggregate functions like COUNT() or MAX(). Note that GROUP 
BY always goes after the FROM clause!
```
SELECT sex, count(*)
FROM employees
GROUP BY sex;
```

## GROUP BY practice
SQL will return an error if you try to SELECT a field that is not in your GROUP BY clause 
without using it to calculate some kind of value about the entire group.
```
SELECT release_year, COUNT(*)
FROM films 
GROUP BY release_year
```
```
SELECT release_year, AVG(duration)
FROM films 
GROUP BY release_year
```
```
SELECT release_year, MAX(budget)
FROM films 
GROUP BY release_year
```
```
SELECT imdb_score, COUNT(*)
FROM reviews 
GROUP BY imdb_score
```

## GROUP BY practice (2)
```
SELECT release_year, MIN(gross)
FROM films
GROUP BY release_year
```
```
SELECT language, SUM(gross)
FROM films
GROUP BY language
```
```
SELECT country, SUM(budget)
FROM films
GROUP BY country
```
```
SELECT release_year, country, MAX(budget)
FROM films
GROUP BY release_year,country
ORDER BY release_year, country
```
```
SELECT country, release_year, MIN(gross)
FROM films
GROUP BY release_year, country
ORDER BY country, release_year
```

## HAVING a great time
In SQL, aggregate functions can't be used in WHERE clauses. This means that if you want to 
filter based on the result of an aggregate function, you need HAVING!
```
SELECT release_year,Count(title) 
FROM films
Group by release_year
Having Count(title) >200;
```

## All together now
```
SELECT release_year, AVG(budget) AS avg_budget, AVG(gross) AS avg_gross
FROM films
WHERE release_year > 1990
GROUP BY release_year
HAVING AVG(budget) > 60000000
ORDER BY avg_gross DESC;
```

## All together now (2)
```
SELECT country, AVG(budget) as avg_budget,  AVG(gross) as avg_gross
FROM films
GROUP BY country
HAVING COUNT(*) > 10 
ORDER BY country
LIMIT 5
```

## A taste of things to come (JOIN)
```
SELECT title, imdb_score
FROM films
JOIN reviews
ON films.id = reviews.film_id
WHERE title = 'To Kill a Mockingbird';
```