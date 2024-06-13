import tkinter as tk
import random
from PIL import Image, ImageTk
def джигурда():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    image = Image.open("i.png")
    for _ in range(1000):
        x = random.randint(0, screen_width - 480)
        y = random.randint(0, screen_height - 315)
        window = tk.Toplevel(root)
        window.title("джигурда")
        window.geometry("480x315+{}+{}".format(x, y))
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(window, image=photo)
        label.image = photo
        label.pack()
root = tk.Tk()
root.title("джигурда")
button = tk.Button(root, text="джигурда", command=джигурда)
button.pack()
root.mainloop()