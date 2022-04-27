from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from .dao import episodes_dao, imdb_rating_dao


class GameOfThroneDB:
    def __init__(self, url: str = "sqlite:///game_of_throne.db"):
        engine = create_engine(url)
        self.__session = Session(bind=engine)

    def episodes(self):
        return episodes_dao.EpisodesDAO(self.__session)

    def rating(self):
        return imdb_rating_dao.IMDBRatingDAO(self.__session)
