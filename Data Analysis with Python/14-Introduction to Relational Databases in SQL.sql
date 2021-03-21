-- Introduction to Relational Databases in SQL

--- Introduction to relational databases

---- In databases each table contains data from a single entity type
---- to reduce redundancy by storing them only once. A database
---- can be used to model relationships between entities.
---- constaints, keys and referantial integrity help preserve
---- data quality in databases.

---- information_schema is a meta-database that holds information about
---- currentdatabase.

SELECT table_schema, table_name
FROM information_schema.tables

---- by querying information_schema you can get information either about
---- tables or columns once you know the table name.


----- Query information_schema with SELECT

SELECT table_name 
FROM information_schema.tables
WHERE table_schema = 'public';

---- to get the information about user defined tables.

SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'university_professors' AND table_schema = 'public';

---- to get the information about columns of the table.

SELECT * 
FROM university_professors 
LIMIT 5;

---- querying the related table after learning its name.

----- Tables: At the core of every database

--- There were redundancy about the table since it holds many entity
--- together just in one table. (one prof with many affiliations.)
--- The table holds information about the Prefessors, universities and
--- organizations. Splitting them into different tables will reduce the 
--- redundancy which is one of the main considerations of creating databases.

---- CREATE your first few TABLEs

CREATE TABLE professors (
	firstname text,
	lastname text
);

SELECT *
FROM professors

CREATE TABLE universities (
	university_shortname text,
	university text,
	university_city text
);

SELECT *
FROM universities

---- ADD a COLUMN with ALTER TABLE
--- Notice we forgot to add university_shortname to professors table
--- that column is important to connect professors and universities table.

ALTER TABLE professors
ADD COLUMN university_shortname text;

SELECT *
FROM professors

----- Update your database as the structure changes

--- Some of the codes will be used;
INSERT INTO organizations
SELECT DISTINCT organizations, organizations_sector -- reduce redundancy with distinct.
FROM university_professors; -- the old table where we wanto migrate data from.

--- the normal use case for INSERT INTO where you inset values manually
INSERT INTO table_name (column_a, column_b)
VALUES ('value_a', 'value_b')

--- changing the name of the column
ALTER TABLE table_name
RENAME COLUMN old_name TO new_name;

--- To drop a column use:
ALTER TABLE table_name
DROP COLUMN column_name;

---- RENAME and DROP COLUMNs in affiliations

ALTER TABLE affiliations
RENAME COLUMN organisation TO organization;

ALTER TABLE affiliations
DROP COLUMN university_shortname;

---- Migrate data with INSERT INTO SELECT DISTINCT

INSERT INTO professors
SELECT DISTINCT firstname, lastname, university_shortname
FROM university_professors;
--- to check it
SELECT *
FROM professors;

INSERT INTO affiliations
SELECT DISTINCT firstname, lastname, function, organization
FROM university_professors;

SELECT *
FROM affiliations;

---- Delete tables with DROP TABLE

DROP TABLE university_professors; -- We don't need this table anymore since we splitted it.


--- Enforce data consistency with attribute constraints

--- After building a simple database, it's now time to make use of the features. 
--- specifying data types in columns, enforcing column uniqueness, and disallowing
--- NULL values.

---- Better data quality with constraints

--- The idea of a database is to push data into a certain structure
--- pre-defined model, where you enforce data types, relationships 
--- and other rules. These rules are called integrity constraints.

--- Attribute (Domain) Constraints: legal values to use

--- Key Constraints: Primary can't be repeated.

--- Referential Integrity Constraints: Enforces through foreign keys.
--- They glue different database tables together.

--- Entity Integrity Constraints: Primary key can't be NULL

--- Constraints give consistency and thus data quality.

--- Attribute constraints are data types that can be specified
--- To convert data type to do some operations CAST(.... AS integer) can be used.


---- Conforming with data types

CREATE TABLE transactions(
	transaction_date date,
	amount integer,
	fee text
);

INSERT INTO transactions (transaction_date, amount, fee)
VALUES ('2018-24-09', 5454, '30')
--- Rejected

INSERT INTO transactions (transaction_date, amount, fee)
VALUES ('2018-09-24', 5454, '30')

