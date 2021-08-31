# Correlated Queries, Nested Queries, and Common Table Expressions

## Correlated subqueries

Correlated subqueries use values from the outer query to generate the final results.
It is re-executed each time a new row in the final data set is returned. Correlated 
subqueries can not be executed independently since it is dependent on values in the main 
query. It is evaluated in loops once for each row. 

```
SELECT c.name AS country,
       AVG(m.home_goal + m.away_goal) AS avg_goals
FROM country AS c
LEFT JOIN match AS m
ON c.id = m.country_id
GROUP BY country
ORDER BY country
```

This query gives the same result as the below one. The entire join is replaced.

```
SELECT c.name AS country,
       (SELECT AVG(home_goal + away_goal) 
        FROM match AS m
        WHERE m.country_id = c.id) AS avg_goals
FROM country AS c
ORDER BY country
```


### Basic Correlated Subqueries
The average goal can be found for all the matches in the data set is a one 
value and can be utilized by using simple subqueries. But average goals for each
country can not be used with simple subqueries and correlated subqueries are needed.

```
SELECT main.country_id, date, main.home_goal, main.away_goal
FROM match AS main
WHERE (home_goal + away_goal) > (SELECT AVG((sub.home_goal + sub.away_goal) * 3)
         			 FROM match AS sub
        			 WHERE main.country_id = sub.country_id);
```

### Correlated subquery with multiple conditions

Selecting the highest scoring match for each country in each season.

```
SELECT main.country_id, main.date, main.home_goal, main.away_goal
FROM match AS main
WHERE (home_goal + away_goal) = (SELECT MAX(sub.home_goal + sub.away_goal)
         			 FROM match AS sub
          	 		 WHERE main.season = sub.season
               			 AND main.country_id = sub.country_id);
```

## Nested subqueries

Nested subqueries can be correlated or uncorrelated.

```
SELECT c.name AS country, AVG(home_goal+away_goal)
FROM match
INNER JOIN country AS c
ON match.country_id = c.id
WHERE season = '2011/2012'
GROUP BY country
ORDER BY country
```

The same result with nested subqueries.

```
SELECT c.name AS country, (SELECT AVG(home_goal + away_goal)
			   FROM match AS m
			   WHERE m.country_id = c.id AND id IN (SELECT id
     				     				FROM match
     				     				WHERE season = '2011/2012')) AS avg_goals
FROM country AS c
ORDER BY country
```

###  Nested simple subqueries

```
SELECT season,
       MAX(home_goal + away_goal) AS max_goals,
       (SELECT MAX(home_goal + away_goal) FROM match ) AS overall_max_goals,
       ((SELECT MAX(home_goal + away_goal) FROM match
       WHERE EXTRACT(MONTH FROM date) = 07)) AS july_max_goals
FROM match
GROUP BY season
```

### Nest a subquery in FROM

```
SELECT c.name AS country, AVG(outer_s.matches) AS avg_seasonal_high_scores
FROM country AS c
LEFT JOIN (SELECT country_id, season, COUNT(id) AS matches
	   FROM (SELECT country_id, season, id
	         FROM match
	         WHERE home_goal >= 5 OR away_goal >= 5) AS inner_s
           GROUP BY country_id, season) AS outer_s
ON c.id = outer_s.country_id
GROUP BY country;
```

## Common Table Expressions

Common table expressions are used to improve readibility and accessibility of information in
subqueries. Common table is declared before the main query, named and referenced later in 
FROM statement like any other table in database. More than one CTE can be listed one after
another with a comman between them. CTEs are run only once and then stored in memory.

### Clean up with CTEs

```
WITH match_list AS (SELECT country_id, id
    		    FROM match
       	 	    WHERE (home_goal + away_goal) >= 10)

SELECT l.name AS league, COUNT(match_list.id) AS matches
FROM league AS l
LEFT JOIN match_list ON l.id = match_list.country_id
GROUP BY l.name;
```

### Organizing with CTEs

```
WITH match_list AS (SELECT name AS league, date, m.home_goal, m.away_goal,
       		    (m.home_goal + m.away_goal) AS total_goals
    		    FROM match AS m
                    LEFT JOIN league as l ON m.country_id = l.id)

SELECT league, date, home_goal, away_goal
FROM match_list
WHERE total_goals >= 10;
```

### CTEs with nested subqueries

```
WITH match_list AS (SELECT country_id, (home_goal + away_goal) AS goals
    		    FROM match
    		    WHERE id IN (SELECT id
      				 FROM match
       				 WHERE season = '2013/2014' AND EXTRACT(MONTH FROM date) = 08))

SELECT l.name, AVG(goals)
FROM league AS l
LEFT JOIN match_list ON l.id = match_list.country_id
GROUP BY l.name;
```

## Deciding on techniques to use

* Joins

Combining 2 or more tables, mostly limited to simple combinations and aggregations of tables 
already present in database.

* Correlated Subqueries

Combining information between a subquery and a table or another subquery. You can avoid limits of 
joins.

* Multiple/Nested Subqueries

Useful for multi-step tansformations. Improve accuracy and reproducibility by breakingdown the problem.

* Common Table Expressions

Organizes subqueries sequantially. They are processed one at a time. They are an alternative to
nested subqueries.

### Get team names with a subquery

```
SELECT m.date, hometeam, awayteam, m.home_goal, m.away_goal
FROM match AS m
LEFT JOIN (SELECT match.id, team.team_long_name AS hometeam
  	   FROM match
           LEFT JOIN team
           ON match.hometeam_id = team.team_api_id) AS home
ON home.id = m.id
LEFT JOIN (SELECT match.id, team.team_long_name AS awayteam
  	   FROM match
  	   LEFT JOIN team
  	   ON match.awayteam_id = team.team_api_id) AS away
ON away.id = m.id;
```

### Get team names with correlated subqueries

```
SELECT m.date, (SELECT team_long_name
     		FROM team AS t
     		WHERE t.team_api_id = m.hometeam_id) AS hometeam, 
       (SELECT team_long_name
       FROM team AS t
       WHERE t.team_api_id = m.awayteam_id) AS awayteam,
       home_goal,
       away_goal
FROM match AS m;
```

### Get team names with CTEs

```
WITH home AS (SELECT m.id, m.date, t.team_long_name AS hometeam, m.home_goal
  	      FROM match AS m
     	      LEFT JOIN team AS t 
  	      ON m.hometeam_id = t.team_api_id),
away AS (SELECT m.id, m.date, t.team_long_name AS awayteam, m.away_goal
  	 FROM match AS m
  	 LEFT JOIN team AS t 
  	 ON m.awayteam_id = t.team_api_id)
SELECT home.date, home.hometeam, away.awayteam, home.home_goal, away.away_goal
FROM home
INNER JOIN away
ON home.id = away.id;
```

### Get team names with Joins

```
SELECT  date, a.team_long_name AS hometeam, b.team_long_name AS awayteam, home_goal, away_goal
FROM match
LEFT JOIN team as a
ON match.hometeam_id = a.team_api_id
LEFT JOIN team as b
ON match.awayteam_id = b.team_api_id
```