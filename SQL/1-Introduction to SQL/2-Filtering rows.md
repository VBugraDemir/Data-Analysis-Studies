
# Filtering rows


## Filtering results
```
SELECT title
FROM films
WHERE release_year > 2000;
```

## Simple filtering of numeric values
```
SELECT *
FROM films
WHERE release_year = 2016
```
```
SELECT COUNT(*)
FROM films
WHERE release_year < 2000
```
```
SELECT title, release_year
FROM films
WHERE release_year > 2000
```

## Simple filtering of text
```
SELECT *
FROM films
WHERE language = 'French';
```
```
SELECT name, birthdate
FROM people
WHERE birthdate = '1974-11-11'
```
```
SELECT COUNT(*)
FROM films
WHERE language = 'Hindi'
```
```
SELECT *
FROM films
WHERE certification = 'R'
```


## WHERE AND
You can build up your WHERE queries by combining multiple conditions with the AND keyword.
```
SELECT title, release_year
FROM films
WHERE language = 'Spanish'
AND release_year < 2000
```
```
SELECT *
FROM films
WHERE language = 'Spanish'
AND release_year > 2000
```
```
SELECT *
FROM films
WHERE language = 'Spanish'
AND release_year > 2000
AND release_year < 2010
```

## WHERE AND OR
```
SELECT title
FROM films
WHERE (release_year = 1994 OR release_year = 1995)
AND (certification = 'PG' OR certification = 'R');
```

## WHERE AND OR (2)
```
SELECT title, release_year
FROM films
WHERE (release_year >= 1990 AND release_year < 2000)
AND (language = 'French' OR language = 'Spanish')
AND gross > 2000000
```

## BETWEEN
Checking for ranges like this is very common, so in SQL the BETWEEN keyword provides 
a useful shorthand for filtering values within a specified range. 
```
SELECT title
FROM films
WHERE release_year
BETWEEN 1994 AND 2000;
```

## BETWEEN (2)
```
SELECT title, release_year
FROM films
WHERE release_year BETWEEN 1990 AND 2000
AND budget > 100000000
AND language = 'Spanish';
```

## WHERE IN
The IN operator allows you to specify multiple values in a WHERE clause, making it easier 
and quicker to specify multiple OR conditions
```
SELECT title, release_year
FROM films
WHERE release_year IN (1990, 2000)
AND duration > 120
```
```
SELECT title, language 
FROM films
WHERE language IN ('Spanish', 'English', 'French')
```
```
SELECT title, certification
FROM films
WHERE certification IN ('NC-17', 'R');
```

## Introduction to NULL and IS NULL
In SQL, NULL represents a missing or unknown value. You can check for NULL values using 
the expression IS NULL. 
```
SELECT COUNT(*)
FROM people
WHERE birthdate IS NULL;
```
```
SELECT name
FROM people
WHERE birthdate IS NOT NULL;
```
## NULL and IS NULL
```
SELECT name
FROM people
WHERE deathdate IS NULL
```
```
SELECT title
FROM films 
WHERE budget IS NULL
```
```
SELECT COUNT(title)
FROM films
WHERE language IS NULL
```

## LIKE and NOT LIKE
The "%" wildcard will match zero, one, or many characters in text. The "_" wildcard will match 
a single character. 
```
SELECT name
FROM people
WHERE name LIKE 'B%'
```
```
SELECT name
FROM people
WHERE name LIKE '_r%'
```
```
SELECT name
FROM people
WHERE name NOT LIKE 'A%'
```