---- Type CASTs

--- certain column stores numbers as text, you can cast the column 
--- to a numeric form, i.e. to integer.

SELECT transaction_date, amount + CAST(fee as integer) 
AS net_amount
FROM transactions;
--- Casting is cool but it is better to store columns in the right 
--- data type from the first place. 


----- Working with data types
--- Data types are attribute constraints.
--- The most common data types;
--- text: character strings of any length
--- varchar: a maximum of n characters
--- char: a fixed-length string of n characters
--- boolean: can only take three states; TRUE FALSE NULL
--- date, time and timestamp: various formats for date and calculations.
--- numeric: arbitrary precision numbers, 3.1457 numeric(3,2)
--- integer: whole number in the range of -2147483648 and +2147483648
--- bigint: for larger numbers
--- Altering data type

ALTER TABLE table_name
ALTER COLUMN name
TYPE varchar(128);

ALTER TABLE table_name
ALTER COLUMN name
TYPE integer
USING ROUND(name);

---- Change types with ALTER COLUMN
ALTER TABLE professors
ALTER COLUMN university_shortname
TYPE char(3);

ALTER TABLE professors
ALTER COLUMN firstname
TYPE varchar(64);

---- Convert types USING a function

ALTER TABLE professors
ALTER COLUMN firstname
TYPE varchar(16)
USING SUBSTRING(firstname FROM 1 FOR 16)


----- The not-null and unique constraints
--- 2 special attribute constraints: NOT NULL and unique.
CREATE TABLE stundents (
	ssn integer not null,
	lastname varchar(64) not null,
	home_phone integer,
	office_phone integer
);

--- Add not null or null constraints to existing tables
ALTER TABLE sutdents
ALTER COLUMN home_phone
SET NOT NULL;

ALTER TABLE sutdents
ALTER COLUMN ssn 
DROP NOT NULL;

--- Unique constraint on a column makes sure that there are no duplicates
--- in a column 
CREATE TABLE table_name(
	column_name UNIQUE
);
--- to existing table 
ALTER TABLE table_name
ADD CONSTRAINT some_name UNIQUE(column_name);

---- Disallow NULL values with SET NOT NULL

ALTER TABLE professors
ALTER COLUMNS firstname SET NOT NULL;

ALTER TABLE professors
ALTER COLUMNS lastname SET NOT NULL;

---- Make your columns UNIQUE with ADD CONSTRAINT

ALTER TABLE universities
ADD CONSTRAINT university_shortname_unq UNIQUE (univesity_shortname);
--- Also, you have to give the constraint a name some_name.

ALTER TABLE organizations
ADD CONSTRAINT organizations UNIQUE(organization)

--- Making sure they only contain unique values is a prerequisite for 
--- turning them into so-called primary keys 



------ Uniquely identify records with key constraints

--- It's time to add primary and foreign keys to the tables. These are two of the most 
--- important concepts in databases, and are the building blocks you’ll use to establish
--- relationships between tables.

----- Keys and superkeys
--- To create a database firt design a model for it. Specify attribute constraints,
--- data types. Set not-null and unique constraints on certain attributes.
--- then add primary keys to three different tables named id.
--- Typically a database table has an attribute or a combination of attributes
--- whose values are unique across the whole table. As long as attributes can be removed
--- that is called superkey. If no more attribute can be removed that is key.
--- a key shoul be selected from candidate keys.

---- Get to know SELECT COUNT DISTINCT

SELECT COUNT(DISTINCT (university_shortname,university,university_city))
FROM universities;
--- 11
SELECT COUNT(DISTINCT university_city)
FROM universities;
--- 9 so university cant be used as a key.


---- Identify keys with SELECT COUNT DISTINCT

--- Count the distinct records for all possible combinations of
--- columns. If the resulting number x equals the number of all rows in the table for
--- a combination, you have discovered a superkey.
--- Then remove one column after another until you can no longer remove columns
--- without seeing the number x decrease. If that is the case, you have discovered a (candidate) key.

SELECT COUNT(DISTINCT (fistname, lastname, university_shortname))
FROM professors;
--- 551
SELECT COUNT(DISTINCT (fistname, lastname))
FROM professors;
--- 551 so it is a candidate key that uniquely identifies professors.


