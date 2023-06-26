def get_valid_input():
    marker = ""
    while True:
        marker = input("Player 1: Do you want to be X or O?").upper()
        if marker in ["X", "O"]:
            return marker

def player_input():
    
    marker = get_valid_input()
        
    if marker == "X":
        return ("X", "0")
    else:
        return ("O", "X")
    
move = player_input()
print(move)