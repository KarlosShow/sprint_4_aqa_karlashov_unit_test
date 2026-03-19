import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_book_title_added_to_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Смешарики')
        assert 'Смешарики' in collector.books_genre

    def test_add_new_book_duplicate_title_not_added(self):
        collector = BooksCollector()
        
        collector.add_new_book('Хоббит')
        collector.add_new_book('Хоббит')
        assert len(collector.books_genre) == 1    

@pytest.mark.parametrize('name', [
    "Книга с именем, которое слишком длинное для добавления в систему",
    ""
])
def test_add_new_book_title_length_validation(name):
    collector = BooksCollector()
    collector.add_new_book(name)
    assert name not in collector.books_genre
    
def test_set_book_genre_valid_genre_set():
    collector = BooksCollector()
    collector.books_genre["Поле битвы земля"] = ""
    collector.set_book_genre("Поле битвы земля", "Фантастика")
    assert collector.books_genre["Поле битвы земля"] == "Фантастика"

def test_set_book_genre_invalid_genre_not_set():
    collector = BooksCollector()
    collector.books_genre["Аватар"] = ""
    collector.set_book_genre("Аватар", "Фэнтези")
    assert collector.books_genre["Аватар"] == ""    

def test_get_book_genre_returns_correct_genre():
    collector = BooksCollector()
    collector.books_genre["Какая то фантастика"] = "Фантастика"
    assert collector.get_book_genre("Какая то фантастика") == "Фантастика"

def test_get_books_for_children_returns_suitable_books():
    collector = BooksCollector()
    collector.books_genre = {
        "Лунтик": "Фантастика",
        "Лепрекон": "Ужасы",
        "Один дома": "Комедии",
    }

    books_for_children = collector.get_books_for_children()
    assert "Лунтик" in books_for_children
    assert "Один дома" in books_for_children
    assert "Лепрекон" not in books_for_children

def test_get_books_for_children_empty_collection_returns_empty_list():
    collector = BooksCollector()
    collector.books_genre = {}
    books_for_children = collector.get_books_for_children()
    assert books_for_children == []

def test_add_book_in_favorites_book_added_to_favorites():
    collector = BooksCollector()
    book_name = "Ужасающий"
    collector.books_genre[book_name] = "Ужасы"
    collector.add_book_in_favorites(book_name)
    assert book_name in collector.favorites

def test_add_book_in_favorites_non_existent_book_not_added():
    collector = BooksCollector()
    book_name = "Книга, которой нет в коллекции"
    collector.add_book_in_favorites(book_name)
    assert book_name not in collector.favorites

def test_delete_book_from_favorites_deleted_successfully():
    collector = BooksCollector()
    book_name = "будем удалять"
    collector.favorites.append(book_name)
    collector.delete_book_from_favorites(book_name)
    assert book_name not in collector.favorites

def test_get_list_of_favorites_returns_list_of_favorite_books():
    collector = BooksCollector()

    collector.favorites.append("Водный мир")
    collector.favorites.append("Мошенники")
    favorites_list = collector.get_list_of_favorites_books()
    assert "Водный мир" in favorites_list
    assert "Мошенники" in favorites_list

