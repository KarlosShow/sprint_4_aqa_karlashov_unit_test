# qa_python
репозиторий переименован на гит хабе 
sprint_4_aqa_karlashov_unit_test

добавили юнит тесты в tests.py

# проверка добавления новой книги: название книги добавлено в жанры книг.
    test_add_new_book_book_title_added_to_books_genre
# проверка добавления новой книги: дубликат названия не добавляется
    test_add_new_book_duplicate_title_not_added
# проверка добавления новой книги: валидация длины названия
    test_add_new_book_title_length_validation
# проверка установки жанра книги: корректный жанр установлен    
    test_set_book_genre_valid_genre_set
# проверка установки жанра книги: некорректный жанр не установлен.
    test_set_book_genre_invalid_genre_not_set
#  проверка получения жанра книги: возвращается корректный жанр.
    test_get_book_genre_returns_correct_genre
# проверка получения книг для детей: возвращаются подходящие книги
    test_get_books_for_children_returns_suitable_books
# проверка получения книг для детей из пустой коллекции: возвращается пустой список
    test_get_books_for_children_empty_collection_returns_empty_list
#  проверка добавления книги в избранное: книга добавлена в избранное
    test_add_book_in_favorites_book_added_to_favorites
# проверка добавления несуществующей книги в избранное: не добавлена
    test_add_book_in_favorites_non_existent_book_not_added
# проверка удаления книги из избранного: успешно удалена
    test_delete_book_from_favorites_deleted_successfully
# проверка получения списка избранных книг: возвращается список любимых книг.
    test_get_list_of_favorites_returns_list_of_favorite_books
# проверка при вызове словаря словарь вызывается с дабавленной книгой и добавленным жанром
    test_get_books_genre_returns_correct_dictionary
# проверка при вывозе книги по имени выводится ее жанр
    test_get_book_genre_correct_genre

Результат запуска тестов:
                    pytest -v tests.py
======================================= test session starts ======================================== 
platform win32 -- Python 3.14.2, pytest-9.0.2, pluggy-1.6.0 -- C:\Users\Сергей\AppData\Local\Programs\Python\Python314\python.exe
cachedir: .pytest_cache 
rootdir: C:\Users\Сергей\unit_test_4s\qa_python
plugins: cov-7.0.0
collected 14 items                                                                                   

tests.py::TestBooksCollector::test_add_new_book_add_two_books PASSED                          [  7%] 
tests.py::TestBooksCollector::test_add_new_book_book_title_added_to_books_genre PASSED        [ 14%] 
tests.py::TestBooksCollector::test_add_new_book_duplicate_title_not_added PASSED              [ 21%] 
tests.py::test_add_new_book_title_length_validation[\u041a\u043d\u0438\u0433\u0430 \u0441 \u0438\u043c\u0435\u043d\u0435\u043c, \u043a\u043e\u0442\u043e\u0440\u043e\u0435 \u0441\u043b\u0438\u0448\u043a\u043e\u043c \u0434\u043b\u0438\u043d\u043d\u043e\u0435 \u0434\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443] PASSED [ 28%]   
tests.py::test_add_new_book_title_length_validation[] PASSED                                  [ 35%] 
tests.py::test_set_book_genre_valid_genre_set PASSED                                          [ 42%] 
tests.py::test_set_book_genre_invalid_genre_not_set PASSED                                    [ 50%] 
tests.py::test_get_book_genre_returns_correct_genre PASSED                                    [ 57%] 
tests.py::test_get_books_for_children_returns_suitable_books PASSED                           [ 64%] 
tests.py::test_get_books_for_children_empty_collection_returns_empty_list PASSED              [ 71%] 
tests.py::test_add_book_in_favorites_book_added_to_favorites PASSED                           [ 78%] 
tests.py::test_add_book_in_favorites_non_existent_book_not_added PASSED                       [ 85%] 
tests.py::test_delete_book_from_favorites_deleted_successfully PASSED                         [ 92%] 
tests.py::test_get_list_of_favorites_returns_list_of_favorite_books PASSED                    [100%] 

======================================== 14 passed in 0.28s ========================================

Оценка покрытия
PS C:\Users\Сергей\unit_test_4s\qa_python>  pytest --cov=main tests.py
======================================= test session starts ======================================== 
platform win32 -- Python 3.14.2, pytest-9.0.2, pluggy-1.6.0
rootdir: C:\Users\Сергей\unit_test_4s\qa_python 
plugins: cov-7.0.0
collected 14 items                                                                                   

tests.py ..............                                                                       [100%] 

========================================== tests coverage ========================================== 
_________________________ coverage: platform win32, python 3.14.2-final-0 __________________________ 

Name      Stmts   Miss  Cover
-----------------------------
main.py      38      6    84%
-----------------------------
TOTAL        38      6    84%
======================================== 14 passed in 0.26s ========================================