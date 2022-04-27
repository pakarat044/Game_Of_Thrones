from fastapi import APIRouter
from typing import Optional
from utils.game_of_thrones_db import GameOfThroneDB

db = GameOfThroneDB().rating()

router = APIRouter(prefix="/rating", tags=["rating"])

@router.get("/")
def get_all_rating(more_than: Optional[float] = None):
    if more_than:
        return db.get_all_by_higher_rating(more_than)
    return db.get_all_rating()