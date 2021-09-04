# Working with DATE/TIME Functions and Operators

## Overview of basic arithmetic operators

When you subtract date values the result is an integer data type. You can also
add integers to date values. The implied precision is days. 

AGE function is used to calculate the difference between two timestamps and returns 
an INTERVAL.

You can add integers to dates but not timestamps. To add days to timestamps use
INTERVAL '... day'

### Adding and subtracting date and time values

```
SELECT f.title, f.rental_duration, r.return_date - r.rental_date AS days_rented
FROM film AS f
     INNER JOIN inventory AS i ON f.film_id = i.film_id
     INNER JOIN rental AS r ON i.inventory_id = r.inventory_id
ORDER BY f.title;
```

```
SELECT f.title, f.rental_duration,
	AGE(r.return_date, r.rental_date) AS days_rented
FROM film AS f
	INNER JOIN inventory AS i ON f.film_id = i.film_id
	INNER JOIN rental AS r ON i.inventory_id = r.inventory_id
ORDER BY f.title;
```

### INTERVAL arithmetic

```
SELECT f.title, INTERVAL '1' day * f.rental_duration, r.return_date - r.rental_date AS days_rented
FROM film AS f
    INNER JOIN inventory AS i ON f.film_id = i.film_id
    INNER JOIN rental AS r ON i.inventory_id = r.inventory_id
WHERE r.return_date IS NOT NULL
ORDER BY f.title;
```

### Calculating the expected return date

```
SELECT f.title, r.rental_date, f.rental_duration,
       INTERVAL '1' day * f.rental_duration + r.rental_date AS expected_return_date,
       r.return_date
FROM film AS f
    INNER JOIN inventory AS i ON f.film_id = i.film_id
    INNER JOIN rental AS r ON i.inventory_id = r.inventory_id
ORDER BY f.title;
```

## Functions for retrieving current date/time

CAST() function allows you to convert one data type to another

```
SELECT CAST(... as ...);
```

CURRENT_TIMESTAMP (PostgreSQL) or NOW(), CURRENT_DATE, CURRENT_TIME. NOW()
and CURRENT_TIMESTAMP can be used interchangeably

### Working with the current date and time

```
SELECT NOW();
```

```
SELECT CURRENT_DATE;
```

```
SELECT CAST( NOW() AS timestamp)
```

```
SELECT CURRENT_DATE,
CAST(NOW()  AS date )
```

### Manipulating the current date and time

```
SELECT CURRENT_TIMESTAMP::timestamp AS right_now;
```

```
SELECT CURRENT_TIMESTAMP::timestamp AS right_now,
       INTERVAL '5 days' + CURRENT_TIMESTAMP AS five_days_from_now;
```

```
SELECT CURRENT_TIMESTAMP(0)::timestamp AS right_now,
       INTERVAL '5 days' + CURRENT_TIMESTAMP(0) AS five_days_from_now;
```

### Extracting and transforming date/ time data

Manipulating timestamp data and creating new columns. 

* EXTRACT(field FROM source)

* DATE_PART('field', source)

Field parameter is and identifier that indicates what sub-field that you want to
extract from the source; year, month, quarter, day of week, etc.

e-commerce applications need the timestamp information of the payments. You would
want to aggregate this data to use for training a model, reporting or trend analysis.

DATE_TRUNC() function will truncate timestamp or interval data types. DATE_TRUNC
return an interval or timestamp.

### Using EXTRACT

```
SELECT EXTRACT(dow FROM rental_date) AS dayofweek, COUNT(*) as rentals 
FROM rental 
GROUP BY 1;
```

### Using DATE_TRUNC

```
SELECT DATE_TRUNC('year', rental_date) AS rental_year
FROM rental;
```

```
SELECT DATE_TRUNC('month', rental_date) AS rental_month
FROM rental;
```

```
SELECT DATE_TRUNC('day', rental_date) AS rental_day 
FROM rental;
```


```
SELECT DATE_TRUNC('day', rental_date) AS rental_day, COUNT(*) AS rentals 
FROM rental
GROUP BY 1;
```

### Putting it all together

```
SELECT c.first_name || ' ' || c.last_name AS customer_name, f.title, r.rental_date,
       EXTRACT(dow FROM r.rental_date) AS dayofweek, AGE(r.return_date, r.rental_date) AS rental_days,
       CASE WHEN DATE_TRUNC('day', AGE(r.return_date, r.rental_date)) > 
       f.rental_duration * INTERVAL '1' day  THEN TRUE 
       ELSE FALSE END AS past_due 
FROM film AS f 
INNER JOIN inventory AS i ON f.film_id = i.film_id 
INNER JOIN rental AS r ON i.inventory_id = r.inventory_id 
INNER JOIN customer AS c ON c.customer_id = r.customer_id 
WHERE r.rental_date BETWEEN CAST('2005-05-01' AS DATE) AND CAST('2005-05-01' AS DATE) + INTERVAL '90 day';
```

|| ' ' || for concatinating two columns.