# Write your solution here
##here we have use input for row and column. we need to check whether the values are valid or not. If not
##return False then check for whether the gameboard is empty or not if empty place that replace that empty 
##element by the piece and then return true and then return the list and atlast return False if element is
##not empty
def play_turn(game_board: list, x: int, y: int, piece: str):
    if (x <0 or x >=3) or (y <0 or y>=3):
        return False
    elif game_board[y][x] == "" :
        game_board[y][x] = piece
        return True
    else:
        return False




if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 0, 0, "X"))
    print(game_board)