# Key-value databases

## NoSQL

Relational databases us tables with rows and columns and need a predefined schema before 
inserting the data. Queries can be slow when joining multiple tables. They scale vertically
by adding more power CPU or RAM and it is expensive. They are typically closed source.

NoSQL aka non-relational databases don't use tables with row and columns. No predefined schema available
which provides the possibility of changing the structure of the data over time. Queries can be faster since
there is no need to join multiple tables. They scale horizontally, which means they scale by adding more machines
and that is cheaper. Most of them are open source.

They are complementary and coexist with each other. The four major types of NoSQL databases:
* Key-value databases
* Document databases
* Column family databases
* Graph databases

Key-value databases are the simplest NoSQL databases. They support values with an associated key. Key can
be any binary sequence, like text, numbers, etc. Keys must be unique. Long key would use more memory. A value is
always associated with a key. A value can be retrieved, set or deleted by its key. Values can be numbers, strings,
Json objects, images, etc.

## Advantages and limitations of key-value databases

Key-value databases are very simple. No need to define a schema and no need to determine the types of keys and
values. They support basic operations like put, get and delete. Put inserts a new key-value tuple or update if the
key already exists. Get returns the value by a given key. Delet removes a key and its value. Fast opertions due to
simplicity. They are very flexible, they allow data types to be changed as oppoesed to relational databases (predefined 
schema). Many key-value databases store the information in memory so reads and writes are faster than writing to a disk.
Thanks to sharding, key-value databases can scale horizontally by distributing different parts of the data across different
servers. 

They have some limitations. Only keys are searchable. So if you don't know the key you want, you have a problem. 

## Advantages and limitations of key-value databases

Suitable cases: Website store data of user sessions. The key is the user identifier. The preferences and profile information
can be stored in the value within a single object. Key-value databases also fit well with the real-time recommendations. They
also can help to show advertisements quickly while user navigates throughout a web page. 

When there is a need to search a key based on its value, key-value databases are not typically an option. Also if the data 
has to be related to other data, key-value databases would not be the best fit.

## Redis case study

Remote dictionary server. It is a fast in-memory data structure store. Redis supports many data structures. Strings, lists of
elements sets (unordered collections of strings), hashes (collecyions of field-value pairs) and more. Supports atomic operations. Redis
is often used for caching, session storage, chatting... Some established cloud providers offer services packaged with Redis.
Like AWS offers Elasticache for Redis or MS offers Azure Cache for Redis.

For example "editoo" used a traditional relational database management system that couldn't handle that increase in traffic. Then
editoo decided to use Redis to store user sessions and caching database queries. Reduction in downtime and higher performance have 
been seen. 