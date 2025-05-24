from Movies import Movie
from MoviesCollection import MovieCollection


def display_movies(movies: list, title: str = "Фильмы"):
    """Вспомогательная функция для отображения списка фильмов."""
    print(f"\n{title}:")
    if not movies:
        print("  Нет фильмов")
        return

    for i, movie in enumerate(movies, 1):
        print(f"  {i}. {movie}")


def test_movie_collection():
    """Тестирование функциональности коллекции фильмов."""
    print("\n=== Тестирование коллекции фильмов ===")

    # Инициализация коллекции
    collection = MovieCollection()

    # Тест 1: Добавление фильмов
    print("\nТест 1: Добавление фильмов")
    try:
        movies_to_add = [
            Movie("Крепкий орешек", 1988, "боевик", "Джон Мактирнан", 8.2),
            Movie("Побег из Шоушенка", 1994, "драма", "Фрэнк Дарабонт", 9.3),
            Movie("Зеленая миля", 1999, "фэнтези", "Фрэнк Дарабонт", 9.1),
            Movie("Форрест Гамп", 1994, "драма", "Роберт Земекис", 8.8)
        ]

        for movie in movies_to_add:
            collection.add_movie(movie)
            print(f"Добавлен: {movie.title}")

        display_movies(collection.list_movies(), "Все фильмы в коллекции")
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Тест 2: Создание коллекций
    print("\nТест 2: Создание коллекций")
    try:
        collection.create_collection("Классика")
        collection.create_collection("Драмы")
        print("Созданы коллекции: Классика, Драмы")
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Тест 3: Добавление в коллекции
    print("\nТест 3: Добавление в коллекции")
    try:
        collection.add_to_collection("Побег из Шоушенка", "Классика")
        collection.add_to_collection("Зеленая миля", "Классика")
        collection.add_to_collection("Форрест Гамп", "Классика")
        collection.add_to_collection("Побег из Шоушенка", "Драмы")
        collection.add_to_collection("Зеленая миля", "Драмы")
        print("Фильмы успешно добавлены в коллекции")

        # Просмотр содержимого коллекций
        print("\nСодержимое коллекций:")
        for name, movies in collection.list_collections().items():
            display_movies(movies, f"Коллекция '{name}'")
    except ValueError as e:
        print(f"Ошибка: {e}")

    # Тест 4: Поиск фильмов
    print("\nТест 4: Поиск фильмов")

    # Поиск по году
    movies_1994 = collection.search_movies(year=1994)
    display_movies(movies_1994, "Фильмы 1994 года")

    # Поиск по режиссеру
    darabont_movies = collection.search_movies(director="Дарабонт")
    display_movies(darabont_movies, "Фильмы Фрэнка Дарабонта")

    # Поиск по рейтингу
    top_movies = collection.search_movies(min_rating=9.0)
    display_movies(top_movies, "Фильмы с рейтингом 9.0+")

    # Тест 5: Итерация по коллекции
    print("\nТест 5: Итерация по коллекции")
    print("Все фильмы (через итератор):")
    for movie in collection:
        print(f"  - {movie.title} ({movie.year})")

    # Тест 6: Удаление фильма
    print("\nТест 6: Удаление фильма")
    try:
        collection.remove_movie("Крепкий орешек")
        print("Фильм 'Крепкий орешек' удален")
        display_movies(collection.list_movies(), "Оставшиеся фильмы")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    test_movie_collection()
    print("\n=== Тестирование завершено ===")