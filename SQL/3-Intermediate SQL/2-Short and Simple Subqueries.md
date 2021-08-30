# Short and Simple Subqueries

## WHERE are the Subqueries?

Additional SELECT statement in the query. They are useful for intermediary transformation before
selecting, filtering and calculating.

Subqueries can be placed in;

* SELECT
* FROM
* WHERE
* GROUP BY clause

By subqueries you can compare summarized values to detailed data.

The subqueries in the WHERE clause are useful for filtering results.

### Filtering using scalar subqueries

```
SELECT 
	3 * AVG(home_goal + away_goal)
FROM matches_2013_2014;
```