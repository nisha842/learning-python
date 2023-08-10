class player():
    def __init__(self, name):
        self.name = name
        self.position = 0
        
    def update_positon(self, position):
        self.position = self.position  + position
        # if self.position is ladder postion
            # self.position = ladder[self.position]
        # if self.position is snake postion
            # self.position = snake[self.position]

# initialize players
player_1 = player('Nisha') # similar to a = {}
# name: Nisha, positon: 0
player_2 = player('Isha')
# name: Shishir, positon: 0

# roll_dice player 1
# . is an access operator for methods
dice = 5
player_1.update_positon(position=dice)


# roll_dice player 2
dice = 3
player_2.update_positon(position=dice)

# roll_dice player 1
dice = 2
player_1.update_positon(position=dice)

# roll_dice player 2
dice= 3
player_2.update_positon(position=dice)

print(player_1.name, player_1.position)
print(player_2.name, player_2.position)

