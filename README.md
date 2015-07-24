# docker-demo
A basic Python web app in a docker container

Build the Web Service
---------------------
docker build -t dockerdemo_web .

Start the Database
------------------
docker run --name dockerdemo-postgres -e POSTGRES_PASSWORD=mypasswd -d postgres

Initialize the Database
-----------------------
1. docker run -it --link dockerdemo-postgres:postgres --rm postgres sh -c 'exec psql -h "$POSTGRES_PORT_5432_TCP_ADDR" -p "$POSTGRES_PORT_5432_TCP_PORT" -U postgres'
2. create database dockerdemo with owner postgres;
3. \connect dockerdemo
4. create table person(name varchar(50));
5. insert into person(name) values('ThoughtWorker');
6. \q

Start The Web Service
---------------------
docker run -d --name web --link dockerdemo-postgres:postgres -p 8080:8080 dockerdemo_web

Browse to Web Service
---------------------
1. boot2docker ip
2. http://192.168.59.103:8080
