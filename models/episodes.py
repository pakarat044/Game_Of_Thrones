from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Text, ForeignKey
from .base import Base


class Episodes(Base):
    __tablename__ = 'episodes'

    id = Column(Integer, primary_key=True)
    season = Column(Integer, nullable=False)
    episode_num = Column(Integer, nullable=False)
    title = Column(Text, nullable=False)
    directed_by = Column(Text, nullable=False)
    written_by = Column(Text, nullable=False)
    us_viewers = Column(Integer, nullable=False)
    rating_id = Column(Integer, ForeignKey("imdb_rating.id"), nullable=False)

    imdb_rating = relationship("IMDBRating", back_populates="episodes")

    def __repr__(self) -> str:
        return f"<Episodes(id={self.id}, season={self.season}, episode_num={self.episode_num}, title={self.title}, directed_by={self.directed_by}, written_by={self.written_by}, us_viewers={self.us_viewers})>"