---- Primary keys
--- Almost every database table should have a primary key chosen by user from the set
--- of candidate keys to uniquely identify records in a table. This makes it easier to reference
--- these records from other tables. Primary keys don't accept duplicate or NULL values.
CREATE TABLE products (
	product_no integer UNIQUE NOT NULL,
	name text,
	price numeric
);

CREATE TABLE products (
	product_no integer PRIMARY KEY,
	name text,
	price numeric
);

CREATE TABLE example (
	a integer,
	b integer,
	c integer,
	PRIMARY KEY (a, c)
);

ALTER TABLE table_name
ADD CONSTRAINT some_name PRIMARY KEY (column_name)

---- ADD key CONSTRAINTs to the tables

ALTER TABLE organizations
RENAME COLUMNS organization TO id;

ALTER TABLE organizations
ADD CONSTRAINT organization_pk PRIMARY KEY (id);
---
ALTER TABLE universities
RENAME COLUMN university_shortname TO id;

ALTER TABLE universities
ADD CONSTRAINT university_pk PRIMARY KEY(id);


----- Surrogate keys
--- They are sort of an artificial primary key. They are not based on a native column
--- in your data but on a column that just exists for the sake of having a primary key. 
--- Serial type will add numbers to an axisting table automatically.
ALTER TABLE cars
ADD COLUMN id serial PRIMARY KEY;
--- Once the column with the serial type is added, all the records in the table will be
--- numbered. Adding a new record will get automatically a number.
--- Another strategy for creating a surrogate key is to combine 2 existing columns into
--- a new one.

ALTER TABLE table_name
ADD COLUMN column_c varchar(256);

UPDATE table_name
SET column_c = CONCAT(column_a, column_b);

ALTER TABLE table_name
ADD CONSTRAINT pk PRIMARY KEY (column_c);


---- Add a SERIAL surrogate key

ALTER TABLE professors
ADD COLUMN id serial;

ALTER TABLE professors
ADD CONSTRAINT professors_pkey PRIMARY KEY (id);

SELECT *
FROM professors
LIMIT 10;


---- CONCATenate columns to a surrogate key

SELECT COUNT(DISTINCT (make, model))
FROM cars;

ALTER TABLE cars
ADD COLUMN id varchar(128);

UPDATE cars
SET id = CONCAT(make,model);

ALTER TABLE cars
SET CONSTRAINT id_pk PRIMARY KEY(id);

SELECT * FROM cars;


---- Test your knowledge before advancing

CREATE TABLE student (
	last_name varchar(128) NOT NULL,
	ssn integer PRIMARY KEY,
	phone_no char(12)
);


------ Glue together tables with foreign keys

----- Model 1:N relationships with foreign keys
--- Relationships are implemented with foreign keys. Foreign keys are designated columns
--- that point to a primary key of another table. Domain and the data type must be the same
--- as one of the primary key. and only foreign key values are allowed that exist as values in the
--- primary key of the referenced table so called referential integrity. FKs are not actual keys because
--- duplicates and null values are allowed.

CREATE TABLE manufacturers(
	name varchar(255) PRIMARY KEY);
INSERT INTO manufacturers
VALUES ('Ford'),('VW'),('GM');

CREATE TABLE cars (
	model varchar(255) PRIMARY KEY,
	manufacturer_name varchar(255) REFERENCES manufacturers (name));

INSERT INTO cars
VALUES ('Ranger', 'Ford'), ('Beetle', 'VW');

INSERT INTO cars
VALUES ('Tundra', 'Toyota');
--- That throws an error!

ALTER TABLE a
ADD CONSTRAINT a_fkey FOREIGN KEY (b_id) REFERENCES b (id);

---- REFERENCE a table with a FOREIGN KEY

ALTER TABLE professors
RENAME COLUMN university_shortname TO university_id;

ALTER TABLE professors
ADD CONSTRAINT professors_fkey FOREIGN KEY (university_id) 
REFERENCES universities (id); 

---- Explore foreign key constraints

