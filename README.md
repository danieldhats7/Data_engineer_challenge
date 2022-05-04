# Challenge Data Engineer

You can find the challenge [here](challenge.md)

## Prerequisites 


## Setup database
You can setup the dabase by running
```
docker run -d --name challenge_de -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -e POSTGRES_DB=postgres postgres

```
You can access the database by running
```
docker exec -it challenge_pg psql -U postgres -d data_analytics

---------------------------------------------

docker exec -it challenge_de psql -U postgres

