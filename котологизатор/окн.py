#В tkinter расположение окна задается с помощью метода geometry().
#Например, чтобы разместить окно по центру экрана с шириной 800 пикселей и высотой 600 пикселей, нужно выполнить следующий код:
import tkinter as tk

root = tk.Tk()
root.geometry("800x600+{}+{}".format(root.winfo_screenwidth()//2 - 400, root.winfo_screenheight()//2 - 300))
import tkinter as tk

root.mainloop()
root.mainloop()
#Здесь "800x600" - это ширина и высота окна, "root.winfo_screenwidth()//2 - 400" и "root.winfo_screenheight()//2 - 300" -
#координаты левого верхнего угла окна по центру экрана.
