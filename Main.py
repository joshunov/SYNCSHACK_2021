'''from PIL import Image                                                                                
img = Image.open('/Users/joshuanovick/Desktop/Screenshot.png')
img.show() '''

import Horse_racing.horse_racing_2 as horse

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

    def print_scoreboard(self):

        scores = []

        for players in self.player_list:
            scores.append(players.score)
        scores = sorted(scores, reverse=True)

        for score in scores:
            for player in self.player_list:
                if player.score == score and player not in self.leaderboard:
                    self.leaderboard.append(player)
                    break
            continue

        print("Alright, lets see how these scores are looking!")
        space = " "

        print("\t\t        \t\t|\t\t              \t\t|\t\t     ")
        print("\t    Position\t\t\t|\t        Name      \t\t|\t     Score")
        print("\t\t        \t\t|\t\t              \t\t|\t\t     ")
        for i in range(len(self.leaderboard)):
            print("-----------------------------------------------------------------------------------------------------------")
            print("\t\t        \t\t|\t\t              \t\t|\t\t     ")
            print(f"\t\t{str(i+1) + space*(8-len(str(i+1)))}\t\t|\t\t{self.leaderboard[i].name + space*(14-len(self.leaderboard[i].name))}\t\t|\t\t{self.leaderboard[i].score}")
            print("\t\t        \t\t|\t\t              \t\t|\t\t     ")

class Player:
    def __init__(self):
        self.name = " "
        self.weight = 0
        self.max_bac = 0.05 #<-- determines how drunk ppl will get 0.03-0.05 for safe driving, 0.06-0.1 for impared balance/word slurring, 0.11+ nausea, blurred vision etc
        self.max_alcahol = 0.0 #maximum amount of alcahol can be drunk to stay under the max BAC in grams
        self.gender = " " # M or F Biological Sex
        self.score = 0
        self.is_host = False
    
        #attributes for horse_racing
        self.bet = 0
        self.suit = ""


    """
    To Complete:
    Drink() DONE
    Introduce() DONE

    """
    # def

    def drink(self):
        #functoin has no input, but outputs the amount of alcahol in grams that should be drunk
        """
        using formula BAC = alcahol consumed in grams/body weight in grams*r *100

        where r = 0.55 for females and 0.68 for males
        
        """
        if self.gender == "M":
            r = 0.68
        else:
            r = 0.55

        self.max_alcahol = self.max_bac*self.weight*r*10

        # player drinks 10% of their max alcahol every drink, hence never drinking 100% of their max alcahol
        # 10g of alcahol = abt 1 standard drink

        #p = percentage of total alcahol drank in every sip
        p = 0.25

        self.max_alcahol = self.max_alcahol*(1-p)
        print(f'wow {self.name} has to drink {self.max_alcahol*p} grams!')

        #STILL TO DO convert alcahol amounts into 'sip's'
        return self.max_alcahol*p
    
    def introduce(self):
        weight_questions = [
        f"If you dont mind me asking {self.name}, approximately how much do you weigh in Kg: ",
        f"Heyo {self.name}, spill the beans, how much do you weigh?",
        f"Whats'up {self.name}, Hope your having a good one, let us know your weight",
        f"OK {self.name}, you know the deal, How much do you weigh",
        f"Hello {self.name}, we need to know your weight, promise its for your own benefit :)",
        f"{self.name} Your looking good tonight, between you and me i recon your gonna win, just tell me your weight so we can get started"
        ]

        sex_questions = [
        f"Nice {self.name}, now Please enter your bilogical sex, please enter either M or F: ",
        f"Very interesting, Now lets hear your biological sex",
        f"You weigh whatttt? Just kidding. One more thing, we need to know your biological sex please",
        f"",
        f"",
        f"",
        f"",
        ]




        random.shuffle(weight_questions)

        try:
            self.weight = int(input(f"If you dont mind me asking {self.name}, approximately how much do you weigh in Kg: "))
        except:
            print(f"\nSeriously {self.name}, That is just not a number, Try again")
            return False

        try:
            print(sex_questions[0])
            self.gender = input("please enter either M or F: ")
            assert self.gender in ["M","F"]
            return True
        except:
            print(f"\nCome on either M or F, enter either M or F, dont make me angry")
            return False




#Below is a draft of how the game_begin function will be structured:
def game_begin():
    game1 = Game()

    print("\n\n\t\tsome long involved but funny rulebook/welcome message\n\n")
    n = int(input("please enter the number of players: "))

#Loop collecting names of every player
    for player in range(n):
        curr_name = input(f"\nEnter the name of player {player+1}: ")
        curr_name = curr_name.lower().capitalize()
        game1.add_person(curr_name)

#loop collecting more info on each player
    print(f"\nLets start with some fun Ice-Breakers, {game1.player_list[0].name} you start!")
    for i in game1.player_list:
        print("\n\n")
        while i.introduce() == False:
            continue
        print(f"\n Thanks {i.name}, lets move on")

    #run horse game
    horse.horse_racing(game1.player_list)






game_begin()







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