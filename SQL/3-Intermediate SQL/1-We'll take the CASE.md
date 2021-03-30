
# We'll take the CASE

Use the CASE WHEN statement to create categorical variables, aggregate data into a single 
column with multiple filtering conditions, and calculate counts and percentages.

## We'll take the CASE

Case statement contains a WHEN, THEN and ELSE statement, finished with END. An alias should be 
given. Completed CASE statement will evaluate to one column in a SQL query.

### Basic CASE statements
```
SELECT team_long_name, team_api_id
FROM teams_germany
WHERE team_long_name IN ('FC Schalke 04', 'FC Bayern Munich');
```
```
SELECT CASE WHEN hometeam_id = 10189 THEN 'FC Schalke 04'
        WHEN hometeam_id = 9823 THEN 'FC Bayern Munich'
         ELSE 'Other' END AS home_team,
	COUNT(id) AS total_matches
FROM matches_germany
GROUP BY home_team;
```

### CASE statements comparing column values
```
SELECT date, CASE WHEN home_goal > away_goal THEN 'Home win!'
		WHEN home_goal < away_goal THEN 'Home loss!'
		ELSE 'Tie' END AS outcome
FROM matches_spain;
```
```
SELECT m.date, t.team_long_name AS opponent, CASE WHEN m.home_goal > m.away_goal THEN 'Home win!'
       						 WHEN m.home_goal < m.away_goal THEN 'Home loss :('
        					 ELSE 'Tie' END AS outcome
FROM matches_spain AS m
LEFT JOIN teams_spain AS t
ON m.awayteam_id = t.team_api_id;
```
```
SELECT m.date, t.team_long_name AS opponent, CASE WHEN m.home_goal > m.away_goal THEN 'Barcelona win!'
        					WHEN m.home_goal < m.away_goal THEN 'Barcelona loss :(' 
        					ELSE 'Tie' END AS outcome 
FROM matches_spain AS m
LEFT JOIN teams_spain AS t 
ON m.awayteam_id = t.team_api_id
WHERE m.hometeam_id = 8634; 
```
### CASE statements comparing two column values part 2

```
SELECT  m.date, t.team_long_name AS opponent, CASE WHEN m.home_goal < m.away_goal THEN 'Barcelona win!'
        					WHEN m.home_goal > m.away_goal THEN 'Barcelona loss :(' 
        					ELSE 'Tie' END AS outcome
FROM matches_spain AS m
LEFT JOIN teams_spain AS t 
ON m.hometeam_id = t.team_api_id
WHERE m.awayteam_id = 8634;
```

## In CASE things get more complex

Multiple logical conditions can be added to WHEN clause with AND. Correctly categorizing the CASE
is important. The CASE statement can be used in WHERE statement to filter outcomes.

If else is not defined it there will be nulls in the result.

### In CASE of rivalry
when you have multiple logical conditions in a CASE statement, you may quickly end up with a large number 
of WHEN clauses to logically test every outcome you are interested in. 
```
SELECT date, CASE WHEN hometeam_id = 8634 THEN 'FC Barcelona' 
        	ELSE 'Real Madrid CF' END AS home,
	CASE WHEN awayteam_id = 8634 THEN 'FC Barcelona' 
        ELSE 'Real Madrid CF' END AS away
FROM matches_spain
WHERE (awayteam_id = 8634 OR hometeam_id = 8634)
      AND (awayteam_id = 8633 OR hometeam_id = 8633);
```
```
SELECT date, CASE WHEN hometeam_id = 8634 THEN 'FC Barcelona' 
             ELSE 'Real Madrid CF' END as home, CASE WHEN awayteam_id = 8634 THEN 'FC Barcelona' 
         					ELSE 'Real Madrid CF' END as away,
	CASE WHEN home_goal > away_goal AND hometeam_id = 8634 THEN 'Barcelona win!'
        WHEN home_goal > away_goal AND hometeam_id = 8633 THEN 'Real Madrid win!'
        WHEN home_goal < away_goal AND awayteam_id = 8634 THEN 'Barcelona win!'
        WHEN home_goal < away_goal AND awayteam_id = 8633 THEN 'Real Madrid win!'
        ELSE 'Tie!' END AS outcome
FROM matches_spain
WHERE (awayteam_id = 8634 OR hometeam_id = 8634)
      AND (awayteam_id = 8633 OR hometeam_id = 8633);
```

