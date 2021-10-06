# Graph databases

## Graph databases treat data and its relationships  with the same importance. They are based on 
graph theory which studies the graphs for modeling the relationships between objects. Graph are
structures that have two parts. Nodes (vertices) and edges (links). Node represents entities like
users, cities, employees. Nodes can have properties such as; name, surname, email, date of birth, etc.
Edges connect the nodes and define the relationships between the nodes. Edge also can have properties.
Edges can directed or undirected. Querying the graps is called traversing the graph. 

Set of nodes and edges across a graph is called path. Graph databases support query languages such as
Cypher and Gremlin

## Advantages and limitations of graph databases

They are flexible and can change as applications and industries change. The final structure of a graph
is not needed to be defined in advance. Nodes, propreties and edges can be added and deleted without
worrying about the current information. Another advantage is their performance. They don't need perform
joins and joining process is time consuming. Instead edges can be followed node to node which is faster and
simpler even for complex queries or large volumes of data. They have an easy representation of the data.
Graphs map in a more realistic way than other databases. It makes graph modelling very intuitive.
Graphs are easily visualized with the nodes, relationships and associated properties. Horizontial scalability
is possible however it is more difficult than in other NoSQL databases since they are connected and they need to be
distributed across multiple machines.

Having entity properties containing extremely large values is unsuitable for graph databases like BLOBs or CLOBs.

## Advantages and limitations of graph databases

Graph databases are suitable for highly connected data such as social graphs. Modeling infectious disease is another
use of graph databases. Graph databases can be used to model the interactions between people, contact events, or exposures.
They can also represent locations and distances between these locations. They also can bu used in fraud detection. Also real-time
recommendations can be created.

They are not the best option when the data is disconnected or the relationships between the data are not important.

## Neo4j case study

Graph algorithms such as path-finding, centrality, community detection, similarity, link prediction, node embeddings, and node classification.
Bloom is visualization tool to view and analyze data. Cypher is a powerful query language and is inspiered by SQL. It allows users to save
and get data from the graph database. With Neo4j it is possible to run multiple queries in Cypher within the same transaction.
Aura is the cloud database service. 
For Gousto they grew their menu but that implied that the menus were difficult to navigate. They used an
internal recommendation system. The data sources are the subscriber's previous interactions and the information 
on upcoming recipes.