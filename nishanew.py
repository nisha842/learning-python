def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


test_board = ['#', 'x', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'x']
display_board(test_board)


def player_input() :
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
value=player_input()
print(value)

def place_marker(board, marker, position):
    board[position] = marker
place_marker(test_board,'€',8)
display_board(test_board)


