from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Float, Integer, Text, null
from .base import Base

class IMDBRating(Base):
    __tablename__ = 'imdb_rating'
    
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    rating = Column(Float, nullable=False)
    total_votes = Column(Integer, nullable=False)
    description = Column(Text)

    episodes = relationship("Episodes", back_populates="imdb_rating")

    def __repr__(self) -> str:
        return f"<IMDBRating(id={self.id}, title={self.title}, rating={self.rating}, total_votes={self.total_votes}, description={self.description})>"