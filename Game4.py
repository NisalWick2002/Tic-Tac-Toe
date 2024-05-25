import tkinter as tk
from tkinter import messagebox, simpledialog

# Dictionary to store player names and symbols
players = {}

# Function to reset the board
def reset_board():
    global board
    board = [' ' for _ in range(board_size * board_size)]

# GUI Game
def check_victory(icon):
    # Check rows, columns, and diagonals for victory
    for i in range(board_size):
        if all(board[j] == icon for j in range(i * board_size, (i + 1) * board_size)):
            return True
        if all(board[j] == icon for j in range(i, len(board), board_size)):
            return True
    # Check diagonals
    if all(board[i] == icon for i in range(0, len(board), board_size + 1)):
        return True
    if all(board[i] == icon for i in range(board_size - 1, len(board) - 1, board_size - 1)):
        return True
    
    # Check for custom winning condition
    for i in range(len(board)):
        # Check rows
        if i % board_size <= board_size - win_condition:
            if all(board[i + j] == icon for j in range(win_condition)):
                return True
        # Check columns
        if i // board_size <= board_size - win_condition:
            if all(board[i + j * board_size] == icon for j in range(win_condition)):
                return True
        # Check diagonals
        if i % board_size <= board_size - win_condition and i // board_size <= board_size - win_condition:
            if all(board[i + j * (board_size + 1)] == icon for j in range(win_condition)):
                return True
            if all(board[i + j * (board_size - 1)] == icon for j in range(win_condition)):
                return True
    return False

def check_draw():
    return ' ' not in board

def on_button_click(i):
    global current_player

    if board[i] == ' ':
        board[i] = current_player
        buttons[i].config(text=current_player, state=tk.DISABLED)

        if check_victory(current_player):
            messagebox.showinfo("Game Over", f"{players[current_player]} Wins! Congratulations!")
            reset_board()
            update_buttons()
        elif check_draw():
            messagebox.showinfo("Game Over", "The game is a draw!")
            reset_board()
            update_buttons()
        else:
            current_player = player_order[(player_order.index(current_player) + 1) % len(player_order)]

def update_buttons():
    for i in range(board_size * board_size):
        buttons[i].config(text=board[i], state=tk.NORMAL if board[i] == ' ' else tk.DISABLED)

def setup_players():
    global players, board_size, current_player, player_order, win_condition
    # Ask the user how many players will be playing
    num_players = simpledialog.askinteger("Number of Players", "How many players will be playing?")
    if num_players is None or num_players < 2:
        messagebox.showerror("Error", "At least 2 players are required to play the game.")
        return

    # Assign names and symbols to players
    for i in range(num_players):
        name = simpledialog.askstring("Player Name", f"Enter name for Player {i+1}:")
        symbol = simpledialog.askstring("Player Symbol", f"Enter symbol for {name}:")
        players[symbol] = name

    # Determine board size based on the number of players
    board_size = num_players * 3

    # Ask for the winning condition
    win_condition = simpledialog.askinteger("Winning Condition", "How many symbols are required to win?")
    if win_condition is None or win_condition < 3 or win_condition > board_size:
        messagebox.showerror("Error", f"Winning condition must be between 3 and {board_size}.")
        return

    # Set current player and player order
    player_order = list(players.keys())
    current_player = player_order[0]

    gui_game()

def gui_game():
    global root, buttons
    reset_board()
    root = tk.Tk()
    root.title("Tic-Tac-Toe")

    buttons = []

    for i in range(board_size * board_size):
        button = tk.Button(root, text=' ', font=('normal', 40), width=5, height=2,
                           command=lambda i=i: on_button_click(i))
        button.grid(row=i // board_size, column=i % board_size)
        buttons.append(button)

    root.mainloop()

# Setup players and start the game
setup_players()
