import tkinter as tk
from tkinter import messagebox
import random

class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku")
        self.board = [[0]*9 for _ in range(9)]
        self.create_widgets()
        self.generate_board()
        self.display_board()

    def create_widgets(self):
        self.cells = [[None]*9 for _ in range(9)]
        self.block_frames = [[None]*3 for _ in range(3)]  # Frames for blocks
        for i in range(9):
            for j in range(9):
                block_row, block_col = i // 3, j // 3
                if not self.block_frames[block_row][block_col]:
                    self.block_frames[block_row][block_col] = tk.Frame(self.master, bg="black", bd=2)  # Increase border thickness
                    self.block_frames[block_row][block_col].grid(row=block_row * 3, column=block_col * 3, rowspan=3, columnspan=3, sticky="nsew")

                cell_frame = tk.Frame(self.block_frames[block_row][block_col], bg="white", bd=1)
                cell_frame.grid(row=i % 3, column=j % 3)
                self.cells[i][j] = tk.Entry(cell_frame, width=2, font=('Arial', 20), justify='center')
                self.cells[i][j].pack(fill='both', expand=True)

        self.solve_button = tk.Button(self.master, text="Solve", command=self.solve_and_check)
        self.solve_button.grid(row=9, column=4, columnspan=2, pady=10)

    def generate_board(self):
        # Generate a completed Sudoku board
        self.solve_board()
        # Remove numbers randomly to create a puzzle
        for _ in range(50):
            row, col = random.randint(0, 8), random.randint(0, 8)
            self.board[row][col] = 0

    def solve_board(self):
        # Solve the Sudoku puzzle using backtracking algorithm
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True
        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid_move(row, col, num):
                self.board[row][col] = num
                if self.solve_board():
                    return True
                self.board[row][col] = 0
        return False

    def find_empty_cell(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def display_board(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    self.cells[i][j].insert(tk.END, str(self.board[i][j]))
                    self.cells[i][j].config(state='disabled', disabledforeground='black', disabledbackground='light grey')
                else:
                    self.cells[i][j].bind('<Key>', lambda event, row=i, col=j: self.on_key_press(event, row, col))

    def on_key_press(self, event, row, col):
        value = event.char
        if value.isdigit():
            if not self.is_valid_move(row, col, int(value)):
                event.widget.delete(0, tk.END)
                event.widget.config(fg='red')
            else:
                event.widget.config(fg='black')

    def is_valid_move(self, row, col, value):
        # Check row
        if value in self.board[row]:
            return False
        # Check column
        if value in [self.board[i][col] for i in range(9)]:
            return False
        # Check 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.board[i][j] == value:
                    return False
        return True

    def solve_and_check(self):
        self.solve_board()
        if self.is_solved_correctly():
            messagebox.showinfo("Sudoku Solver", "Congratulations! You solved the Sudoku puzzle correctly!")
        else:
            messagebox.showinfo("Sudoku Solver", "Sorry, the Sudoku puzzle is not solved correctly. Please try again.")

    def is_solved_correctly(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0 or not self.is_valid_move(i, j, self.board[i][j]):
                    return False
        return True

def main():
    root = tk.Tk()
    SudokuGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()