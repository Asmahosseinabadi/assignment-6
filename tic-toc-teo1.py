import pyfiglet
from colorama import Fore, Style
import time

def show():
    for row in game_board:
        for cell in row:
            if cell == "X":
                print(Fore.RED + cell + Style.RESET_ALL, end=" ")
            elif cell == "O":
                print(Fore.BLUE + cell + Style.RESET_ALL, end=" ")
            else:
                print(cell, end=" ")
        print()

# def show():
#     for row in game_board:
#         for cell in row:
#             print(cell, end=" ")
#         print()
def check_win():
    # Check rows
    for row in game_board:
        if row.count(row[0]) == len(row) and row[0] != "-":
            return row[0]

    # Check columns
    for col in range(len(game_board)):
        check = []
        for row in game_board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != "-":
            return check[0]

    # Check diagonals
    if game_board[0][0] == game_board[1][1] == game_board[2][2] != "-":
        return game_board[0][0]
    if game_board[0][2] == game_board[1][1] == game_board[2][0] != "-":
        return game_board[0][2]

    if "-" not in [cell for row in game_board for cell in row]:
        return "again"

    return None


title = pyfiglet.figlet_format("Tic Toc Teo",font="slant")
print(title)

game_board=[["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]]

show()

start_time = time.time()

while True:
    print("player 1:")

    while True:
        row=int(input("row= "))
        col=int(input("col= "))

        if 0<=row and row<=2 and 0<=col and col<=2:
            if game_board[row][col]=="-":
                game_board[row][col]="X"
                break
            else:
                print("this place is already taken!!!!!")
        else:
            print("OpSsss! the range of number should be between 0 and 2!")
        check_win()

    show()
    check_win()

    print("player2:")
    while True:
        row=int(input("row= "))
        col=int(input("col= "))
        if 0<=row and row<=2 and 0<=col and col<=2:
            if game_board[row][col]=="-":
                game_board[row][col]="O"
                break
            else:
                print("this place is already taken!!!!!")
        else:
            print("OpSsss! the range of number should be between 0 and 2!")
        check_win()



    show()
    check_win()
end_time = time.time()

elapsed_time = end_time - start_time

print(f"\nTime spent on the game: {elapsed_time:.2f} seconds")
