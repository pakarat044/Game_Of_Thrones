from models.episodes import Episodes
from sqlalchemy.orm import Session


class EpisodesDAO:

    def __init__(self, session: Session):
        self.__session = session

    def get_all_episodes(self):
        episodes_list = self.__session.query(Episodes).all()
        return episodes_list

    def get_episode_by_id(self, id: int):
        episode = self.__session.query(Episodes).filter(Episodes.id == id).first()
        return episode

    def get_episodes_by_season(self, season_num: int):
        episodes_list = self.__session.query(Episodes).filter(Episodes.season == season_num).all()
        return episodes_list

    def get_episode_by_season_and_episode_num(self, season_num: int, episode_num: int):
        episode = self.__session.query(Episodes).filter(Episodes.season == season_num and Episodes.episode_num == episode_num).first()
        return episode

    def get_episode_by_title(self, title: str):
        episode = self.__session.query(Episodes).filter(Episodes.title == title).first()
        return episode

    def get_episodes_by_director(self, director: str):
        episodes_list = self.__session.query(Episodes).filter(Episodes.directed_by == director).all()
        return episodes_list

    def get_episodes_by_writer(self, writer: str):
        episodes_list = self.__session.query(Episodes).filter(Episodes.written_by == writer).all()
        return episodes_list

    def get_episodes_by_sorted_us_viewer(self):
        episodes_list = self.get_all_episodes()
        episodes_list_by_view = sorted(episodes_list, key=lambda episode: episode.us_viewers)
        return episodes_list_by_view

    def get_episodes_by_sorted_rating(self):
        # episodes_list = self.__session.query(Episodes).join(IMDBRating, Episodes.id == IMDBRating.id).all()
        episodes_list = self.get_all_episodes()
        episodes_list_by_rating = sorted(episodes_list, key=lambda episode: episode.imdb_rating.rating)
        return episodes_list_by_rating

    def create_episode(self, episode: Episodes):
        self.__session.add(episode)
        self.__session.commit()