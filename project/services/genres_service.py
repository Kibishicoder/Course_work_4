from project.dao.genre import GenreDAO
from project.schemas.genre import GenreSchema
from project.exceptions import GenreNotFound


class GenresService:

    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_item_by_id(self, pk: int):
        genre = self.genre_dao.get_by_id(pk)
        if not genre:
            raise GenreNotFound
        return GenreSchema().dump(genre)

    def get_all_genres(self, filter):
        if filter.get("page"):
            genres = self.genre_dao.get_all_by_page(filter.get("page"))
        else:
            genres = self.genre_dao.get_all()
        return GenreSchema(many=True).dump(genres)