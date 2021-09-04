# Parsing and Manipulating Text

## Reformatting string and character data

The string concatenation allows you to merge two or more strings
together to form a single cobined string. ... || ' ' || ...

PostgreSQL also has a bulit-in funtion -> CONCAT(..., ' ', ...)

You can concatenate both string and non-string data.

UPPER(), LOWER(), INITCAP(), REPLACE(where, what, with), REVERSE()

### Concatenating strings

```
SELECT first_name || ' ' || last_name || ' <' || email || '>' AS full_email 
FROM customer
```

```
SELECT CONCAT(first_name, ' ', last_name,  ' <', email, '>') AS full_email 
FROM customer
```

### Changing the case of string data

```
SELECT UPPER(name)  || ': ' || INITCAP(title) AS film_category, 
       LOWER(description) AS description
FROM film AS f 
INNER JOIN film_category AS fc 
ON f.film_id = fc.film_id 
INNER JOIN category AS c 
ON fc.category_id = c.category_id;
```

### Replacing string data

```
SELECT REPLACE(title, ' ', '_') AS title
FROM film; 
```

## Parsing string and character data

CHAR_LENGTH() and LENGTH() are the same. POSITION counts the characters
before the search string located. STRPOS does the same but the syntax is
different.

LEFT(n) first n chars of the string. RIGHT(n) last n chars. SUBSTRING() 
extracts a substring from text data. SUBSTR does the same. 

SUBSTRING(... FROM POSITION('...' IN ...)+1 FOR ...(...))

SUBSTRING(... FROM 0 FOR POSITION('...' IN ...))

### Determining the length of strings

```
SELECT title, description, LENGTH(description) AS desc_len
FROM film;
```

### Truncating strings

```
SELECT LEFT(description, 50) AS short_desc
FROM film AS f; 
```

### Extracting substrings from text data

```
SELECT SUBSTRING(address FROM POSITION(' ' IN address)+1 FOR CHAR_LENGTH(address))
FROM 
  address;
```

### Combining functions for string manipulation

```
SELECT LEFT(email, POSITION('@' IN email)-1) AS username,
SUBSTRING(email FROM POSITION('@' IN email)+1 FOR CHAR_LENGTH(email)) AS domain
FROM customer;  
```

## Truncating and padding string data

TRIM removes characters from a string, LTRIM and RTRIM. LPAD appends a character or
string to another string by a specified number of chars. This is useful when you need
a field to be the same length and want to pad the string with a certain char like sapce or
tab. (RPAD) 

### Padding

``` 
SELECT RPAD(first_name, LENGTH(first_name)+1) || last_name AS full_name
FROM customer;
```

```
SELECT first_name || LPAD(last_name, LENGTH(last_name)+1) AS full_name
FROM customer; 
```

```
SELECT RPAD(first_name, LENGTH(first_name)+1) 
    || RPAD(last_name, LENGTH(last_name)+2, ' <') 
    || RPAD(email, LENGTH(email)+1, '>') AS full_email
FROM customer; 
```

### The TRIM function

```
SELECT CONCAT(UPPER(name), ': ', title) AS film_category, TRIM(LEFT(description, 50)) AS film_desc
FROM film AS f 
INNER JOIN film_category AS fc 
ON f.film_id = fc.film_id 
INNER JOIN category AS c 
ON fc.category_id = c.category_id;
```

### Putting it all together

```
SELECT CONCAT(UPPER(name), ': ', title) AS film_category, 
       TRIM(LEFT(description, 50)) AS film_desc
FROM film AS f 
INNER JOIN film_category AS fc 
ON f.film_id = fc.film_id 
INNER JOIN category AS c
ON fc.category_id = c.category_id;
```