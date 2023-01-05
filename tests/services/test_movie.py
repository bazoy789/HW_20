import pytest
from unittest.mock import MagicMock

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService

@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(session=None)

    movie1 = Movie(id=1,
                   title='Чикаго',
                   description='Рокси Харт мечтает о песнях и танцах и о том, как сравняться с самой Велмой Келли, примадонной водевиля. И Рокси действительно оказывается с Велмой в одном положении, когда несколько очень неправильных шагов приводят обеих на скамью подсудимых.',
                   trailer='https://www.youtube.com/watch?v=YxzS_LzWdG8',
                   year=2002,
                   rating=7.2)

    movie2 = Movie(id=2,
                   title='Одержимость',
                   description='Эндрю мечтает стать великим. Казалось бы, вот-вот его мечта осуществится. Юношу замечает настоящий гений, дирижер лучшего в стране оркестра. Желание Эндрю добиться успеха быстро становится одержимостью, а безжалостный наставник продолжает подталкивать его все дальше и дальше – за пределы человеческих возможностей. Кто выйдет победителем из этой схватки?',
                   trailer='https://www.youtube.com/watch?v=Q9PxDPOo1jw',
                   year=2013,
                   rating=8.5)

    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2])
    movie_dao.create = MagicMock(return_value=Movie(id=2))
    movie_dao.delete = MagicMock(return_value=Movie(id=2))
    movie_dao.update = MagicMock(return_value=Movie(id=1))

    return movie_dao

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

