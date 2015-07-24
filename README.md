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
docker run -it --link dockerdemo-postgres:postgres --rm postgres sh -c 'exec psql -h "$POSTGRES_PORT_5432_TCP_ADDR" -p "$POSTGRES_PORT_5432_TCP_PORT" -U postgres'
create database dockerdemo with owner postgres;
\connect dockerdemo
create table person(name varchar(50));
insert into person(name) values('ThoughtWorker');
\q

Start The Web Service
---------------------
docker run -d --name web --link dockerdemo-postgres:postgres -p 8080:8080 dockerdemo_web

Browse to Web Service
---------------------
boot2docker ip
http://192.168.59.103:8080
