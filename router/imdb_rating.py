from fastapi import APIRouter
from typing import Optional, List
from utils.game_of_thrones_db import GameOfThroneDB
from schemas.rating import RatingAllDetail

db = GameOfThroneDB().rating()

router = APIRouter(prefix="/rating", tags=["rating"])

@router.get("/", response_model=List[RatingAllDetail])
def get_all_rating(more_than: Optional[float] = None):
    """
    Get all IMDB rating in Game of Thrones series
    ### Query parameters:
    - **more_than**: (Optional) Return rating that equal or higher than your provide.
    """
    if more_than:
        return db.get_all_by_higher_rating(more_than)
    return db.get_all_rating()