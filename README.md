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