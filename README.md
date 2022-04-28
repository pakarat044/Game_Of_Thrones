# Game of Thrones

> Application about Game of Thrones where users can search the database about Game of Thrones.

## Step-by-step installation instructions

### Step 1: install all requirements
```
pip install -r requirements.txt
```

### Step 2: create the database and table schema

```
sqlite3 game_of_throne.db < game_of_throne.schema
```

### Step 3: add initial data to the database,

```
sqlite3 game_of_throne.db
.mode csv
.import data/game_of_thrones_imdb.csv imdb_rating
.import data/game_of_thrones_episodes.csv episodes
```

### Step 4: run the application

```
uvicorn main:app --reload
```

test the api with openapi by this path ➜ http://127.0.0.1:8000/docs

## UML class
![UML class](https://www.img.in.th/images/e652f6df8f184fc1bd4e31c588cefa11.png)

## package diagram
![package diagram](https://www.img.in.th/images/50d0e81d30a7e4e701b09e7e6ebd30b5.png)
