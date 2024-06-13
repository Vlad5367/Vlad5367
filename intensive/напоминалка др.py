import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
class BirthdayReminderApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Напоминалка о Днях Рождения")
        self.geometry("400x350")
        self.friends_birthdays = {}
        self.load_friends_birthdays()
        self.reminders_label = ctk.CTkLabel(self, text="Сегодня поздравляем:", font=("Arial", 12))
        self.reminders_label.pack(pady=5)
        self.reminders_text = ctk.CTkTextbox(self, wrap=ctk.WORD, font=("Arial", 12), height=5)
        self.reminders_text.pack(pady=5, fill=ctk.BOTH, expand=True)
        self.check_birthdays_today()
        self.add_friend_label = ctk.CTkLabel(self, text="Добавить друга:", font=("Arial", 12))
        self.add_friend_label.pack(pady=5)
        self.friend_name_entry = ctk.CTkEntry(self)
        self.friend_name_entry.pack(pady=5)
        self.friend_birthday_entry = ctk.CTkEntry(self)
        self.friend_birthday_entry.pack(pady=5)
        self.add_friend_button = ctk.CTkButton(self, text="Добавить друга", command=self.add_friend)
        self.add_friend_button.pack(pady=5)
        self.view_friends_button = ctk.CTkButton(self, text="Посмотреть список друзей", command=self.view_friends)
        self.view_friends_button.pack(pady=5)

    def check_birthdays_today(self):
        today = datetime.today().strftime('%d.%m.%Y')

        birthdays_today = [name for name, birthday in self.friends_birthdays.items() if birthday == today]

        if birthdays_today:
            reminders_text = "\n".join(birthdays_today)
            self.reminders_text.insert(ctk.END, reminders_text)
        else:
            self.reminders_text.insert(ctk.END, "Сегодня ни у кого нет дня рождения!")

    def add_friend(self):
        name = self.friend_name_entry.get()
        birthday = self.friend_birthday_entry.get()

        if not name or not birthday:
            messagebox.showwarning("Предупреждение", "Введите имя друга и его день рождения")
            return

        self.friends_birthdays[name] = birthday
        self.friend_name_entry.delete(0, ctk.END)
        self.friend_birthday_entry.delete(0, ctk.END)
        self.save_friends_birthdays()
        self.update_reminders()
    def update_reminders(self):
        self.reminders_text.delete(1.0, ctk.END)
        self.check_birthdays_today()
    def view_friends(self):
        friends_list = "\n".join([f"{name}: {birthday}" for name, birthday in self.friends_birthdays.items()])
        messagebox.showinfo("Список друзей", friends_list)

    def save_friends_birthdays(self):
        with open("friends_birthdays.txt", "w") as f:
            for name, birthday in self.friends_birthdays.items():
                f.write(f"{name}:{birthday}\n")

    def load_friends_birthdays(self):
        try:
            with open("friends_birthdays.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    name, birthday = line.strip().split(":")
                    self.friends_birthdays[name] = birthday
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    app = BirthdayReminderApp()
    app.mainloop()
