import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Каталогизатор домашней библиотеки")
library = {}
def add_book():
    title = entry_title.get()
    author = entry_author.get()
    year = entry_year.get()

    if title and author and year:
        library[title] = {"author": author, "year": year}
        messagebox.showinfo("Успех", "Книга добавлена в каталог")
    else:
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля")
def show_catalog():
    catalog = ""
    for title, info in library.items():
        catalog += f"{title} - {info['author']} ({info['year']})\n"

    messagebox.showinfo("Каталог книг", catalog)
label_title = tk.Label(root, text="Название книги:")
label_title.pack()
entry_title = tk.Entry(root)
entry_title.pack()
label_author = tk.Label(root, text="Автор:")
label_author.pack()
entry_author = tk.Entry(root)
entry_author.pack()
label_year = tk.Label(root, text="Год издания:")
label_year.pack()
entry_year = tk.Entry(root)
entry_year.pack()
btn_add = tk.Button(root, text="Добавить книгу", command=add_book)
btn_add.pack()
btn_show_catalog = tk.Button(root, text="Показать каталог", command=show_catalog)
btn_show_catalog.pack()
root.mainloop()