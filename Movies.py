from typing import Dict, List, Optional, Iterator


class Movie:
    """Класс для представления фильма."""

    def __init__(self, title: str, year: int, genre: str, director: str, rating: float = 0.0):
        """
        Инициализация объекта фильма.
        """
        self.title = title
        self.year = year
        self.genre = genre
        self.director = director
        self.rating = rating

    def __str__(self) -> str:
        """Строковое представление фильма."""
        return f"{self.title} ({self.year}), {self.genre}, реж. {self.director}, рейтинг: {self.rating}"

    def update_rating(self, new_rating: float) -> None:
        """Обновление рейтинга фильма."""
        if 0 <= new_rating <= 10:
            self.rating = new_rating
        else:
            raise ValueError("Рейтинг должен быть между 0 и 10")


