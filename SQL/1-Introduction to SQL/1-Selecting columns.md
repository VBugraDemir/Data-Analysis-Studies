# Selecting columns


## Tables
```
SELECT *
FROM people;
```

## Onboarding | Query Result
```
SELECT name 
FROM people;
```

## Onboarding | Errors
```
SELECT 'DataCamp <3 SQL'
AS result;
```

## Onboarding | Bullet Exercises
```
SELECT 'SQL is cool'
AS result;
```


## SELECTing single columns
```
SELECT title
FROM films;
```
```
SELECT release_year
FROM films;
```
```
SELECT release_year
FROM films;
```


## SELECTing multiple columns
```
SELECT title, release_year
FROM films;
```
```
SELECT title, release_year, country
FROM films;
```

## SELECT DISTINCT
Often your results will include many duplicate values. If you want to select all the unique 
values from a column, you can use the DISTINCT keyword.
```
SELECT DISTINCT country
FROM films;
```
```
SELECT DISTINCT certification
FROM films;
```
```
SELECT DISTINCT role
FROM roles;
```

## Learning to COUNT
The COUNT statement returns the number of rows in one or more columns.
```
SELECT COUNT(*)
FROM reviews;
```

