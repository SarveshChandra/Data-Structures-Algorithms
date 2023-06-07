Important
1. scaling cache
2. queue systems
3. basics of internet
4. basics of OS


Grokking the System Design Interview (Educative)

## 1. System design basics
    1.1 distributed system and architectures

## 2. Key characteristics of distributed systems
	2.1 scalability
		> serve to increased demand, traffic, increased data volume, increased transactions
		> horizontal vs vertical scaling
		> horizontal eg. mongodb, cassandra
		> vertical eg. mysql
	2.2 reliability
		> eg. amazon user transaction example add to cart
	2.3 availability
		> reliability over time
		> reliable is available but available need not be reliable
	2.4 efficiency
		> response time (latency), throughput (bandwidth)
		> efficiency of supported data structures and algorithms in use
		> factors like neywork topology, network load, hardware and software components
	2.5 serviceability or manageability
		> how easy to repair or fix

## 3. Load balancing (component of distributed systems)
	> in horizontal scaling
	> spread the traffic across cluster of servers
	> to improve responsiveness and availability
	> keeps track of status of all the resources while distributing requests
	> sits between client and servers
	> can balance load at each layer of the system
		> between user and web servers
		> between web servers and internal platform layers (application servers of cache servers)
		> between internal platform layers and database servers
		> client -> LB -> web servers -> LB -> internal platform layers -> LB -> database servers
	> smart load balancers
	3.1 benefits of load balancing
	3.2 load balancing algorithms
		> first, collects all the healthy servers into its pool by doing health checks
		> second, from its pool of healthy servers, there are load balancing methods
			1. least connection method
				> server with fewest active connections
			2. least response time method
				> server with fewest acive connections and lowest average response time
			3. least bandwidth method
				> server with least amount of traffic, measured in mbps
			4. round robin method
				> cycles through the list of servers, sends each new request to the next server
				> useful when servers are equal in specs and not many persistent connections
			5. weighted round robin method
				> servers with different processing capacities
			6. IP hash
				> hash of client ip address is calculated to send to server
	3.3 redundant load balancers
		> cluster of load balancers (active and passive lbs)

## 4. Caching
	> mostly at level nearest to frontend layer
	> contains recently accessed items
	4.1 application server cache
		> cache in request node in application storage
	4.2 CDN
		> for sites with large amount of static media
		> alternative of different subdomain (http server)
	4.3 cache invalidation
		> to maintain data consistency
		> 3 schemes
			1. write-through cache
				> higher latency
			2. write-around cache
			3. write-back cache
	4.4 cache eviction policies
		1. FIFO
		2. LIFO
		3. LRU
		4. MRU
		5. LFU
		6. RR

## 5. Data Partitioning
    > large database partitioned into smaller database servers
    > done as it becomes cheaper and more feasible to scale horizontally after a certain scale point
    > for better manageability, performance, availability, load balance
    > horizontal scalability by adding more machines
	5.1 partitioning methods
        1. horizontal partitioning
            > different rows into different tables in different servers
            > range-based partitioning
            > also called as data sharding
            > inappropriate range may unbalance servers
        2. vertical partitioning
            > easier and less impact on application
            > different feature tables to different servers
        3. directory-based partitioning
            > a directory server (lookup service) that holds the mapping between each tuple key to its db server
            > easy db pool changes or partitioning change with no impact on application
	5.2 partitioning criteria/schemes
        1. key or hash-based partitioning
            > uniform allocation of data among servers
            > adding new server -> changing hash function -> redistribution of data -> application downtime
            > workaround to this problem -> consistent hashing
        2. list partitioning
            > each partition is assigned a list of values
        3. round-robin partitioning
            > uniform data distribution
            > with n partitions, the i tuple is assigned to partition (i mod n)
        4. composite partitioning
            > to combine any of the above schemes to make a new scheme
            > for eg. list + hash-based considered as consistent hashing
    5.3 common problems of data partitioning
        > operations across multiple tables or multiple rows in the same table will not run on the same server
        > joins and denormalization
        > referential integrity
            > application has to enforce it in application code
            > often run sql jobs to clean up dangling references
        > rebalancing
            > data partitions not uniform (like data distribution or requests)

## 6. Indexes
    > for better database performance
    > index on table for rapid random lookups and efficient access of ordered records
    > easy search with sorted list of data by relevant information
    > with large size datasets, but with very small payloads (eg. 1KB), indexes are a necessity for optimizing data access
    > indexes decrease write performance, with index itself large
    > avoid adding unnecessary indexes on tables, and remove unused indexes
    > index not very useful when data is such that is rarely read and often written to

## 7. Proxies
    > forward proxy (used to cache data, filter requests, log requests, or transform requests by adding/removing headers, encrypting/decrypting, compress a resource)
    > forward proxy hides the client from the server
    > collapsed forwarding
    > reverse proxy hides the server from the client
    > reverse proxy used for caching, load balancing or routing requests to the appropriate servers

## 8. Redundancy and Replication
    > redundancy removes the single point of failure in the system and provides backups
    > replication in database ensure consistency, reliability, fault tolerance, accessibility

## 9. SQL vs NoSQL
    > sql examples: mysql, oracle, sql server, sqlite, postgresql, mariadb
    > nosql types
        1. key-value stores eg. redis, dynamo
        2. document databases eg. couchdb, mongodb
        3. wide column databases eg. cassandra, hbase
        4. graph databases eg. neo4j, infinitegraph
    > sql databases are ACID (atomicity, consistency, isolation, durability) compliance (data integrity) whereas nosql databases are generally not
    > relational databases are vertically scalable, with predefined schema
    > non-relational databases are horizontally scalable and fast

## 10. CAP theorem
    > it states that it is impossible for a distributed system to simultaneously provide all three of the following desirable properties
        1. consistency
        2. availability
        3. partition tolerance
    > in the presence of a network partition, a distributed system must choose either consistency or availability

## 11. PACELC theorem
    > it states that in a system that replicates data, if there is a partition P, a distributed system can tradeoff between availability and consistency, else when the system is running normally in the absence of partitions, the system can tradeoff between latency and consistency

## 12. Consistent hashing