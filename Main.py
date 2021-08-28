'''from PIL import Image                                                                                
img = Image.open('/Users/joshuanovick/Desktop/Screenshot.png')
img.show() '''

import Horse_racing.horse_racing_2 as horse
import fTheBus_fn as ftb
import trivia1 as triv
import kings_cup as king
import random
import time

def letter_by_letter(string):
    for i in string:
        print(i, end= (''), flush= True)
        time.sleep(0.025)
    return ''
    
class Game:
    def __init__(self):
        self.leaderboard = []
        self.player_list = []
        self.player_num = 0
        self.end = False

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
        print("\t    Position\t\t\t|\t        Name      \t\t|\t     Drinks")
        print("\t\t        \t\t|\t\t              \t\t|\t\t     ")
        for i in range(len(self.leaderboard)):
            print("-----------------------------------------------------------------------------------------------------------")
            print("\t\t        \t\t|\t\t              \t\t|\t\t     ")
            print(f"\t\t{str(i+1) + space*(8-len(str(i+1)))}\t\t|\t\t{self.leaderboard[i].name + space*(14-len(self.leaderboard[i].name))}\t\t\t|\t\t{self.leaderboard[i].score}")
            print("\t\t        \t\t|\t\t              \t\t|\t\t     ")

    def run_ftb(self):
        ftb.fTheBus(self.player_list)
        return
    
    def run_trivia(self):
        triv.start_trivia(self.player_list)
        return

    def run_horse(self):
        horse.horse_racing(self.player_list)
        return

    def run_kings(self):
        king.run_kings(self.player_list)
        return

    def choose_game(self):
        try:
            letter_by_letter("What game would you like to play?\n\n\n\t(1) Kings Cup\n\n\t(2) Trivia\n\n\t(3) Horse racing\n\n\t(4) Ride the bus\n\n(5) Exit the game :(\n\n\t")
            game_num = int(input())
            if game_num not in [1,2,3,4,5]:
                raise TypeError
        except:
            letter_by_letter("Come on, you saw the list enter one of the numbers!")
            letter_by_letter("What game would you like to play?\n\n\n\t(1) Kings Cup\n\n\t(2) Trivia\n\n\t(3) Horse racing\n\n\t(4) Ride the bus\n\n(5) Exit the game :(\n\n\t")
            game_num = input()

        if game_num == 1:
            self.run_kings()
        elif game_num == 2:
            self.run_trivia()
        elif game_num == 3:
            self.run_horse()
        elif game_num == 4:
            self.run_ftb()
        elif game_num == 5:
            self.end == True


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


    def calculate_max_alc(self):
        """
        using formula BAC = alcahol consumed in grams/body weight in grams*r *100

        where r = 0.55 for females and 0.68 for males
        
        """
        if self.gender == "M":
            r = 0.68
        else:
            r = 0.55

        self.max_alcahol = self.max_bac*self.weight*r*10

    def drink(self,num = 1):
        if self.max_alcahol == 0:
            self.calculate_max_alc()

        self.score += num
        # player drinks 10% of their max alcahol every drink, hence never drinking 100% of their max alcahol
        # 10g of alcahol = abt 1 standard drink

        #p = percentage of total alcahol drank in every sip
        
        p = 0.15**num

        self.max_alcahol = self.max_alcahol*(1-p)
        #letter_by_letter(f'wow {self.name} has to drink {self.max_alcahol*p} grams!')

        drink_statement = [
            "Someone's feeling thirsty",
            f"{self.name} drink has got it's eyes on you",
            f"{self.name}. Drink. Now",
            f"RBT means you need a plan B",
            f"Oh you don't feel like anymore, I don't care HAVE A DRINK",
            f"Better in your belly than on the floor mate. Maybe skip this one",
        ]

        random.shuffle(drink_statement)


        if self.score == 3:
            if self.gender == 'M':
                gen = "boy"
            else:
                gen = "girl"        
            letter_by_letter(f"whoa there cow{gen} this is your third drink, dont feel bad if you wanna skip this one or replace it with water :)")
        
        elif self.score > 3:
            letter_by_letter(f"Your doing well {self.name} but this is your {self.score} drink, maybe we should start to slow it down")

        elif self.max_alcahol < 3:
            letter_by_letter(f"wow {self.name}, we can tell your reaching your limit, start thinking about slowing down")
    

        elif self.max_alcahol < 1:
            letter_by_letter(f"hey there {self.name} we've run the numbers and we think youve hit your limit for tonight, lets stick with water for the rest of the night") 
        
        else:
            letter_by_letter(drink_statement[0])

        letter_by_letter(f"Press Enter once you are finished, but dont feel bad if you need to skip this one out :)")
        input()
        print()
        return self.max_alcahol*p
    
    def introduce(self):

        weight_questions = [
        f"If you dont mind me asking {self.name}, approximately how much do you weigh in Kg: ",
        f"Heyo {self.name}, spill the beans, how much do you weigh in Kg? ",
        f"Whats'up {self.name}, Hope your having a good one, let us know your weight in Kg: ",
        f"OK {self.name}, you know the deal, How much do you weigh in Kg: ",
        f"Hello {self.name}, we need to know your weight in kg, promise its for your own benefit :): ",
        f"{self.name} Your looking good tonight, between you and me i recon your gonna win, just tell me your weight in Kg so we can get started: "
        ]

        sex_questions = [
        f"Nice {self.name}, now Please enter your bilogical sex: ",
        f"Very interesting, Now lets hear your biological sex: ",
        f"You weigh whatttt? Just kidding. One more thing, we need to know your biological sex please: ",
        f"Hey {self.name} we need your biological sex, we promise we wont tell anyone: "
        ]

        random.shuffle(sex_questions)
        random.shuffle(weight_questions)
        
        try:
            letter_by_letter(weight_questions[0])
            self.weight = int(input())
            print("\n")
        except:
            letter_by_letter(f"\nSeriously {self.name}, That is just not a number, Try again\n")
            return False
            

        try:
            letter_by_letter(sex_questions[0])
            self.gender = input("please enter either M or F: ")
            self.gender = self.gender.upper()
            assert self.gender in ["M","F"]
            return True
        except:
            print(f"\nCome on either M or F, enter either M or F, dont make me angry")
            return False




