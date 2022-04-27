from fastapi import APIRouter
from utils.game_of_thrones_db import GameOfThroneDB

db = GameOfThroneDB().episodes()

router = APIRouter(prefix="/episodes", tags=["episodes"])


@router.get("/")
def get_all_episodes():
    return db.get_all_episodes()


@router.get("/id/{id}")
def get_episode_by_id(id: int):
    return db.get_episode_by_id(id)


@router.get("/season/{season_num}")
def get_episodes_by_season(season_num: int):
    return db.get_episodes_by_season(season_num)


@router.get("/season/{season_num}/episode_num/{episode_num}")
def get_episode_by_season_and_episode_num(season_num: int, episode_num: int):
    return db.get_episode_by_season_and_episode_num(season_num, episode_num)


@router.get("/title/{title}")
def get_episode_by_title(title: str):
    return db.get_episode_by_title(title)


@router.get("/director/{director}")
def get_episodes_by_director(director: str):
    return db.get_episodes_by_director(director)


@router.get("/writer/{writer}")
def get_episodes_by_writer(writer: str):
    return db.get_episodes_by_writer(writer)


@router.get("/sorted_by_rating")
def get_episodes_by_sorted_rating():
    return db.get_episodes_by_sorted_rating()
