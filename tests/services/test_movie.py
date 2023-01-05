import pytest

from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_services = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_services.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_services.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie_c = {
            'title':'1',
            'description':'1',
            'trailer':'1',
            'year':2000,
            'rating':10
        }

        movie = self.movie_services.create(movie_c)

        assert movie.id is not None

    def test_delete(self):
        movie = self.movie_services.delete(1)

        assert movie is None

    def test_update(self):
        movie_c = {
            'title': '2',
            'description': '2',
            'trailer': '2',
            'year': 2000,
            'rating': 10
        }

        self.movie_services.update(movie_c)

