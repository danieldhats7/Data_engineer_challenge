# Challenge Data Engineer

You can find the challenge [here](https://github.com/danieldhats7/Data_engineer_challenge/blob/master/Challenge_Engineer%20(17).pdf)

## Prerequisites 
You need to install all dependencies for the project:
```
virtualenv env
source env/Script/activate
pip install -r requirements.txt
```
## Challenge 1
To get the activities answers in the terminal, you need to move to the challenge_1 folder and run the following command to get the activity answers (activity 6 answer by default)
```
cd challenge_1
python main.py
```
And if you want to get the answer of some specific activity (2,3,4,5 or 6) then execute
```
python main.py --activity {number}
```
For example, for activity 3 run
```
python main.py --activity 3
```
## Challenge 2

### Setup database
Before executing the queries, you need to set up the database with docker
```
docker run -d --name challenge_de -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -e POSTGRES_DB=postgres postgres
```
You need to move to the challenge_2 folder and create the tables and load the data
```
cd challenge_2
python setup_db.py
```
### Querys on data base
To query for answers the questions (1,2,3 or 4) execute
```
python query_db.py {number}
```
For example, for query to answer the question 3 run
```
python query_db.py 3
```
You can access the database by running
```
docker exec -it challenge_pg psql -U postgres
```

## TO DO

- [ ] Implementar Airflow para la automatizacion de las actividades en el challenge 1.
- [ ] Cambiar los Prints por log para tener un mejor registro en el challenge 2.


