# Challenge Data Analytics - Python

You can find the challenge [here](challenge.md)

## Prerequisites 
#### Poetry
Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.<br>
You need to install poetry with `pip install poetry` then all other dependencies will be managed by it.<br>
Basic usage<br>
Using `poetry install` it will create a virtual env with all the necesary dependencies then you can access it with `poetry shell`.<br>
If you need to add a dependency just use `poetry add <dependency>` or you can customice much more editing the `pyproyect.toml`<br>
I exported all necesary dependencies to a `requirements.txt` if you dont fancy poetry (you should tho)<br>
You can read more about Poetry [Here](https://python-poetry.org/docs/)<br>
Also you can expand even further with this post [Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)<br>


## Setup database
You can setup the dabase by running
```
docker run -d --name challenge_pg -v my_dbdata:/var/lib/postgresql/data -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=data_analytics postgres
```
You can access the database by running
```
docker exec -it challenge_pg psql -U postgres -d data_analytics

---------------------------------------------
docker run -d --name challenge_de -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -e POSTGRES_DB=postgres postgres

docker exec -it challenge_de psql -U postgres

