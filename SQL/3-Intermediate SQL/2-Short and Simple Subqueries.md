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

```
SELECT date, home_goal,	away_goal
FROM  matches_2013_2014
WHERE (home_goal + away_goal) > (SELECT 3 * AVG(home_goal + away_goal)
        			 FROM matches_2013_2014); 
```

### Filtering using a subquery with a list

Excluding values from subquery in main query.

```
SELECT team_long_name, team_short_name
FROM team 
WHERE team_api_id NOT IN (SELECT DISTINCT hometeam_id 
			  FROM match);
```

### Filtering with more complex subquery conditions

Including all values from subquery in main query.

```
SELECT team_long_name, team_short_name
FROM team
WHERE team_api_id IN (SELECT hometeam_id
		      FROM match
       	 	      WHERE home_goal >= 8);
```

## Subqueries in FROM

You can query transformed data with subquery in FROM. 

Also you can calculate aggregates of aggregates. Such as finding the top
averages.

Subqueries in FROM should have aliases.

You can create multiple subqueries in one FROM statement but you should join
them. Or you can join a subquery to any existing table.

### Joining Subqueries in FROM

```
SELECT name AS country_name, COUNT(c.id) AS matches
FROM country AS c
INNER JOIN (SELECT country_id, id 
            FROM match
            WHERE (home_goal + away_goal) >= 10) AS sub
ON c.id = sub.country_id
GROUP BY country_name;
```

### Building on Subqueries in FROM

```
SELECT country, date, home_goal, away_goal
FROM (SELECT c.name AS country, m.date, m.home_goal, m.away_goal,
      (m.home_goal + m.away_goal) AS total_goals
      FROM match AS m
      LEFT JOIN country AS c
      ON m.country_id = c.id) AS subq
WHERE total_goals >= 10;
```

## Subqueries in SELECT

Can be used to bring summary values to a detailed data set. Subqueries in
SELECT return a single, aggregate value in an ungrouped data. Deviations from
the average can be calculated using subqueries in SELECT. SELECT subqueries
need to return a single value. The value will be applied identically in each 
row in the data set. Main and subquery should have the same WHERE filters.

### Add a subquery to the SELECT clause

```
SELECT l.name AS league, 
       ROUND(AVG(m.home_goal + m.away_goal), 2) AS avg_goals,
       (SELECT ROUND(AVG(home_goal + away_goal), 2) 
        FROM match
        WHERE season = '2013/2014') AS overall_avg
FROM league AS l
LEFT JOIN match AS m
ON l.country_id = m.country_id
WHERE season = '2013/2014'
GROUP BY league;
```

### Subqueries in Select for Calculations

```
SELECT l.name AS league,
	ROUND(AVG(m.home_goal + m.away_goal),2) AS avg_goals,
	ROUND(AVG(m.home_goal + m.away_goal) - (SELECT AVG(home_goal + away_goal)
		 				FROM match 
         					WHERE season = '2013/2014'),2) AS diff
FROM league AS l
LEFT JOIN match AS m
ON l.country_id = m.country_id
WHERE season = '2013/2014'
GROUP BY l.name;
```

## Subqueries everywhere! And best practices!

### ALL the subqueries EVERYWHERE

```
SELECT 	m.stage,
    ROUND(AVG(m.home_goal + m.away_goal),2) AS avg_goals,
    ROUND((SELECT AVG(home_goal + away_goal) 
           FROM match 
           WHERE season = '2012/2013'),2) AS overall
FROM match AS m
WHERE season = '2012/2013'
GROUP BY stage;
```

### Add a subquery in FROM

```
SELECT 	stage, ROUND(avg_goals,2) AS avg_goals
FROM (SELECT stage,
      AVG(home_goal + away_goal) AS avg_goals
      FROM match
      WHERE season = '2012/2013'
      GROUP BY stage) AS s
WHERE s.avg_goals > (SELECT AVG(home_goal + away_goal) 
                     FROM match WHERE season = '2012/2013');
```

### Add a subquery in SELECT

```
SELECT stage, ROUND(avg_goals,2) AS avg_goal,
      (SELECT AVG(home_goal + away_goal) FROM match WHERE season = '2012/2013') AS overall_avg
FROM (SELECT stage,
             AVG(home_goal + away_goal) AS avg_goals
      FROM match
      WHERE season = '2012/2013'
      GROUP BY stage) AS s
WHERE s.avg_goals > (SELECT AVG(home_goal + away_goal) 
                     FROM match WHERE season = '2012/2013');
```