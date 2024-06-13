import json
import os
import customtkinter as ctk
import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk
DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "budget_data.json")
class BudgetTrackerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Трекер бюджета")
        self.geometry("300x330")
        self.load_data()
        self.income_button = ctk.CTkButton(self, text="Доходы", command=self.add_income)
        self.income_button.pack(pady=10, padx=20, fill=ctk.BOTH, expand=True)
        self.expense_button = ctk.CTkButton(self, text="Расходы", command=self.add_expense_window)
        self.expense_button.pack(pady=10, padx=20, fill=ctk.BOTH, expand=True)
        self.add_goal_button = ctk.CTkButton(self, text="Добавить цель", command=self.add_goal_window)
        self.add_goal_button.pack(pady=10, padx=20, fill=ctk.BOTH, expand=True)
        self.save_for_goal_button = ctk.CTkButton(self, text="Отложить на цель", command=self.save_for_goal_window)
        self.save_for_goal_button.pack(pady=10, padx=20, fill=ctk.BOTH, expand=True)
        self.view_goals_button = ctk.CTkButton(self, text="Просмотреть цели", command=self.view_goals_window)
        self.view_goals_button.pack(pady=10, padx=20, fill=ctk.BOTH, expand=True)
        self.view_expenses_button = ctk.CTkButton(self, text="Посмотреть расходы", command=self.view_expenses_window)
        self.view_expenses_button.pack(pady=10, padx=20, fill=ctk.BOTH, expand=True)
        self.result_label = ctk.CTkLabel(self, text="Общий бюджет: 0")
        self.result_label.pack(pady=10)

    def load_data(self):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
                self.total_budget = data.get("total_budget", 0)
                self.goals = data.get("goals", [])
                self.expenses = data.get("expenses", {})
        else:
            self.total_budget = 0
            self.goals = []
            self.expenses = {"Продукты": 0, "Транспорт": 0, "Жилье": 0, "Развлечения": 0, "Здоровье": 0, "Прочее": 0}
    def save_data(self):
        data = {
            "total_budget": self.total_budget,
            "goals": self.goals,
            "expenses": self.expenses
        }
        with open(DATA_FILE, "w") as file:
            json.dump(data, file)
    def add_income(self):
        income = simpledialog.askfloat("Доходы", "Введите сумму дохода:")
        if income is not None:
            self.total_budget += income
            self.result_label.configure(text=f"Общий бюджет: {self.total_budget}")
            self.save_data()
    def add_expense_window(self):
        expense_window = ctk.CTk()
        expense_window.title("Добавить расход")
        category_label = ctk.CTkLabel(expense_window, text="Выберите категорию расхода:")
        category_label.grid(row=0, column=0, padx=10, pady=5)
        categories = list(self.expenses.keys())
        category_combobox = ttk.Combobox(expense_window, values=categories)
        category_combobox.grid(row=0, column=1, padx=10, pady=5)
        amount_label = ctk.CTkLabel(expense_window, text="Введите сумму расхода:")
        amount_label.grid(row=1, column=0, padx=10, pady=5)
        amount_entry = ctk.CTkEntry(expense_window)
        amount_entry.grid(row=1, column=1, padx=10, pady=5)

        def add_expense():
            category = category_combobox.get()
            amount = amount_entry.get()
            try:
                amount = float(amount)
                if amount <= self.total_budget:
                    self.total_budget -= amount
                    self.expenses[category] += amount
                    self.result_label.configure(text=f"Общий бюджет: {self.total_budget}")
                    self.save_data()
                    expense_window.destroy()
                else:
                    ctk.CTkMessagebox.showerror("Ошибка", "Сумма расхода не может превышать общий бюджет.")
            except ValueError:
                ctk.CTkMessagebox.showerror("Ошибка", "Пожалуйста, введите числовое значение для суммы расхода.")
        add_button = ctk.CTkButton(expense_window, text="Добавить", command=add_expense)
        add_button.grid(row=2, columnspan=2, padx=10, pady=10)
        expense_window.mainloop()
    def add_goal_window(self):
        goal_window = ctk.CTk()
        goal_window.title("Добавить цель")
        name_label = ctk.CTkLabel(goal_window, text="Название цели:")
        name_label.grid(row=0, column=0, padx=10, pady=5)
        name_entry = ctk.CTkEntry(goal_window)
        name_entry.grid(row=0, column=1, padx=10, pady=5)
        cost_label = ctk.CTkLabel(goal_window, text="Стоимость цели:")
        cost_label.grid(row=1, column=0, padx=10, pady=5)
        cost_entry = ctk.CTkEntry(goal_window)
        cost_entry.grid(row=1, column=1, padx=10, pady=5)

        def add_goal():
            name = name_entry.get()
            cost = cost_entry.get()
            try:
                cost = float(cost)
                goal = {"name": name, "cost": cost, "saved": 0}
                self.goals.append(goal)
                self.save_data()
                goal_window.destroy()
            except ValueError:
                ctk.CTkMessagebox.showerror("Ошибка", "Пожалуйста, введите числовое значение для стоимости цели.")
        add_button = ctk.CTkButton(goal_window, text="Добавить", command=add_goal)
        add_button.grid(row=2, columnspan=2, padx=10, pady=10)
        goal_window.mainloop()
    def save_for_goal_window(self):
        save_for_goal_window = ctk.CTk()
        save_for_goal_window.title("Отложить на цель")
        goal_label = ctk.CTkLabel(save_for_goal_window, text="Выберите цель:")
        goal_label.grid(row=0, column=0, padx=10, pady=5)
        goals_names = [goal["name"] for goal in self.goals]
        goal_combobox = ttk.Combobox(save_for_goal_window, values=goals_names)
        goal_combobox.grid(row=0, column=1, padx=10, pady=5)
        amount_label = ctk.CTkLabel(save_for_goal_window, text="Введите сумму для отложения:")
        amount_label.grid(row=1, column=0, padx=10, pady=5)
        amount_entry = ctk.CTkEntry(save_for_goal_window)
        amount_entry.grid(row=1, column=1, padx=10, pady=5)
        def save_for_goal():
            goal_name = goal_combobox.get()
            amount = amount_entry.get()
            try:
                amount = float(amount)
                for goal in self.goals:
                    if goal["name"] == goal_name:
                        if amount <= self.total_budget:
                            goal["saved"] += amount
                            self.total_budget -= amount
                            self.result_label.configure(text=f"Общий бюджет: {self.total_budget}")
                            self.save_data()
                            ctk.CTkMessagebox.showinfo("Успех", f"Сумма {amount} успешно отложена на цель '{goal_name}'.")
                            save_for_goal_window.destroy()
                            return
                        else:
                            ctk.CTkMessagebox.showerror("Ошибка", "Сумма для отложения превышает общий бюджет.")
                            return
                ctk.CTkMessagebox.showerror("Ошибка", f"Цель '{goal_name}' не найдена.")
            except ValueError:
                ctk.CTkMessagebox.showerror("Ошибка", "Пожалуйста, введите числовое значение для суммы.")
        save_button = ctk.CTkButton(save_for_goal_window, text="Отложить", command=save_for_goal)
        save_button.grid(row=2, columnspan=2, padx=10, pady=10)
        save_for_goal_window.mainloop()
    def view_goals_window(self):
        view_goals_window = ctk.CTk()
        view_goals_window.title("Просмотр целей")
        tree = ttk.Treeview(view_goals_window, columns=("Name", "Cost", "Saved", "Left to Save"))
        tree.heading("#0", text="ID")
        tree.heading("Name", text="Название")
        tree.heading("Cost", text="Стоимость")
        tree.heading("Saved", text="Отложено")
        tree.heading("Left to Save", text="Осталось отложить")
        for i, goal in enumerate(self.goals):
            name = goal["name"]
            cost = goal["cost"]
            saved = goal["saved"]
            left_to_save = max(cost - saved, 0)
            tree.insert("", "end", text=str(i+1), values=(name, cost, saved, left_to_save))
        tree.pack(expand=True, fill="both")
        view_goals_window.mainloop()
    def view_expenses_window(self):
        view_expenses_window = ctk.CTk()
        view_expenses_window.title("Просмотр расходов по категориям")
        tree = ttk.Treeview(view_expenses_window, columns=("Category", "Amount"))
        tree.heading("#0", text="ID")
        tree.heading("Category", text="Категория")
        tree.heading("Amount", text="Сумма")
        for i, (category, amount) in enumerate(self.expenses.items()):
            tree.insert("", "end", text=str(i+1), values=(category, amount))
        tree.pack(expand=True, fill="both")
        view_expenses_window.mainloop()
if __name__ == "__main__":
    app = BudgetTrackerApp()
    app.mainloop()