#Below is a draft of how the game_begin function will be structured:
def game_begin():
    game1 = Game()

    letter_by_letter("\n\n\n\n\n\n\n\n\n\n\n\t\t\033[92mWelcome to 'Drinky bill' The safe drinking game for people young and old (but not younger than 18 :)) if you want to have a good time, youve come to the right place. This online drinking game takes information about YOU and works out a safe amount for you to drink, making sure everyone has an enjoyable fun time!\n please follow all of the prompts and values exactly as they are specified, and most importantly enjoy!\033[0m\n\n")
    n = int(input("please enter the number of players: "))

#Loop collecting names of every player
    for player in range(n):
        letter_by_letter(f"\nEnter the name of player {player+1}: ")
        curr_name = input()
        curr_name = curr_name.lower().capitalize()
        curr_name =f'\033[1m{curr_name}\033[0m'
        game1.add_person(curr_name)

#loop collecting more info on each player
    letter_by_letter(f"\nLets start with some fun Ice-Breakers, {game1.player_list[0].name} you start!")
    for i in game1.player_list:
        print("\n\n")
        while i.introduce() == False:
            continue
        print(f"\n Thanks {i.name}, lets move on")

   
    print("\n\n\n\n\n")
    game1.print_scoreboard()
    letter_by_letter("Lets get down to business")

    while game1.end == False:
        game1.choose_game()
        letter_by_letter("hope you enjoyed that, lets get moving onto the next one")



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
