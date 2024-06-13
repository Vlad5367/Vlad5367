import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
def destroy_all():#кнопка закрытия всех окон
    all_windows = root.winfo_children()
    for window in all_windows:
        window.destroy()
        sys.exit()

def endwindow1(): #еще один цевток, если выбрали не получать подарок
    root.withdraw()
    root5 = tk.Toplevel()
    root5.title('ПОЗДРАВЛЕНИЕ!!!')
    root5.geometry('800x600')
    root5['background'] = '#F48FB1'
    image1 = Image.open('flovers1.png')
    image1 = image1.resize((image1.width // 6, image1.height // 6))
    photo1 = ImageTk.PhotoImage(image1)
    label = tk.Label(root5, image=photo1, highlightbackground='#F48FB1')
    label.pack(pady=30)
    label_zabrat = tk.Label(root5,text='Сегодня ты словно яркие цветы, привносящие радость и тепло своим присутствием. Твоя улыбка освещает этот день, а твоя энергия заряжает всех вокруг позитивом. Пусть этот день будет для тебя таким же ярким и радостным, как ты сама!',font=('Comic Sans MS', 20), wraplength = 700, justify = 'center', bg = '#F48FB1')
    label_zabrat.pack()
    image4 = Image.open('выкл.png')
    image4 = image4.resize((image4.width // 7, image4.height // 7))
    photo4 = ImageTk.PhotoImage(image4)
    button3 = tk.Button(root5, image=photo4, command=lambda: (root5.destroy(), destroy_all()))
    button3.photo = photo4
    button3.pack()
    root5.mainloop()
def endwindow2(): #pvz цветок, если выбрали не получать подарок
    root.withdraw()
    root5 = tk.Toplevel()
    root5.title('ПОДСОЛНУХ ИЗ PvZ???')
    root5.geometry('800x600')
    root5['background'] = '#F48FB1'
    image2 = Image.open('послолн.png')
    image2 = image2.resize((image2.width // 6, image2.height // 6))
    photo2 = ImageTk.PhotoImage(image2)
    label = tk.Label(root5, image=photo2, highlightbackground='#F48FB1')
    label.pack(pady=30)
    label_zabrat = tk.Label(root5,text='Ты как подсолнух из игры PvZ — всегда стремишься к свету и расцветаешь с новой силой каждый день. Твоя энергия и оптимизм поднимают настроение окружающим, а твоя улыбка – подобно солнцу – согревает сердца. Пусть твоя жизнь будет наполнена яркими моментами и новыми достижениями!',font=('Comic Sans MS', 20), wraplength=700, justify='center', bg='#F48FB1')
    label_zabrat.pack()
    image4 = Image.open('выкл.png')
    image4 = image4.resize((image4.width // 7, image4.height // 7))
    photo4 = ImageTk.PhotoImage(image4)
    button3 = tk.Button(root5, image=photo4, command=lambda: (root5.destroy(), destroy_all()))
    button3.photo = photo4
    button3.pack()
    root5.mainloop()
def endwindow3():#еще один цевток, если выбрали не получать подарок
    root.withdraw()
    root5 = tk.Toplevel()
    root5.title('ПОЗДРАВЛЕНИЕ!!!')
    root5.geometry('800x600')
    root5['background'] = '#F48FB1'
    image3 = Image.open('flovers3.png')
    image3 = image3.resize((image3.width // 6, image3.height // 6))
    photo3 = ImageTk.PhotoImage(image3)
    label = tk.Label(root5, image=photo3, highlightbackground='#F48FB1')
    label.pack(pady=30)
    label_zabrat = tk.Label(root5, text='Сегодня ты как темные цветы, притягивающие внимание своей загадочностью и глубиной. Ты умеешь видеть красоту в том, что не всегда на поверхности, и твоя мудрость делает тебя уникальной. Пусть этот день принесет тебе новые открытия и вдохновение!', font=('Comic Sans MS', 20), wraplength=700, justify='center', bg='#F48FB1')
    label_zabrat.pack()
    image4 = Image.open('выкл.png')
    image4 = image4.resize((image4.width // 7, image4.height // 7))
    photo4 = ImageTk.PhotoImage(image4)
    button3 = tk.Button(root5, image=photo4, command=lambda: (root5.destroy(), destroy_all()))
    button3.photo = photo4
    button3.pack()
    root5.mainloop()
def вбой():#Начальное окно, надо нажать кнопку в бой
    for i in range(3):
        messagebox.showerror("Ошибка", "Произошла ошибка!")
    result = messagebox.askokcancel("Подарок?", "ВЫ ХОТИТЕ ЗАБРАТЬ ПОДАРОК?")
    if result:
        open_window_2()
        root.withdraw()
    else:
        open_window_3()
        root.withdraw()
def gift():#это подарок
    root.withdraw()
    root6 = tk.Toplevel()
    root6.title('ПОЗДРАВЛЕНИЕ!!!')
    root6.geometry('750x500')
    root6['background'] = '#F48FB1'
    root6.photo = ImageTk.PhotoImage(Image.open('dar.png'))
    label_image = tk.Label(root6, image=root6.photo, relief="solid", highlightbackground='#F48FB1')
    label_image.pack(pady=20)
    image4 = Image.open('выкл.png')
    image4 = image4.resize((image4.width // 7, image4.height // 7))
    photo4 = ImageTk.PhotoImage(image4)
    button3 = tk.Button(root6, image=photo4, command=destroy_all)
    button3.photo = photo4
    button3.pack()
    root6.mainloop()
def open_window_2():#если мы нажали да при получение подарка
    root.withdraw()
    root1 = tk.Toplevel()
    root1.title('ПОЗДРАВЛЕНИЕ!!!')
    root1.geometry('712x580')
    root1['background'] = '#F48FB1'
    root1.photo = ImageTk.PhotoImage(Image.open('gift.png'))
    label_image = tk.Label(root1, image=root1.photo, relief="solid", highlightbackground='#F48FB1')
    label_image.pack(pady=20)
    label_zabrat = tk.Label(root1, text='Нажми кнопку чтобы забрать подарок!!!', font=('Comic Sans MS', 25),bg='#F48FB1')
    label_zabrat.pack()
    button_image = ImageTk.PhotoImage(Image.open('zabr.png'))
    button = tk.Button(root1, image=button_image, relief="solid", highlightbackground='#F48FB1', command=gift)
    button.image = button_image
    button.pack(pady=20)

def open_window_3():#если мы нажали отмена при получение подарка
    root.withdraw()
    root2 = tk.Toplevel()
    root2.title('ПОЗДРАВЛЕНИЕ!!!')
    root2.geometry('1050x700')
    root2['background'] = '#F48FB1'
    image = Image.open('rr.png')
    image = image.resize((image.width // 7, image.height // 7))
    photo = ImageTk.PhotoImage(image)
    label2 = tk.Label(root2, image=photo)
    label2.image = photo
    label2.pack(pady=20)
    label = tk.Label(root2, text='Выбери какой ты сегодня цветок.', font=('Comic Sans MS', 25), bg='#F48FB1')
    label.pack(pady=30)
    image1 = Image.open('flovers1.png')
    image1 = image1.resize((image1.width // 7, image1.height // 7))
    photo1 = ImageTk.PhotoImage(image1)
    button1 = tk.Button(root2, image=photo1, command=endwindow1)
    button1.photo = photo1
    button1.pack(side='left', padx=30, pady=110)
    image2 = Image.open('послолн.png')
    image2 = image2.resize((image2.width // 7, image2.height // 7))
    photo2 = ImageTk.PhotoImage(image2)
    button2 = tk.Button(root2, image=photo2, command=endwindow2)
    button2.photo = photo2
    button2.pack(side='left', padx=20, pady=110)
    image3 = Image.open('flovers3.png')
    image3 = image3.resize((image3.width // 7, image3.height // 7))
    photo3 = ImageTk.PhotoImage(image3)
    button3 = tk.Button(root2, image=photo3, command=endwindow3)
    button3.photo = photo3
    button3.pack(side='left', padx=20, pady=110)
    root.withdraw()
root = tk.Tk()
root.title('ПОЗДРАВЛЕНИЕ!!!')
root.geometry('800x600')
root['background']='#F48FB1'
image = Image.open("vboy.png")
photo = ImageTk.PhotoImage(image)
button = tk.Button(root, image=photo, command=вбой)
button.pack(pady=200)
root.mainloop()
