from fastapi import APIRouter, status, HTTPException
from utils.game_of_thrones_db import GameOfThroneDB
from typing import List
from schemas.episodes import Episode, NotFoundEpisode

db = GameOfThroneDB().episodes()

router = APIRouter(prefix="/episodes", tags=["episodes"])

@router.get("/", response_model=List[Episode])
def get_all_episodes():
    """
    Get all episodes in Game of Thrones series
    """
    return db.get_all_episodes()

@router.get("/id/{id}", response_model=Episode, responses={status.HTTP_404_NOT_FOUND: {"model": NotFoundEpisode}})
def get_episode_by_id(id: int):
    """
    Get the specific episode from episode id:
    ### Parameters:
    - **id**: the id of the specific episode as an integer e.g., 1
    """
    episode = db.get_episode_by_id(id)
    if not episode:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Not found episode(s)"
        )
    return episode

@router.get("/season/{season_num}", response_model=List[Episode], responses={status.HTTP_404_NOT_FOUND: {"model": NotFoundEpisode}})
def get_episodes_by_season(season_num: int):
    """
    Get all episodes from specific season:
    ### Parameters:
    - **season_num**: the season number as an integer e.g., 1
    """
    episodes = db.get_episodes_by_season(season_num)
    if not episodes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Not found episode(s)"
        )
    return episodes

@router.get("/season/{season_num}/episode_num/{episode_num}", response_model=Episode, responses={status.HTTP_404_NOT_FOUND: {"model": NotFoundEpisode}})
def get_episode_by_season_and_episode_num(season_num: int, episode_num: int):
    """
    Get specific episode from season and episode number:
    ### Parameters:
    - **season_num**: the season number as an integer e.g., 1
    - **episode_num**: the episode number as an integer e.g., 1
    """
    episode = db.get_episode_by_season_and_episode_num(season_num, episode_num)
    if not episode:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Not found episode(s)"
        )
    return episode

@router.get("/title/{title}", response_model=Episode, responses={status.HTTP_404_NOT_FOUND: {"model": NotFoundEpisode}})
def get_episode_by_title(title: str):
    """
    Get specific episode from title:
    ### Parameters:
    - **title**: the episode title as a string e.g., Winter Is Coming
    """
    episode = db.get_episode_by_title(title)
    if not episode:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Not found episode(s)"
        )
    return episode

@router.get("/director/{director}", response_model=List[Episode], responses={status.HTTP_404_NOT_FOUND: {"model": NotFoundEpisode}})
def get_episodes_by_director(director: str):
    """
    Get all episodes from director:
    ### Parameters:
    - **director**: the director of episode as a string e.g., Tim Van Patten
    """
    episodes = db.get_episodes_by_director(director)
    if not episodes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Not found episode(s)"
        )
    return episodes

@router.get("/writer/{writer}", response_model=List[Episode], responses={status.HTTP_404_NOT_FOUND: {"model": NotFoundEpisode}})
def get_episodes_by_writer(writer: str):
    """
    Get all episodes from writer:
    ### Parameters:
    - **writer**: the writer of episode as a string e.g., David Benioff & D. B. Weiss
    """
    episodes = db.get_episodes_by_writer(writer)
    if not episodes:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Not found episode(s)"
        )
    return episodes

@router.get("/sorted_by_rating", response_model=List[Episode])
def get_episodes_by_sorted_rating():
    """
    Get all episodes in Game of Thrones series and sorted by rating
    """
    return db.get_episodes_by_sorted_rating()