# -*- coding: cp1251 -*-
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import os
import json

STUDENTS_DIR = "students_profiles"

def ensure_students_dir():
    if not os.path.exists(STUDENTS_DIR):
        os.makedirs(STUDENTS_DIR)

def load_students():
    students = {}
    ensure_students_dir()
    for filename in os.listdir(STUDENTS_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(STUDENTS_DIR, filename), "r", encoding="cp1251") as file:
                student = json.load(file)
                students[student["login"]] = student
    return students

def save_student(student):
    with open(os.path.join(STUDENTS_DIR, f"{student['number']}_{student['login']}.json"), "w", encoding="cp1251") as file:
        json.dump(student, file, ensure_ascii=False, indent=4)

def get_next_student_number():
    ensure_students_dir()
    max_number = 0
    for filename in os.listdir(STUDENTS_DIR):
        if filename.endswith(".json"):
            number = int(filename.split('_')[0])
            max_number = max(max_number, number)
    return max_number + 1

def login():
    login = login_entry.get()
    password = password_entry.get()
    if login in students and students[login]["password"] == password:
        show_profile(login)
    else:
        messagebox.showerror("Ошибка", "Неправильный логин или пароль")

def register():
    login = login_entry.get()
    password = password_entry.get()
    if len(password) < 8:
        messagebox.showerror("Ошибка", "Пароль должен содержать не менее 8 символов")
        return

    if login in students:
        messagebox.showerror("Ошибка", "Логин уже существует")
    else:
        number = str(get_next_student_number())
        students[login] = {
            "number": number,
            "login": login,
            "password": password,
            "full_name": "",
            "dob": "",
            "address": "",
            "phone": "",
            "email": "",
            "parent_phone": "",
            "criminal_record": "Нет",
            "educational_org": "",
            "info": "",
            "photo_path": ""
        }
        save_student(students[login])
        messagebox.showinfo("Успех", "Регистрация прошла успешно")
        show_login_window()

def update_info(login):
    students[login]["full_name"] = full_name_entry.get()
    students[login]["dob"] = dob_entry.get()
    students[login]["address"] = address_entry.get()
    students[login]["phone"] = phone_entry.get()
    students[login]["email"] = email_entry.get()
    students[login]["parent_phone"] = parent_phone_entry.get()
    students[login]["criminal_record"] = criminal_record_var.get()
    students[login]["educational_org"] = educational_org_entry.get()
    students[login]["info"] = info_entry.get()
    save_student(students[login])
    messagebox.showinfo("Успех", "Информация сохранена")
    reset_form()
    show_profile(login)

