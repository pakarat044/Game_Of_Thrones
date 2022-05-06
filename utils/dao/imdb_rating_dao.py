from models.imdb_rating import IMDBRating
from sqlalchemy.orm import Session

class IMDBRatingDAO:

    def __init__(self, session: Session):
        self.__session = session
    
    def get_all_rating(self):
        rating_list = self.__session.query(IMDBRating).all()
        return rating_list

    def get_all_by_higher_rating(self, rating: float):
        rating_list = self.__session.query(IMDBRating).filter(IMDBRating.rating >= rating).all()
        return rating_list
