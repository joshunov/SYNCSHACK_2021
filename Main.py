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
        self.is_host = bool
    
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
    def add_person(self,name):
        self.player_num += 1
        name = Player()
        name.name = name

    def create_player_list(self):
        #FINISH
        return


#EVERY GAME FO MUST HAVE STANDARD OUTPUT/INPUT
#Input will be

#n = number of players insert later



#Below is a draft of how the game_begin function will be structured:
game1 = Game()

print("some long involved but funny rulebook/welcome message")
n = int(input("please enter the number of players"))
Gam

for player in range(n):
    curr_name = input(f"Enter the name of player {player}")
    

