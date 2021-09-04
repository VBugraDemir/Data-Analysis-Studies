# Full-text Search and PostgresSQL Extensions

## Introduction to full-text search

For full text search use to_tsvector(column_name) @@ to_tsquery('...')
to convert data to a tsvector data type which is a sorted list of words that have
been normalized into variants of the same word. These are called 'lexemes'.

### A review of the LIKE operator

```
SELECT *
FROM film
-- Select only records that contain the word 'GOLD'
WHERE title LIKE '%GOLD%'; -- 'GOLD%' or '%GOLD'
```

### What is a tsvector?

```
SELECT to_tsvector(description)
FROM film;
```

### Basic full-text search

```
SELECT title, description
FROM film 
WHERE to_tsvector(title) @@ to_tsquery('elf');
```

## Extending PostgreSQL

User defined data types. Data type is created by using the CREATE TYPE command.

Enumerated data types (ENUM) list of values that are never going to change.

User-defined funtion: You can bundle several SQL queries and statements together
into a single package using the CREATE FUNCTION command.

* pg_type is a system table to get information about all data type available in database.
Also you can use INFORMATION_SCHEMA system database by querying data_type and udt_name.

### User-defined data types

```
CREATE TYPE compass_position AS ENUM ('North', 
  				      'South',
  				      'East', 
  				      'West');

SELECT *
FROM pg_type
WHERE typname='compass_position';
```

### Getting info about user-defined data types

```
SELECT column_name, data_type, udt_name
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE table_name ='film' AND column_name='rating';
```

```
SELECT *
FROM pg_type 
WHERE typname='mpaa_rating'
```

### User-defined functions in Sakila

```
SELECT f.title, i.inventory_id, inventory_held_by_customer(i.inventory_id) as held_by_cust
FROM film as f 
INNER JOIN inventory AS i ON f.film_id=i.film_id 
WHERE
inventory_held_by_customer(i.inventory_id) IS NOT NULL
```

## Intro to PostgreSQL extensions

To see what extenstions are available in PostgreSQL distribution, quer the pg_available_extensions
system view. pg_extensions for installed extensions.

You can load and enable extensions: CREATE EXTENSION IF NOT EXISTS ...;

Levenshtein is the number of edits required for the strings to be a perfect match

pg_trgm extension proveides functions and operators to determine the similarity of two
strings.

### Enabling extensions

```
CREATE EXTENSION IF NOT EXISTS pg_trgm;
SELECT * 
FROM pg_extension;
```

### Measuring similarity between two strings

```
SELECT title, description, similarity(title, description)
FROM film
```

### Levenshtein distance examples

```
SELECT title, description, levenshtein(title, 'JET NEIGHBOR') AS distance
FROM film
ORDER BY 3
```

### Putting it all together

```
SELECT title, description, similarity(description, 'Astounding Drama')
FROM film 
WHERE to_tsvector(description) @@ to_tsquery('Astounding & Drama') 
ORDER BY similarity DESC;
```