import tkinter as tk
from tkinter import ttk
def calculating():
    coordinates = uravnenye_entry.get()
    coords = coordinates.split(',')
    x1, y1, x2, y2 = map(float, coords)
    length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    result_label.config(text=f'Длина отрезка: {length}')
root = tk.Tk()
root.title('Вычисление длины отрезка')
root.geometry('500x500')
label = ttk.Label(root, text='Введите координаты двух точек в формате x1, y1, x2, y2: ')
label.pack(pady=10)
uravnenye_entry = tk.Entry(root)
uravnenye_entry.pack(pady=10)
label_result = ttk.Label(root, text='Ответ:')
label_result.pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack()
buttont = ttk.Button(root, text="Вычислить", command=calculating)
buttont.pack(pady=10)
root.mainloop()