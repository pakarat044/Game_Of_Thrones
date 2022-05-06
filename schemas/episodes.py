from pydantic import BaseModel
from typing import Optional
from .rating import Rating

class Episode(BaseModel):
    id: int
    season: int
    episode_num: int
    title: str
    directed_by: str
    written_by: str
    us_viewers: int
    rating_id: int
    imdb_rating: Rating

    class Config:
        orm_mode = True

class NotFoundEpisode(BaseModel):
    detail: Optional[str] = "Not found episode(s)"