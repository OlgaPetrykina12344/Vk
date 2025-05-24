from typing import List,Dict
from Movies import Movie

class MovieCollection:
    """
    Класс для управления коллекцией фильмов.
    """

    def __init__(self):
        """
        Инициализация коллекции фильмов (хранится в словаре).
        """
        self.movies: Dict[str, Movie] = {}
        self.collections: Dict[str, List[Movie]] = {}

    def add_movie(self, movie: Movie) -> None:
        """
        Добавление фильма в коллекцию.
        """
        if movie.title in self.movies:
            raise ValueError(f"Фильм '{movie.title}' уже существует в коллекции.")
        self.movies[movie.title] = movie

    def remove_movie(self, title: str) -> None:
        """
        Удаление фильма из коллекции.
        """
        if title not in self.movies:
            raise ValueError(f"Фильм '{title}' не найден в коллекции.")

        for collection in self.collections.values():
            if self.movies[title] in collection:
                collection.remove(self.movies[title])

        del self.movies[title]

    def create_collection(self, name: str) -> None:
        """
        Создание новой коллекции фильмов.
        """
        if name in self.collections:
            raise ValueError(f"Коллекция '{name}' уже существует.")
        self.collections[name] = []

    def add_to_collection(self, movie_title: str, collection_name: str) -> None:
        """
        Добавление фильма в коллекцию.
        """
        if movie_title not in self.movies:
            raise ValueError(f"Фильм '{movie_title}' не найден.")

        if collection_name not in self.collections:
            raise ValueError(f"Коллекция '{collection_name}' не найдена.")

        movie = self.movies[movie_title]
        if movie in self.collections[collection_name]:
            raise ValueError(f"Фильм '{movie_title}' уже есть в коллекции '{collection_name}'.")

        self.collections[collection_name].append(movie)