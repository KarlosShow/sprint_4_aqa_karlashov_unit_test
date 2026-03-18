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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_added_in_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Смешарики')
        assert 'Смешарики' in collector.book_genre

    def test_add_new_book_existing_name(self):
        collector = BooksCollector()
        
        collector.add_new_book('Хоббит')
        collector.add_new_book('Хоббит')
        assert len(collector.books_genre) == 1    

@pytest.mark.parametrize('name', [
    "Книга с именем, которое слишком длинное для добавления в систему",
    "",
    "А"
])
def test_add_new_book_invalid_length(name):
    collector = BooksCollector()
    collector.add_new_book(name)
    assert name not in collector.books_genre
    
def test_set_book_genre_success():
    collector = BooksCollector()
    collector.books_genre["Поле битвы земля"] = ""
    collector.set_book_genre("Поле битвы земля", "Фантастика")
    assert collector.books_genre["Поле битвы земля"] == "Фантастика"

def test_set_book_genre_invalid_genre():
    collector = BooksCollector()
    collector.books_genre["Аватар"] = ""
    collector.set_book_genre("Аватар", "Фэнтези")
    assert collector.books_genre["Аватар"] == ""    

