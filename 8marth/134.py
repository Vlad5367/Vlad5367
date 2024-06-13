import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
def endwindow():
    root5 = tk.Toplevel()
    root5.title('ПОЗДРАВЛЕНИЕ!!!')
    root5.geometry('800x600')
    root5['background'] = '#F48FB1'
    root5.mainloop()

root2 = tk.Tk()
root2.title('ПОЗДРАВЛЕНИЕ!!!')
root2.geometry('1050x700')
root2['background'] = '#F48FB1'
image = Image.open('rr.png')
image = image.resize((image.width // 7, image.height // 7))
photo = ImageTk.PhotoImage(image)
label2 = Label(root2, image=photo)
label2.image = photo
label2.pack(pady = 20)
label = tk.Label(text='Выбери какой ты сегодня цветок.', font=('ROMAN', 25), bg='#F48FB1')
label.pack(pady = 30)
image1 = Image.open('flovers1.png')
image1 = image1.resize((image1.width // 7, image1.height // 7))
photo1 = ImageTk.PhotoImage(image1)
button1 = Button(root2, image=photo1, command=endwindow)
button1.photo = photo1
button1.pack(side='left', padx=30, pady=110)
image2 = Image.open('послолн.png')
image2 = image2.resize((image2.width // 7, image2.height // 7))
photo2 = ImageTk.PhotoImage(image2)
button2 = Button(root2, image=photo2, command=endwindow)
button2.photo = photo2
button2.pack(side='left', padx=20, pady=110)
image3 = Image.open('flovers3.png')
image3 = image3.resize((image3.width // 7, image3.height // 7))
photo3 = ImageTk.PhotoImage(image3)
button3 = Button(root2, image=photo3, command=endwindow)
button3.photo = photo3
button3.pack(side='left', padx=20, pady=110)
root2.mainloop()