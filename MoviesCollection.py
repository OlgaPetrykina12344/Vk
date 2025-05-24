from typing import List,Dict
from Movies import Movie

class MovieCollection:
    """Класс для управления коллекцией фильмов."""

    def __init__(self):
        """Инициализация коллекции фильмов (хранится в словаре)."""
        self.movies: Dict[str, Movie] = {}
        self.collections: Dict[str, List[Movie]] = {}

    def add_movie(self, movie: Movie) -> None:
        """
        Добавление фильма в коллекцию.
        """
        if movie.title in self.movies:
            raise ValueError(f"Фильм '{movie.title}' уже существует в коллекции.")
        self.movies[movie.title] = movie

