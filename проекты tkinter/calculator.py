import tkinter as tk
from tkinter import *
from tkinter import ttk


def calculating_мсж():
    weight = float(select_weight2.get())
    height = float(select_height2.get())
    age = int(select_age2.get())
    gender = selected_gender2.get()
    lifestyle = selected_lifestyle2.get()
    bmr = 0
    if lifestyle == 'Минимальная':
        lifestyle_coefficient = 1.2
    elif lifestyle == 'Слабая':
        lifestyle_coefficient = 1.375
    elif lifestyle == 'Средняя':
        lifestyle_coefficient = 1.55
    elif lifestyle == 'Высокая':
        lifestyle_coefficient = 1.725
    elif lifestyle == 'Экстра-активность':
        lifestyle_coefficient = 1.9
    if gender == 'Мужской':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5 * lifestyle_coefficient
    elif gender == 'Женский':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161 * lifestyle_coefficient
    if selected_result == 'Похудение':
        bmr -= 400
    if selected_result == 'Набор веса':
        bmr += 400

    result_label.config(text=("Ваша норма калорий: ", bmr))

root = tk.Tk()
root.title("Калькулятор калорий")
root.geometry('400x480')

label = tk.Label(root, text='Укажите ваш пол')
label.pack(pady = 10)
selected_gender2 = tk.StringVar()
options_gender = ['Мужской', 'Женский']
combobox = ttk.Combobox(root, textvariable=selected_gender2, values=options_gender)
combobox.current(0)
combobox.pack(pady=10)

label = tk.Label(root, text='Введите ваш возвраст')
label.pack()
select_age2 = tk.StringVar()
age_entry = tk.Entry(root, textvariable=select_age2)
age_entry.pack(pady=10)

label = tk.Label(root, text='Введите ваш вес')
label.pack()
select_weight2 = tk.StringVar()
weight_entry = tk.Entry(root, textvariable=select_weight2)
weight_entry.pack(pady=10)

label = tk.Label(root, text='Введите ваш рост')
label.pack()
select_height2 = tk.StringVar()
height_entry = tk.Entry(root, textvariable=select_height2)
height_entry.pack(pady=10)

label = tk.Label(root, text='Укажите уровень вашей активности')
label.pack()
selected_lifestyle2 = tk.StringVar()
options_lifestyle = ['Минимальная', 'Слабая', 'Средняя', 'Высокая', 'Экстра-активность']
combobox = ttk.Combobox(root, textvariable=selected_lifestyle2, values=options_lifestyle)
combobox.current(0)
combobox.pack(pady=10)

label = tk.Label(root, text='Выберете для чего вы хотите расчитать калории')
label.pack(pady=10)
selected_result = tk.StringVar()
options_result = ['Похудение','Сохранение веса','Набор веса']
combobox = ttk.Combobox(root, textvariable=selected_result, values=options_result)
combobox.current(0)
combobox.pack(pady=10)

buttont = ttk.Button(root, text="Вычислить", command=calculating_мсж, style='Link.TButton')
buttont.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()