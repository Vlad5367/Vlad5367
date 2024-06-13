import tkinter as tk
from PIL import Image
from customtkinter import CTk, CTkOptionMenu, CTkButton, CTkLabel, CTkImage, CTkToplevel
import random
import CTkMessagebox
class App(CTk):
    def __init__(self):
        super().__init__()
        self.mode = CTkOptionMenu(master=self, values=['Выберите режим', 'Обучение', 'Проверка'], command=self.change_mode, fg_color='#0ecf5b')
        self.mode.grid(row=1, column=0, padx=10, pady=35)
        self.categories = CTkOptionMenu(master=self, values=['Выберите категорию', 'Транспорт', 'Еда', 'Животные', 'Предметы'], command=self.change_category, fg_color='#0ecf5b')
        self.categories.grid(row=0, column=0, padx=130, pady=25)
        self.button_start = CTkButton(self, text="Начать", command=self.start_game, fg_color='#0ecf5b')
        self.button_start.grid(row=2, column=0, padx=130, pady=25)
        self.current_category = None
        self.current_mode = None
    def change_category(self, category):
        self.current_category = category
    def change_mode(self, mode):
        self.current_mode = mode
    def start_game(self):
        if self.current_category == 'Транспорт' and self.current_mode == 'Обучение':
            self.destroy()
            venche1_tutorial()
        elif self.current_category == 'Еда' and self.current_mode == 'Обучение':
            self.destroy()
            food_tutorial()
        elif self.current_category == 'Животные' and self.current_mode == 'Обучение':
            self.destroy()
            animals_tutorial()
        elif self.current_category == 'Предметы' and self.current_mode == 'Обучение':
            self.destroy()
            items_tutorial()
        elif self.current_category == 'Транспорт' and self.current_mode == 'Проверка':
            self.destroy()
            venche1_test()
        elif self.current_category == 'Еда' and self.current_mode == 'Проверка':
            self.destroy()
            food_test()
        elif self.current_category == 'Животные' and self.current_mode == 'Проверка':
            self.destroy()
            animals_test()
        elif self.current_category == 'Предметы' and self.current_mode == 'Проверка':
            self.destroy()
            items_test()
        elif self.current_category == 'Выберите категорию' and self.current_mode == 'Выберите режим':
            self.CTkMessagebox(title="Ошибка", message="Не выбран режим и категория", icon="ок")
        elif self.current_mode == 'Выберите режим':
            self.CTkMessagebox(title="Ошибка", message="Не выбран режим", icon="ок")
        elif self.current_category == 'Выберите категорию':
            self.CTkMessagebox(title="Ошибка", message="Не выбрана категория", icon="ок")
def to_menu(appv):
    appv.destroy()
    app = App()
    app.title('Изучение языка')
    app.geometry("400x430")
    app.mainloop()
def next_pictrue():
    venche1_tutorial()
def venche1_tutorial(appv=None):
    ven_spisok = ['авобус.jpeg', 'самолет.jpg', 'вело.jpg', 'кор.jpg']
    random_image_path = random.choice(ven_spisok)
    appv = CTkToplevel(master=appv)
    appv.title('Транспорт - Обучение')
    appv.geometry("400x430")
    my_image = CTkImage(light_image=Image.open(random_image_path), dark_image=Image.open(random_image_path), size=(300, 300))
    image_label = CTkLabel(master=appv, image=my_image, text="")
    image_label.grid(row=0, column=0, padx=50, pady=25)
    to_main_menu = CTkButton(master=appv, text="В меню", command=lambda: to_menu(appv), fg_color='#0ecf5b')
    to_main_menu.grid()
    appv.mainloop()
def food_tutorial(appv=None):
    food_spisok = ['торт.jpg','яблоко.jpg','шавуха.jpg','салат.jpg','пицца.jpg']
    random_image_path = random.choice(food_spisok)
    appv = CTkToplevel(master=appv)
    appv.title('Еда - Обучение')
    appv.geometry("400x430")
    my_image = CTkImage(light_image=Image.open(random_image_path), dark_image=Image.open(random_image_path), size=(300, 300))
    image_label = CTkLabel(master=appv, image=my_image, text="")
    image_label.grid(row=0, column=0, padx=50, pady=25)
    to_main_menu = CTkButton(master=appv, text="В меню", command=lambda: to_menu(appv), fg_color='#0ecf5b')
    to_main_menu.grid()
    appv.mainloop()
