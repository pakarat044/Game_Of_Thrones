# Game of Thrones

> database of Game of Thrones

## Step-by-step installation instructions

### Step 1: create the database and table schema

```
sqlite3 game_of_throne.db < game_of_throne.schema
```

### Step 2: add initial data to the database,

```
sqlite3 game_of_throne.db
.mode csv
.import data/game_of_thrones_imdb.csv imdb_rating
.import data/game_of_thrones_episodes.csv episodes
```

### Step 3: run the application

```
uvicorn main:app --reload
```

test the api with openapi by this path ➜ http://127.0.0.1:8000/docs

## UML class
![](https://www.img.in.th/images/96df17e9ecb872b0b53c5bc0f7ee15de.png)

## package diagram
