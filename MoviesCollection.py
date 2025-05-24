from typing import List, Dict, Iterator
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

    def remove_from_collection(self, movie_title: str, collection_name: str) -> None:
        """
        Удаление фильма из коллекции.
        """
        if movie_title not in self.movies:
            raise ValueError(f"Фильм '{movie_title}' не найден.")

        if collection_name not in self.collections:
            raise ValueError(f"Коллекция '{collection_name}' не найдена.")

        movie = self.movies[movie_title]
        if movie not in self.collections[collection_name]:
            raise ValueError(f"Фильм '{movie_title}' не найден в коллекции '{collection_name}'.")

        self.collections[collection_name].remove(movie)

    def search_movies(self, **kwargs) -> List[Movie]:
        """
        Поиск фильмов по различным критериям.
        """
        results = []

        for movie in self.movies.values():
            match = True

            if 'title' in kwargs and kwargs['title'].lower() not in movie.title.lower():
                match = False
            if 'year' in kwargs and kwargs['year'] != movie.year:
                match = False
            if 'genre' in kwargs and kwargs['genre'].lower() != movie.genre.lower():
                match = False
            if 'director' in kwargs and kwargs['director'].lower() not in movie.director.lower():
                match = False
            if 'min_rating' in kwargs and movie.rating < kwargs['min_rating']:
                match = False

            if match:
                results.append(movie)

        return results

    def __iter__(self) -> Iterator[Movie]:
        """
        Реализация итератора для перебора коллекции фильмов.
        """
        return iter(self.movies.values())

    def list_movies(self) -> List[Movie]:
        """
        Получить список всех фильмов в коллекции.
        """
        return list(self.movies.values())

    def list_collections(self) -> Dict[str, List[Movie]]:
        """
        Получить словарь всех коллекций и их содержимого.
        """
        return self.collections.copy()


