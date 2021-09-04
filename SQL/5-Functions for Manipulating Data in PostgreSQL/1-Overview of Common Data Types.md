# Overview of Common Data Types

## Welcome!

Text data types like CHAR and VARCHAR allow for a fixed or varying number of 
characters and string data. Numeric data types like INT and DECIMAL.

PostgreSQL stores information about all database objects in a system database
called INFORMATION_SCHEMA. By querying this database you can determine information 
about the database including data types of columns.

### Getting information about your database

Use INFORMATION_SCHEMA.columns or tables

```
SELECT * 
FROM INFORMATION_SCHEMA.TABLES
WHERE table_schema = 'public';
```

```
SELECT * 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE table_name = 'actor';
```

### Determining data types

```
SELECT column_name, data_type
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE table_name = 'customer';
```

## Date and time data types

INTERVALs are useful when you want to do arithmetic on date time columns.

### Interval data types

```
SELECT rental_date, return_date, 
       rental_date + INTERVAL '3 days' AS expected_return_date
FROM rental;
```

## Working with ARRAYs

To create a ARRAY type, add [] to the end of the data type. To insert use {}
To select ARRAYs use indexing. Note that indexing in SQL starts at 1. Indexing can also
be used in WHERE clause to filter. 

ANY function allows you to search an array for a value and return a record if it finds 
a match. (in any value in the array.) Its alternative is CONTAINS aperator. (@> ARRAY["..."])

### Accessing data in an ARRAY

```
SELECT title, special_features 
FROM film
WHERE special_features[1] = 'Trailers';
```

```
SELECT title, special_features 
FROM film
WHERE special_features[2] = 'Deleted Scenes';
```

### Searching an ARRAY with ANY

ANY is more flexible.

```
SELECT title, special_features 
FROM film 
WHERE 'Trailers' = ANY(special_features);
```

### Searching an ARRAY with @>

```
SELECT title, special_features 
FROM film 
WHERE special_features @> ARRAY['Deleted Scenes'];
```