### Filtering your CASE statement
CASE statements allow you to categorize data that you're interested in -- and exclude data 
you're not interested in. In order to do this, you can use a CASE statement as a filter in 
the WHERE statement to remove output you don't want to see.

```
SELECT team_long_name, team_api_id
FROM teams_italy
WHERE team_long_name = 'Bologna';
```
```
SELECT season, date, CASE WHEN hometeam_id = 9857 AND home_goal > away_goal THEN 'Bologna Win'
			  WHEN awayteam_id = 9857 AND away_gola > home_goal THEN 'Bologna Win'
			  ENS AS outcome
FROM matches_italy;
```
```
SELECT season, date, home_goal, away_goal
FROM matches_italy
WHERE CASE WHEN hometeam_id = 9857 AND home_goal > away_goal THEN 'Bologna Win'
	   WHEN awayteam_id = 9857 AND away_goal > home_goal THEN 'Bologna Win'
	   END IS NOT NULL;
```
The details on every match where Bologna won.


## CASE WHEN with aggregate functions
CASE statements are great for 
* Catogorizing data (SELECT)
* Filtering data (WHERE)
* Aggregating data (with GROUP BY)
To make results easier to read you can use ROUND().

### COUNT using CASE WHEN
```
SELECT c.name AS country, COUNT(CASE WHEN m.season = '2012/2013' THEN m.id ELSE NULL END) AS matches_2012_2013
FROM country AS c
LEFT JOIN match AS m
ON c.id = m.country_id
GROUP BY name;
```
### COUNT and CASE WHEN with multiple conditions
```
SELECT c.name AS country,
SUM(CASE WHEN m.season = '2012/2013' AND m.home_goal > m.away_goal THEN 1 ELSE 0 END) AS matches_2012_2013,
SUM(CASE WHEN m.season = '2013/2014' AND m.home_goal > m.away_goal THEN 1 ELSE 0 END) AS matches_2013_2014,
SUM(CASE WHEN m.season = '2013/2015' AND m.home_goal > m.away_goal THEN 1 ELSE 0 END) AS matches_2014_2015
FROM country AS c
LEFT JOIN match AS m
ON c.id = m.country_id
GROUP BY country;
```

### Calculating percent with CASE and AVG
```
SELECT c.name AS country,
COUNT(CASE WHEN m.home_goal > m.away_goal THEN m.id END) AS home_wins,
COUNT(CASE WHEN m.home_goal < m.away_goal THEN m.id END) AS away_wins,
COUNT(CASE WHEN m.home_goal = m.away_goal THEN m.id END) AS ties
FROM country AS c
LEFT JOIN match AS m
ON c.id = m.country_id
GROUP BY country;
```
```
SELECT c.name AS country,
	AVG(CASE WHEN m.season='2013/2014' AND m.home_goal = m.away_goal THEN 1
			WHEN m.season='2013/2014' AND m.home_goal <> m.away_goal THEN 0
			END) AS ties_2013_2014,
	AVG(CASE WHEN m.season='2014/2015' AND m.home_goal = m.away_goal THEN 1
			WHEN m.season='2014/2015' AND m.home_goal <> m.away_goal THEN 0
			END) AS ties_2014_2015
FROM country AS c
LEFT JOIN matches AS m
ON c.id = m.country_id
GROUP BY country;
```
```
SELECT c.name AS country,
	ROUND(AVG(CASE WHEN m.season='2013/2014' AND m.home_goal = m.away_goal THEN 1
			 WHEN m.season='2013/2014' AND m.home_goal != m.away_goal THEN 0
			 END),2) AS pct_ties_2013_2014,
	ROUND(AVG(CASE WHEN m.season='2014/2015' AND m.home_goal = m.away_goal THEN 1
			 WHEN m.season='2014/2015' AND m.home_goal != m.away_goal THEN 0
			 END),2) AS pct_ties_2014_2015
FROM country AS c
LEFT JOIN matches AS m
ON c.id = m.country_id
GROUP BY country;
```
