from pydantic import BaseModel

class Rating(BaseModel):
    rating: float
    total_votes: int
    description: str
    
    class Config:
        orm_mode = True

class RatingAllDetail(Rating):
    id: int
    title: str