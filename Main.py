from PIL import Image                                                                                
img = Image.open('/Users/joshuanovick/Desktop/Screenshot.png')
img.show() 

#each game chooses how drinks are dished out, every game has an output 

class Player:
    def __init__(self):
        self.name = " "
        self.weight = 0
        self.bac = 0
        self.gender = " " # M or F SAY BIOLOGICAL SEXXX
        self.point = 0
    
    def enter_name(self):
        #FINISH
        return
    
    def drink(self):
        #FINISH
        return
    
    def introduce(self,):
         #FINISH
        return
    
class Game:
    def __init__(self, players: Player ):
        self.leaderboard = []
        self.player_list = []
        self.player_num = 0

        #include more game info...
    
    def create_player_list(self):
        #FINISH
        return

game1 = Game()
game1.player_num = int(input("How many players will you have"))
print(game1.player_num)

#EVERY GAME FO MUST HAVE STANDARD OUTPUT/INPUT
#Input will be

#n = number of players insert later