--- Foreign key constraints help you to keep order in your database
--- mini-world. In your database, for instance, only professors belonging 
--- to Swiss universities should be allowed, as only Swiss universities are part of
--- the universities table.

--- The foreign key on professors referencing universities you just created thus makes
--- sure that only existing universities can be specified when inserting new data. 

INSERT INTO professors (firstname, lastname, university_id)
VALUES ('Albert', 'Einstein', 'MIT');
--- That throws an error since 'MIT' is not in the universities table and referenced.
--- Inserting a professor with non-existing university IDs violates the foreign key
--- constraint you've just added. This also makes sure that all universities are spelled equally 
--- – adding to data consistency.
INSERT INTO professors (firstname, lastname, university_id)
VALUES ('Albert', 'Einstein', 'UZH');


---- JOIN tables linked by a foreign key
--- While foreign keys and primary keys are not strictly necessary for join queries, they greatly 
--- help by telling you what to expect.

SELECT professors.lastname, universities.id, universities.university_city
FROM professors
JOIN universities
ON professors.university_id = universities.id
WHERE universities.university_cit = 'Zurich';


----- Model more complex relationships
--- Implement  N:M relationships.

CREATE TABLE affiliations(
	professor id integer REFERENCES professors (id),
	organization_id varchar(256) REFERENCES organizations (id),
	function varchar(256)
);


---- Add foreign keys to the "affiliations" table
--- from {firstname, lastname, function, organization} to  {professor_id, organization_id, function}

ALTER TABLE affiliations
ADD COLUMN professor_id integer REFERENCES professors (id);

ALTER TABLE affiliations
RENAME organization TO organization_id;

ALTER TABLE affiliations
ADD CONSTRAINT affiliations_organization_fkey
FOREIGN KEY (organization_id) REFERENCES organizations (id);

---- Populate the "professor_id" column

UPDATE affiliations
SET professors_id = professors.id 
FROM professors
WHERE affiliations.firtsname = professors.firstname 
AND affiliations.lastname = professors.lastname;

SELECT *
FROM affiliations
LIMIT 10;


---- Drop "firstname" and "lastname"

ALTER TABLE affiliations DROP COLUMN firstname;
ALTER TABLE affiliations DROP COLUMN lastname;


----- Referential integrity
--- Throws error if a refenced row deleted or adding a row that does not exist
--- referenced table. ON DELETE CASCADE will delete the referenced record then the
--- all referencing record.
--- SET NULL, SET DEFAULT

---- Referential integrity violations

DELETE FROM universities WHERE id = 'EPF';
--- That throws an error since there is a referential integrity from professors to
--- universities


----- Change the referential integrity behavior of a key
--- Altering a key constraint doesn't work with ALTER COLUMN. Instead, you have to DROP the key
--- Constraint and then ADD a new one with a different ON DELETE behavior.

--- For deleting constraints, though, you need to know their name. This information
--- is also stored in information_schema.

SELECT constraint_name, table_name, constraint_type
FROM information_schema.table_constraints
WHERE constraint_type = 'FOREIGN KEY';

ALTER TABLE affiliations
DROP CONSTRAINT affiliactions_organization_id_fkey;

ALTER TABLE affiliations
ADD CONSTRAINT affiliactions_organization_id_fkey FOREIGN KEY (organization_id)
REFERENCES organizations (id) ON DELETE CASCADE;

DELETE FROM organizations WHERE id = 'CUREM';
SELECT * FROM affiliations WHERE organization_id = 'CUREM'


----- Roundup

---- Count affiliations per university

SELECT COUNT(*), professors.university_id
FROM affiliations
JOIN professors
ON affiliations.professor_id = professors.id
GROUP BY professors.university_id
ORDER BY COUNT DESC;


---- Join all the tables together

SELECT COUNT(*), organizations.organization_sector, professor.id, universities.university_city
FROM affiliations
JOIN professors
ON affiliations.professor_id = professors.id
JOIN organizations
ON affiliations.organization_id = organizations.id
JOIN universities
ON professors.university_id = universities.id
WHERE organizations.organization_sector = 'Media & communication'
GROUP BY organizations.organization_sector, professors.id, universities.university_city
ORDER BY COUNT DESC;

