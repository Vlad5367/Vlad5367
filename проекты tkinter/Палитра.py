import tkinter as tk
from tkinter import ttk
def display_color_info():
    color_name = color_entry.get()
    color_code = colors.get(color_name, "Цвет не найден")
    color_info_label.config(text=f'Цвет: {color_name}\nКод: {color_code}')
colors = {
    "Красный": "#FF0000",
    "Зеленый": "#00FF00",
    "Синий": "#0000FF",
    "Желтый": "#FFFF00",
    "Фиолетовый": "#800080",
    "Оранжевый": "#FFA500",
    "Голубой": "#00FFFF",
    "Розовый": "#FFC0CB",
}
root = tk.Tk()
root.title('Палитра цветов')
root.geometry('400x200')
color_label = ttk.Label(root, text='Выберите цвет:')
color_label.pack(pady=10)
color_entry = ttk.Combobox(root, values=list(colors.keys()))
color_entry.pack(pady=5)
color_entry.current(0)
display_button = ttk.Button(root, text="Показать информацию", command=display_color_info)
display_button.pack(pady=5)
color_info_label = ttk.Label(root, text="")
color_info_label.pack(pady=10)
root.mainloop()