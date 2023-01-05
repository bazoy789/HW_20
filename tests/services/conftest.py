import pytest
from unittest.mock import MagicMock

from dao.model.movie import Movie
from dao.movie import MovieDAO
from dao.model.director import Director
from dao.director import DirectorDAO
from dao.model.genre import Genre
from dao.genre import GenreDAO


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


@pytest.fixture
def director_dao():
    director_dao=DirectorDAO(session=None)

    director1 = Director(id=1,name='Баз Лурман')
    director2 = Director(id=2,name='Пьетро Антон')

    director_dao.get_one = MagicMock(return_value=director1)
    director_dao.get_all = MagicMock(return_value=[director1, director2])
    director_dao.create = MagicMock(return_value=Director(id=2))
    director_dao.delete = MagicMock(return_value=Director(id=2))
    director_dao.update = MagicMock(return_value=Director(id=1))

    return director_dao


@pytest.fixture
def genre_dao():
    genre_dao = GenreDAO(session=None)

    genre1 = Genre(id=1, name='Ужасы')
    genre2 = Genre(id=2, name='Боевик')

    genre_dao.get_one=MagicMock(return_value=genre1)
    genre_dao.get_all=MagicMock(return_value=[genre1, genre2])
    genre_dao.create=MagicMock(return_value=Genre(id=2))
    genre_dao.delete=MagicMock(return_value=Genre(id=2))
    genre_dao.update=MagicMock(return_value=Genre(id=1))

    return genre_dao