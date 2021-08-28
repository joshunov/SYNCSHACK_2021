import random
quiz = {
    1 : {"question" : "What does 'www' stand for?",
    "answer" : "worldwideweb"},
    2 : {"question" : "What shape is a stop sign",
    "answer" : 'octagon'},
    3 : {"question" : "Which country is responsible for creating the Olympic Games",
    "answer" : 'greece'},
    4 : {"question" : "Who created Sherlock Holmes?",
    "answer" : 'sirarthurconandoyle'},
    5 : {"question" : "What is the loudest animal on Earth?",
    "answer" : 'spermwhale'},
    6 : {"question" : "How many legs does a spider have?",
    "answer" : '8'},
    7 : {"question" : "How many hearts does an octopus have?",
    "answer" : "3"},
    8 : {"question" : "What the the most compact arrangement of atoms called?",
    "answer" : "solid"},
    9 : {"question" : "What is the nearest planet to the sun?",
    "answer" : "mercury"}
}

question_nums = []
selected_questions = []

for i in range(len(quiz)):
    question_nums.append(i+1)

selected_questions = random.sample(question_nums, 5)
# print(selected_questions)

print()
intro_msg = '''For all text related answers, please enter in lowercase, without spaces. 
For all numeric answers, please enter in digits form.
Enjoy your game and remember to drink responsibly.'''

score = 0

print(intro_msg)

print()
print()
# game_status = 0
# if game_status != 'y':
#     game_status = str(input('Would you like to begin the game (y/n)?'))
#     # if game_status == 'y':
        
        

"Incorrect, answer you have no more attempts. You're halfway to another drink"
for i in selected_questions:
    attempts = 2
    print(quiz[i]["question"])
    answer = str(input("Enter Answer: "))
    if answer == quiz[i]["answer"]:
        score += 1
        print()
        print(f"Correct Answer! You're score is now {score}")
        print('Next Question')
        print()
    else:
        attempts -= 1
        
        if attempts == 1:
            print()
            print(f"Incorrect, answer you have no more attempts. You're halfway to another drink!")
            # players[i].drink # here the player must drink after each question they get wrong (after two attempts)
            print(quiz[i]["question"])
            answer_2 = str(input("Have another go: "))
            if answer_2 == quiz[i]["answer"]:
                score += 1
                print(f"Correct Answer! You're score is now {score}")
            else:
                print(f"Incorrect, you have run out of attempts. You're score is {score}... Pitiful really. Drink up champ!")
            print()
            print('Next Question')
            print()

        elif attempts == 0:
            print(f"Incorrect, you have run out of attempts. You're score is {score}... Pitiful really. Drink up champ!")
                # players[i].drink()
            print('Next Question')
            print()

output_msg = (f"You've performed adequately. You're score is {score}!")
print(output_msg)
# print(quiz)


# for question in quiz:
#     attempts = 3
#     while attempts > 0: 
#         print(quiz[question]['question']) # this will print the current interation of for loop
#         answer = str(input("Enter Answer: "))
#         if answer = quiz[question["answer"]]:
#             score += 1
#             break
#         else:
#             attempts -= 1 
