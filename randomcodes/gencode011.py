import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("300x300")

        self.board = [" " for i in range(9)]
        self.player = "X"
        self.result = " "

        self.buttons = []
        for i in range(9):
            button = tk.Button(self.window, width=10, height=5, font=("Helvetica", 24), command=lambda i=i: self.on_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def on_click(self, index):
        if self.board[index] == " " and self.result == " ":
            self.board[index] = self.player
            self.buttons[index].config(text=self.player)
            if self.is_victory(self.player):
                self.result = "Victory"
                self.label.config(text=f"{self.player} wins!")
            elif " " not in self.board:
                self.result = "Draw"
                self.label.config(text="Draw!")
            else:
                self.player = "O" if self.player == "X" else "X"

    def is_victory(self, icon):
        if (self.board[0] == icon and self.board[1] == icon and self.board[2] == icon) or \
           (self.board[3] == icon and self.board[4] == icon and self.board[5] == icon) or \
           (self.board[6] == icon and self.board[7] == icon and self.board[8] == icon) or \
           (self.board[0] == icon and self.board[3] == icon and self.board[6] == icon) or \
           (self.board[1] == icon and self.board[4] == icon and self.board[7] == icon) or \
           (self.board[2] == icon and self.board[5] == icon and self.board[8] == icon) or \
           (self.board[0] == icon and self.

# Code is not working. In complete generation of code by chatGPT.