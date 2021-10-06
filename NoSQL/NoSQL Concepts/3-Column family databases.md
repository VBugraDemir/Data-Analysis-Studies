# Column family databases

## What is a column family database?

Column family databases derive from the Google BigTable data storage system. They store the information
in column families that group related data frequently accessed together. They are also called wide
column databases. They are great when dealing with large volumns of data. They can have multiple rows.
A column family is like a table in a relational database. Each row has a unique row key identifier.
Row key are like primary keys in a relational database. Each row contains columns and their numbers
can differ. Columns can be added to the rows when they are needed. The parts of the columns are the
name, value and timestamp. The data type can be specified depending on the database. Timestamps store
the date and time when the data was inserted. Column-family databases don't support joins.

## Advantages and limitations of column family databases

Column family databases are flexible. Rows can have different number of columns and new columns can be
added to a row if needed. This flexibility avoids filling the new columns with default values. Related
columns are stored together so writing and retrieving information faster than if the data was stored
in different parts of a disk. Like other NoSQL databases, Column family databases scale horizontally 
by sharding across multiple servers. They are designed to handle large volumes of data due to its speed, 
horizontal scalability and efficient data compression.

It does not support multirow transactions. So, more than one operation can not be perfromed within 
the same transaction. It also does not support joins and subqueries.

## When to use column family databases

They are great when dealing with large volumnes of data. They are also frequently used when extreme
write speeds are needed. They are used for Event logging, content management systems and 
storing time-series data. 

They are not suitable for prototyping and at the beginning of a project since the queries can be changed
frequently. They are modeled by thinking about the queries we want to have in out application. Complex
queries and joins are not suitable.

## Apache Cassandra case study

Apache Cassandra is one of the most popular column family databases. It is distributed, so it can run
on multiple machines as if it was one. Data is distributed across the nodes of the cluster. Every node
plays the same role and there is no master node. It scales horizontally by addin nodes. It offers 
Cassandra  Query Language (CQL). CQL is used to query data stored in Cassandra databases. It has
similar syntax to SQL but does not support joins, foreing keys, subqueries.