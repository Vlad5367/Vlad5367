import customtkinter as ctk
from tkinter import messagebox
import sqlite3
from CTkListbox import *

conn = sqlite3.connect('recipes.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS recipes
             (id INTEGER PRIMARY KEY,
              title TEXT,
              ingredients TEXT,
              instructions TEXT)''')

def show_recipe(selected_item):
    recipe_details = c.execute("SELECT * FROM recipes WHERE title=?", (selected_item,)).fetchone()
    show_recipe_window(recipe_details)

def add_recipe():
    title = title_entry.get()
    ingredients = ingredients_entry.get('1.0', 'end-1c')
    instructions = instructions_entry.get('1.0', 'end-1c')
    c.execute("INSERT INTO recipes (title, ingredients, instructions) VALUES (?, ?, ?)",
              (title, ingredients, instructions))
    conn.commit()
    clear_fields()
    refresh_recipe_list()

def delete_recipe():
    selected_indices = listbox.curselection()
    if selected_indices:
        for index in reversed(selected_indices):
            selected_item = listbox.get(index)
            c.execute("DELETE FROM recipes WHERE title=?", (selected_item,))
            conn.commit()
        refresh_recipe_list()
    else:
        messagebox.showinfo("Ошибка", "Не выбран ни один рецепт для удаления.")

def show_recipe_window(recipe_details):
    recipe_window = ctk.CTkToplevel(root)
    recipe_window.title(recipe_details[1])

    ingredients_label = ctk.CTkLabel(recipe_window, text="Ингредиенты:")
    ingredients_label.grid(row=0, column=0, padx=5, pady=5)

    ingredients_text = ctk.CTkTextbox(recipe_window, width=100, height=20)
    ingredients_text.insert('end', recipe_details[2])
    ingredients_text.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

    instructions_label = ctk.CTkLabel(recipe_window, text="Инструкции:")
    instructions_label.grid(row=1, column=0, padx=5, pady=5)

    instructions_text = ctk.CTkTextbox(recipe_window, width=100, height=20)
    instructions_text.insert('end', recipe_details[3])
    instructions_text.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

    close_button = ctk.CTkButton(recipe_window, text="Закрыть", command=recipe_window.destroy)
    close_button.grid(row=2, column=1, padx=5, pady=5)

def clear_fields():
    title_entry.delete(0, 'end')
    ingredients_entry.delete('1.0', 'end')
    instructions_entry.delete('1.0', 'end')

def refresh_recipe_list():
    listbox.delete(0, 'end')
    recipes = c.execute("SELECT * FROM recipes").fetchall()
    for recipe in recipes:
        listbox.insert('end', recipe[1])

root = ctk.CTk()
root.title("Справочник рецептов")

title_label = ctk.CTkLabel(root, text="Название рецепта:")
title_label.grid(row=0, column=0, padx=5, pady=5)

title_entry = ctk.CTkEntry(root, width=100)
title_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

ingredients_label = ctk.CTkLabel(root, text="Ингредиенты:")
ingredients_label.grid(row=1, column=0, padx=5, pady=5)

ingredients_entry = ctk.CTkTextbox(root, width=100, height=10)
ingredients_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

instructions_label = ctk.CTkLabel(root, text="Инструкции:")
instructions_label.grid(row=2, column=0, padx=5, pady=5)

instructions_entry = ctk.CTkTextbox(root, width=100, height=10)
instructions_entry.grid(row=2, column=1, padx=5, pady=5, columnspan=2)

add_button = ctk.CTkButton(root, text="Добавить рецепт", command=add_recipe)
add_button.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

listbox = CTkListbox(root, command=show_recipe, width=100, height=20)
listbox.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

delete_button = ctk.CTkButton(root, text="Удалить рецепт", command=delete_recipe)
delete_button.grid(row=5, column=2, padx=5, pady=5)

refresh_recipe_list()

root.mainloop()
conn.close()