def animals_tutorial(appv=None):
    animals_spisok = ['мышь.jpg', 'дог.jpg', 'кот.jpg', 'лош.jpg', 'кррк.jpg']
    random_image_path = random.choice(animals_spisok)
    appv = CTkToplevel(master=appv)
    appv.title('Животные - Обучение')
    appv.geometry("400x430")
    my_image = CTkImage(light_image=Image.open(random_image_path), dark_image=Image.open(random_image_path), size=(300, 300))
    image_label = CTkLabel(master=appv, image=my_image, text="")
    image_label.grid(row=0, column=0, padx=50, pady=25)
    to_main_menu = CTkButton(master=appv, text="В меню", command=lambda: to_menu(appv), fg_color='#0ecf5b')
    to_main_menu.grid()
    appv.mainloop()
def items_tutorial(appv=None):
    items_spisok = ['бб.jpg', 'ган.jpg', 'кружка.jpg', 'ручка.jpg', 'флаг.jpg']
    random_image_path = random.choice(items_spisok)
    appv = CTkToplevel(master=appv)
    appv.title('Предметы - Обучение')
    appv.geometry("400x430")
    my_image = CTkImage(light_image=Image.open(random_image_path), dark_image=Image.open(random_image_path), size=(300, 300))
    image_label = CTkLabel(master=appv, image=my_image, text="")
    image_label.grid(row=0, column=0, padx=50, pady=25)
    to_main_menu = CTkButton(master=appv, text="В меню", command=lambda: to_menu(appv), fg_color='#0ecf5b')
    to_main_menu.grid()
    appv.mainloop()
def venche1_test(appv=None):
    ven_spisok = ['авобус.jpeg', 'самолет.jpg', 'вело.jpg', 'кор.jpg']
    random_image_path = random.choice(ven_spisok)
    appv = CTkToplevel(master=appv)
    appv.title('Транспорт - Обучение')
    appv.geometry("400x430")
    my_image = CTkImage(light_image=Image.open(random_image_path), dark_image=Image.open(random_image_path), size=(300, 300))
    image_label = CTkLabel(master=appv, image=my_image, text="")
    image_label.grid(row=0, column=0, padx=50, pady=25)
    to_main_menu = CTkButton(master=appv, text="В меню", command=lambda: to_menu(appv), fg_color='#0ecf5b')
    to_main_menu.grid()
    appv.mainloop()
def food_test(appv=None):
    food_spisok = ['торт.jpg', 'яблоко.jpg', 'шавуха.jpg', 'салат.jpg', 'пицца.jpg']
    random_image_path = random.choice(food_spisok)
    appv = CTkToplevel(master=appv)
    appv.title('Еда - Обучение')
    appv.geometry("400x430")
    my_image = CTkImage(light_image=Image.open(random_image_path), dark_image=Image.open(random_image_path), size=(300, 300))
    image_label = CTkLabel(master=appv, image=my_image, text="")
    image_label.grid(row=0, column=0, padx=50, pady=25)
    to_main_menu = CTkButton(master=appv, text="В меню", command=lambda: to_menu(appv), fg_color='#0ecf5b')
    to_main_menu.grid()
    appv.mainloop()
def animals_test(appv=None):
    animals_spisok = ['мышь.jpg', 'дог.jpg', 'кот.jpg', 'лош.jpg', 'кррк.jpg']
    random_image_path = random.choice(animals_spisok)
    appv = CTkToplevel(master=appv)
    appv.title('Животные - Обучение')
    appv.geometry("400x430")
    my_image = CTkImage(light_image=Image.open(random_image_path), dark_image=Image.open(random_image_path), size=(300, 300))
    image_label = CTkLabel(master=appv, image=my_image, text="")
    image_label.grid(row=0, column=0, padx=50, pady=25)
    to_main_menu = CTkButton(master=appv, text="В меню", command=lambda: to_menu(appv), fg_color='#0ecf5b')
    to_main_menu.grid()
    appv.mainloop()
def items_test(appv=None):
    items_spisok = ['бб.jpg', 'ган.jpg', 'кружка.jpg', 'ручка.jpg', 'флаг.jpg']
    random_image_path = random.choice(items_spisok)
    appv = CTkToplevel(master=appv)
    appv.title('Предметы - Обучение')
    appv.geometry("400x430")
    my_image = CTkImage(light_image=Image.open(random_image_path), dark_image=Image.open(random_image_path), size=(300, 300))
    image_label = CTkLabel(master=appv, image=my_image, text="")
    image_label.grid(row=0, column=0, padx=50, pady=25)
    to_main_menu = CTkButton(master=appv, text="В меню", command=lambda: to_menu(appv), fg_color='#0ecf5b')
    to_main_menu.grid()
    appv.mainloop()

app = App()
app.title('Изучение языка')
app.geometry("400x430")
app.mainloop()