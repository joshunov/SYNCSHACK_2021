'''from PIL import Image                                                                                
img = Image.open('/Users/joshuanovick/Desktop/Screenshot.png')
img.show() '''

#each game chooses how drinks are dished out, every game has an output 

import random

    
class Game:
    def __init__(self):
        self.leaderboard = []
        self.player_list = []
        self.player_num = 0

        #include more game info...
    def add_person(self,name):
        #Creating the object of 10 players to be assigned to each person playing the game, capping the maximum number of players at 10 but can be extended

        p1,p2,p3,p4,p5,p6,p7,p8,p9,p10 = Player(),Player(),Player(),Player(),Player(),Player(),Player(),Player(),Player(),Player()
        player_positions = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]

        for positions in player_positions:
            if positions.name == " ":
                positions.name = name
                self.player_list.append(positions)
                break
            else:
                continue

        self.player_num += 1
        name = Player()
        name.name = name

    def create_player_list(self):
        #FINISH
        return

class Player:
    def __init__(self):
        self.name = " "
        self.weight = 0
        self.bac = 0
        self.gender = " " # M or F SAY BIOLOGICAL SEXXX
        self.score = 0
        self.is_host = False
    
    def drink(self):
        #FINISH
        return
    
    def introduce(self,):
        print(f"Lets start with some fun Ice-Breakers, {p1.name} you start!"
        try:
            self.weight = int(input("\n\nIf you dont mind me asking, approximately how much do you weigh in Kg: "
            if self.weight <
         #FINISH
        except:

        return

#EVERY GAME FO MUST HAVE STANDARD OUTPUT/INPUT
#Input will be

#n = number of players insert later



#Below is a draft of how the game_begin function will be structured:
game1 = Game()

print("\n\n\t\tsome long involved but funny rulebook/welcome message\n\n")
n = int(input("please enter the number of players: "))

for player in range(n):
    curr_name = input(f"\n\tEnter the name of player {player+1}")
    game1.add_person(curr_name)

for i in game1.player_list:
    i.introduce()

















#sample game function:

'''
def game_sample(players: Game.player_list):
    #players will be a list from the Game class looking like [p1,p2,p3,...,pn] with each element of the list having all the player attributes
    #this list will be the standard input of each game function.


    #say player 3 has to drink
    players[2].drink()

    #or you want player 1's name
    players[2].name

    #if player 4 gets a point
    players[3].score += 1

    #also each player will have an is_host attribute incase your game needs that, say player 1 is the host, players[0].is_host == True

    #functions dont really need to return anything, just rater update each players attributes along the way
    return
'''