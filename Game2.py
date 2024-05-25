import tkinter as tk
from tkinter import messagebox

# Initialize the game board
board = [' ' for _ in range(9)]

# Create the main application window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Define player turn and buttons
current_player = 'X'
buttons = []

def reset_board():
    global board, current_player
    board = [' ' for _ in range(9)]
    current_player = 'X'
    for button in buttons:
        button.config(text=' ', state=tk.NORMAL)

def check_victory(icon):
    return (
        (board[0] == icon and board[1] == icon and board[2] == icon) or
        (board[3] == icon and board[4] == icon and board[5] == icon) or
        (board[6] == icon and board[7] == icon and board[8] == icon) or
        (board[0] == icon and board[3] == icon and board[6] == icon) or
        (board[1] == icon and board[4] == icon and board[7] == icon) or
        (board[2] == icon and board[5] == icon and board[8] == icon) or
        (board[0] == icon and board[4] == icon and board[8] == icon) or
        (board[2] == icon and board[4] == icon and board[6] == icon)
    )

def check_draw():
    return ' ' not in board

def on_button_click(i):
    global current_player

    if board[i] == ' ':
        board[i] = current_player
        buttons[i].config(text=current_player, state=tk.DISABLED)

        if check_victory(current_player):
            messagebox.showinfo("Game Over", f"{current_player} Wins! Congratulations!")
            reset_board()
        elif check_draw():
            messagebox.showinfo("Game Over", "The game is a draw!")
            reset_board()
        else:
            current_player = 'O' if current_player == 'X' else 'X'

# Create buttons and add them to the window
for i in range(9):
    button = tk.Button(root, text=' ', font=('normal', 40), width=5, height=2,
                       command=lambda i=i: on_button_click(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Start the GUI event loop
root.mainloop()
