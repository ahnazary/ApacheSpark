## Brief explanation about project's requirements and functions<br/> <br/>
------------------------------------------------------
* ### Required services:

Run the following command in project directory to install and launch the requirements :
```
docker-compose -f docker-compose.yml up
```
Kafka, Zookeeper, kafka manager, postgres and pgAdmin should be started after successfully running mentioned command. <br/> <br/>
* ### Building new cluster in kafka manager:<br/>
Open Kafka-manager on browser on: **localhost:9000**. <br/> 
Build a new cluster (arbitrary name). Set the Cluster Zookeeper Hosts to: **zookeeper:2181**. <br/> 
Make sure to enable following options as well:
 <br/>
- [x] Enable JMX Polling (Set JMX_PORT env variable before starting kafka server)
- [x] Poll consumer information (Not recommended for large # of consumers if ZK is used for offsets tracking on older Kafka versions)
- [x] Enable Active OffsetCache (Not recommended for large # of consumers)

* ### Building new topic: <br/>
After successfully building a cluster, build a topic with the name: **testTopic** 

* ### Building new database and server in pgAdmin: <br/>
Open pgAdmin on browser on: **localhost:5555**. <br/> 
Create a new server (arbitrary name). 
Set the database **host**, **name**, **username** and **password** to **'localhost'**, **'sparkConsumer**, **'user'** and **'admin'** respectively. (In case any other arbitrary combination used, database credentials should be modified correspondingly bith in docker-compsoe.yml file and python script) <br/>
If postgress in not running on **localhost**, follow instructions in the next step. 

* #### Fixing "Connection refused Is the server running on host "127.0.0.1" and accepting TCP/IP connections on port 5432?" error
In case of encountering mentioned error while running the script or creating postgreSQL database, database host address should be changed (both in python script and in pgAdmin). To find on which **IP address** the postgres container is running, run:
```
docker container ls
```

in terminal and find the CONTAINER ID for postgres container. Then run:
```
docker inspect <postgres container ID>
```
In the resulting json file, search for **'IP Address'** and use it for creating a postgreSQL database and making the connection to it. 
