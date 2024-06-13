import json


def main():
    library = load_library()

    while True:
        print("\n1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Просмотреть список книг")
        print("4. Сохранить и выйти")

        choice = input("\nВыберите действие: ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            display_books(library)
        elif choice == '4':
            save_library(library)
            break
        else:
            print("Ошибка! Неверный выбор. Попробуйте снова.")


def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"books": []}


def save_library(library):
    with open("library.json", "w") as file:
        json.dump(library, file)
def add_book(library):
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    genre = input("Введите жанр книги: ")

    book = {"title": title, "author": author, "genre": genre}
    library["books"].append(book)


def remove_book(library):
    title = input("Введите название книги, которую хотите удалить: ")

    for book in library["books"]:
        if book["title"] == title:
            library["books"].remove(book)
            print("Книга успешно удалена.")
            return

    print("Книга не найдена.")


def display_books(library):
    if not library["books"]:
        print("Библиотека пуста.")
        return

    print("\nСписок книг в библиотеке:")
    for i, book in enumerate(library["books"], 1):
        print(f"{i}. Название: {book['title']}, Автор: {book['author']}, Жанр: {book['genre']}")


if __name__ == "__main__":
    main()