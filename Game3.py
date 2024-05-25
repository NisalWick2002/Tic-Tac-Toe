import tkinter as tk
from tkinter import messagebox, simpledialog

# Game board for both games
board = [' ' for _ in range(9)]

# Function to reset the board
def reset_board():
    global board, current_player
    board = [' ' for _ in range(9)]
    current_player = 'X'

# Functions for Terminal Game
def print_board():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2
    print('Your turn player {}'.format(number))
    while True:
        choice = input('Enter your move (1-9): ').strip()
        if choice.isdigit() and 1 <= int(choice) <= 9:
            choice = int(choice)
            if board[choice - 1] == ' ':
                board[choice - 1] = icon
                break
            else:
                print('That space is taken! Try again.')
        else:
            print('Invalid input! Please enter a number between 1 and 9.')

def is_victory(icon):
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

def is_draw():
    return ' ' not in board

def terminal_game():
    reset_board()
    while True:
        print_board()
        player_move('X')
        print_board()
        if is_victory('X'):
            print('X Wins! Congratulations!')
            break
        elif is_draw():
            print('The game is a draw!')
            break
        player_move('O')
        print_board()
        if is_victory('O'):
            print('O Wins! Congratulations!')
            break
        elif is_draw():
            print('The game is a draw!')
            break

# GUI Game
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
            update_buttons()
        elif check_draw():
            messagebox.showinfo("Game Over", "The game is a draw!")
            reset_board()
            update_buttons()
        else:
            current_player = 'O' if current_player == 'X' else 'X'

def update_buttons():
    for i in range(9):
        buttons[i].config(text=board[i], state=tk.NORMAL if board[i] == ' ' else tk.DISABLED)

def gui_game(theme):
    global root, buttons, current_player
    reset_board()
    root = tk.Tk()
    root.title("Tic-Tac-Toe")

    current_player = 'X'
    buttons = []

    # Theme colors
    if theme == 'dark':
        bg_color = '#333333'
        fg_color = '#FFFFFF'
    else:
        bg_color = '#FFFFFF'
        fg_color = '#000000'

    for i in range(9):
        button = tk.Button(root, text=' ', font=('normal', 40), width=5, height=2,
                           command=lambda i=i: on_button_click(i), bg=bg_color, fg=fg_color)
        button.grid(row=i//3, column=i%3)
        buttons.append(button)

    root.mainloop()

# Main menu for selecting game mode and theme
def main_menu():
    choice = simpledialog.askstring("Game Selection", "Type 'terminal' to play in terminal or 'gui' to play in GUI:")

    if choice and choice.lower() == 'terminal':
        terminal_game()
    elif choice and choice.lower() == 'gui':
        theme = simpledialog.askstring("Theme Selection", "Type 'dark' for dark mode or 'light' for light mode:")
        if theme and theme.lower() in ['dark', 'light']:
            gui_game(theme.lower())
        else:
            messagebox.showinfo("Invalid Theme", "Please restart and choose a valid theme.")
    else:
        messagebox.showinfo("Invalid Choice", "Please restart and choose a valid option.")

# Create main application window for the menu
root = tk.Tk()
root.withdraw()  # Hide the root window as we don't need it here
main_menu()
root.mainloop()
