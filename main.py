# from utils.game_of_thrones_db import GameOfThroneDB

# game_of_throne_db = GameOfThroneDB()

# print(game_of_throne_db.episodes().get_all_episodes())
# print(game_of_throne_db.episodes().get_episodes_by_director("Alan Taylor"))
# print(game_of_throne_db.episodes().get_episodes_by_season(2))
# print(game_of_throne_db.episodes().get_episodes_by_sorted_rating())

# print(game_of_throne_db.rating().get_all_rating())
# print(game_of_throne_db.rating().get_all_by_higher_rating(9.5))

from fastapi import FastAPI
from router import episodes, imdb_rating

app = FastAPI(title="Game of Thrones")

app.include_router(episodes.router)
app.include_router(imdb_rating.router)