def choose_photo(login):
    photo_path = filedialog.askopenfilename(title="Выберите фото", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if photo_path:
        students[login]["photo_path"] = photo_path
        save_student(students[login])
        show_profile(login)

def load_image(file_path):
    img = Image.open(file_path)
    img = img.resize((100, 100), Image.Resampling.LANCZOS)
    photo_image = ImageTk.PhotoImage(img)
    return photo_image

def show_profile(login):
    for widget in root.winfo_children():
        widget.destroy()

    student = students[login]
    tk.Label(root, text=f"Профиль студента {login}", font=("Arial", 16)).place(x=320, y=10)
    tk.Label(root, text=f"Номер: {student['number']}", font=("Arial", 12)).place(x=20, y=50)

    if student["photo_path"]:
        photo_image = load_image(student["photo_path"])
        panel = tk.Label(root, image=photo_image)
        panel.image = photo_image
        panel.place(x=20, y=80)
    else:
        tk.Label(root, text="Изображение не найдено.", font=("Arial", 12)).place(x=20, y=80)

    y_offset = 200
    fields = [("ФИО", "full_name"), ("Дата рождения", "dob"), ("Адрес", "address"),
              ("Телефон", "phone"), ("Email", "email"), ("Телефон родителей", "parent_phone"),
              ("Образовательная организация", "educational_org"), ("Информация", "info")]

    global full_name_entry, dob_entry, address_entry, phone_entry, email_entry, parent_phone_entry, educational_org_entry, info_entry, criminal_record_var

    entry_widgets = {}
    for label_text, field_name in fields:
        tk.Label(root, text=label_text, font=("Arial", 12)).place(x=20, y=y_offset)
        entry = tk.Entry(root, width=40)
        entry.insert(0, student[field_name])
        entry.place(x=250, y=y_offset)
        entry_widgets[field_name] = entry
        y_offset += 40

    full_name_entry = entry_widgets["full_name"]
    dob_entry = entry_widgets["dob"]
    address_entry = entry_widgets["address"]
    phone_entry = entry_widgets["phone"]
    email_entry = entry_widgets["email"]
    parent_phone_entry = entry_widgets["parent_phone"]
    educational_org_entry = entry_widgets["educational_org"]
    info_entry = entry_widgets["info"]

    tk.Label(root, text="Наличие судимостей", font=("Arial", 12)).place(x=20, y=y_offset)
    criminal_record_var = tk.StringVar(value=student["criminal_record"])
    tk.Radiobutton(root, text="Да", variable=criminal_record_var, value="Да").place(x=250, y=y_offset)
    tk.Radiobutton(root, text="Нет", variable=criminal_record_var, value="Нет").place(x=300, y=y_offset)
    y_offset += 40

    tk.Button(root, text="Сохранить информацию", command=lambda: update_info(login)).place(x=20, y=y_offset)
    tk.Button(root, text="Выбрать фото", command=lambda: choose_photo(login)).place(x=250, y=y_offset)
    tk.Button(root, text="Выход", command=show_login_window).place(x=450, y=y_offset)

def reset_form():
    full_name_entry.delete(0, tk.END)
    dob_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    parent_phone_entry.delete(0, tk.END)
    educational_org_entry.delete(0, tk.END)
    info_entry.delete(0, tk.END)
    criminal_record_var.set("Нет")

def show_login_window():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Личное Дело Студентов", font=("Arial", 16)).place(x=300, y=50)

    global login_entry, password_entry, show_password_var
    tk.Label(root, text="Логин", font=("Arial", 12)).place(x=250, y=150)
    login_entry = tk.Entry(root)
    login_entry.place(x=350, y=150)

    tk.Label(root, text="Пароль", font=("Arial", 12)).place(x=250, y=200)
    password_entry = tk.Entry(root, show="*")
    password_entry.place(x=350, y=200)

    show_password_var = tk.IntVar()
    show_password_check = tk.Checkbutton(root, text="Показать пароль", variable=show_password_var, command=toggle_password)
    show_password_check.place(x=350, y=230)

    tk.Button(root, text="Вход", command=login).place(x=350, y=270)
    tk.Button(root, text="Регистрация", command=show_register_window).place(x=400, y=270)

def toggle_password():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

def show_register_window():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Регистрация нового студента", font=("Arial", 16)).place(x=270, y=50)

    global login_entry, password_entry, show_password_var
    tk.Label(root, text="Логин", font=("Arial", 12)).place(x=250, y=150)
    login_entry = tk.Entry(root)
    login_entry.place(x=350, y=150)

    tk.Label(root, text="Пароль", font=("Arial", 12)).place(x=250, y=200)
    password_entry = tk.Entry(root, show="*")
    password_entry.place(x=350, y=200)

    show_password_var = tk.IntVar()
    show_password_check = tk.Checkbutton(root, text="Показать пароль", variable=show_password_var, command=toggle_password)
    show_password_check.place(x=350, y=230)

    tk.Button(root, text="Зарегистрироваться", command=register).place(x=350, y=270)
    tk.Button(root, text="Назад", command=show_login_window).place(x=450, y=270)

root = tk.Tk()
root.title("Личное Дело Студентов")
root.geometry("800x600")
students = load_students()
show_login_window()
root.mainloop()
