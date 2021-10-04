# Document databases

## What is a document database?

Document databases store data in documents. Documents are grouped into collections. There can be multipl
collections within a database. Collections are sets of documents and a document is a set of 
key-value pairs. Keys are strings and values can be numbers, strings, booleans, arrays or objects. 
Document databases have no schema. Documents can encode the data in JSON, BSON, YAML or XML formats. 
Can support more complex queries than key-value databases. They are polymorphic. Documents within 
the same collection don't need to have the same structure.

Collections are set of documents. They store the same type of entities.

## Advantages and limitations of document databases

Document databases are flexible. No predefined schema needed. Documents can vary over time without
schema migrations. Embedded documents avoid joins so it is more time efficient. Document databases
can scale horizontally by using the sharding technique. 

Data redundancy is one of the disadvantages of document databases. 

## When to use document databases

E-commerce websites and applications store catalogs of their product information. Event logging 
informations like user logging, product purchase, errors... Document flexibility makes them a good
choice for storing user profiles. Content management systems like blogs, video platforms are also
suitable for document databases. Comments, images, videos, etc. can be saved in document databases.
They are also a good option for storing data for real-time analytics like page viewers, unique visitors.

If the data are very structured, document databases will not be the best solution. And if you want
consistent data it is not suitable.

## MongoDB case study

It stores the data in a format called BSON which is a binary representation to store data in JSON format.
MongoDB offers a query language (MQL) which allows us to create complex queries for the data. It scales
horizontally accross multiple nodes with sharding without adding complexity to the application. With MongoDB
Compass queries can be created visually and much more. MongoDB Atlas is a cloud database service. It
can be fully managed across AWS, Azure and Google Cloud. MongoDB Charts you can create visiualizations of
the data. With Realm Mobile Database developers can store data locally on iOS or Android devices.

MongoDB is frequently used in single-view applications, which gather data from multiple sources to create
a single view. MongoDB can store data such as player profiles, leaderboards, etc.

Shutterfly used Oracle relational database and with growth pushed the performance limits of this db.
Oracle became too expensive and Shutterfly chose MongoDB. This switch produced a performance improvement.