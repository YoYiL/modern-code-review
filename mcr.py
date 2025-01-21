def is_win(game):
    win = False
    # Check rows
    if game[0][0] == game[0][1] == game[0][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[1][0] == game[1][1] == game[1][2] and (game[1][0] == 'X' or game[1][0] == 'O'):
        win = True
    if game[2][0] == game[2][1] == game[2][2] and (game[2][0] == 'X' or game[2][0] == 'O'):
        win = True
    # Check columns
    if game[0][0] == game[1][0] == game[2][0] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][1] == game[1][1] == game[2][1] and (game[0][1] == 'X' or game[0][1] == 'O'):
        win = True
    if game[0][2] == game[1][2] == game[2][2] and (game[0][2] == 'X' or game[0][2] == 'O'):
        win = True
    # Check diagonals
    if game[0][0] == game[1][1] == game[2][2] and (game[0][0] == 'X' or game[0][0] == 'O'):
        win = True
    if game[0][2] == game[1][1] == game[2][0] and (game[0][2] == 'X' or game[0][2] == 'O'):
        win = True
    return win

def is_tie(game):
    for row in game:
        for cell in row:
            if cell == ' ':
                return False
    return True

def print_board(game):
    print("\nCurrent chessboard：")
    print("  1 2 3")
    for i, row in enumerate(game, 1):
        print(f"{i} {' '.join(row)}")
    print()

def is_valid_move(i, j, game):
    if not (0 <= i <= 2 and 0 <= j <= 2):
        return False
    if game[i][j] != ' ':
        return False
    return True
    
def main():
    game = [[' ' for _ in range(3)] for _ in range(3)]  # Tic-tac-toe board
    turn = False  # False for player 1's turn, True for player 2's turn
    
    print("Welcome！")
    print("X = player1")
    print("O = player2")
    print("input：row space cloumn（e.g. 1 2）")
    
    print_board(game)
    
    while True:
        turn = not turn  # Switch turns
        current_player = "player1" if not turn else "player2"
        while True:
            try:
                print(f"{current_player} round")
                i, j = map(int, input("input：row space cloumn: ").split())
                i -= 1  # Convert to 0-based index
                j -= 1
                if is_valid_move(i, j, game):
                    break
                else:
                    print("invalid！")
            except (ValueError, IndexError):
                print("invalid!")
        
        # Make the move
        game[i][j] = 'X' if not turn else 'O'
        print_board(game)
        
        # Check for win
        if is_win(game):
            print(f"Done！{current_player}win！")
            break
            
        # Check for tie
        if is_tie(game):
            print("tie！")
            break

if __name__ == "__main__":
    main()
