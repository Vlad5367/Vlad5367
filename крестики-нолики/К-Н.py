import tkinter as tk
from tkinter import messagebox

# Создание главного окна
window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("500x400")

# Функция для начала игры
def start_game(symbol):
    # Закрытие приветственного окна
    welcome_window.destroy()

    # Создание игрового поля
    game_frame = tk.Frame(window)
    game_frame.pack(expand=True)

    buttons = [[None for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            button = tk.Button(game_frame, text=' ', padx=30, pady=30, font=('Arial', 20), command=lambda row=i, col=j: make_move(row, col, symbol))
            button.grid(row=i, column=j, sticky="nsew", padx=1, pady=1)
            buttons[i][j] = button

    # Создание игровой логики
    board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(row, col, symbol):
        if board[row][col] == ' ':
            board[row][col] = symbol
            buttons[row][col].config(text=symbol, state=tk.DISABLED)
            if check_win(symbol):
                end_game_message(symbol + " победил!", buttons)
            elif ' ' not in [cell for row in board for cell in row]:
                end_game_message("Ничья!", buttons)
            else:
                next_symbol = 'O' if symbol == 'X' else 'X'
                computer_move(next_symbol)

    def computer_move(symbol):
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = symbol
                    buttons[i][j].config(text=symbol, state=tk.DISABLED)
                    if check_win(symbol):
                        end_game_message(symbol + " победил!", buttons)
                    return

    def check_win(symbol):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == symbol:
                return True
            if board[0][i] == board[1][i] == board[2][i] == symbol:
                return True
        if board[0][0] == board[1][1] == board[2][2] == symbol:
            return True
        if board[0][2] == board[1][1] == board[2][0] == symbol:
            return True
        return False

    def end_game_message(message, buttons):
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(state=tk.DISABLED)
        result = messagebox.askquestion("Результат игры", message + "\nХотите сыграть еще раз?")
        if result == 'yes':
            play_again()
        else:
            window.destroy()

    def play_again():
        reset_board()
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(text=' ', state=tk.NORMAL)

    def reset_board():
        for i in range(3):
            for j in range(3):
                board[i][j] = ' '

# Создание приветственного окна
welcome_window = tk.Frame(window)
welcome_window.pack(expand=True)

welcome_label = tk.Label(welcome_window, text="Добро пожаловать в игру 'Крестики-нолики'!", font=('Arial', 14))
welcome_label.pack(pady=20)

symbol_label = tk.Label(welcome_window, text="Выберите символ:", font=('Arial', 12))
symbol_label.pack()

symbol_frame = tk.Frame(welcome_window)
symbol_frame.pack()

symbol_var = tk.StringVar(value="X")
symbol_button_x = tk.Radiobutton(symbol_frame, text="X", variable=symbol_var, value="X", font=('Arial', 12))
symbol_button_x.pack(side=tk.LEFT)

symbol_button_o = tk.Radiobutton(symbol_frame, text="O", variable=symbol_var, value="O", font=('Arial', 12))
symbol_button_o.pack(side=tk.LEFT)

start_button = tk.Button(welcome_window, text="Начать игру", width=10, height=2, font=('Arial', 12), command=lambda: start_game(symbol_var.get()))
start_button.pack()

# Запуск главного цикла окна
window.mainloop()
