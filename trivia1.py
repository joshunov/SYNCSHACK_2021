import random
import time

def letter_by_letter(string):
    for i in string:
        print(i, end= (''), flush= True)
        time.sleep(0.035)
    return ''
    
def start_trivia(players):
    
    quiz = {
        1 : {"question" : "What does 'www' stand for?",
        "answer" : "WORLD WIDE WEB"},
        2 : {"question" : "What shape is a stop sign",
        "answer" : 'OCTAGON'},
        3 : {"question" : "Which country is responsible for creating the Olympic Games",
        "answer" : 'GREECE'},
        4 : {"question" : "Who created Sherlock Holmes?",
        "answer" : 'SIR ARTHUR CONAN DOYLE'},
        5 : {"question" : "What is the loudest animal on Earth?",
        "answer" : 'SPERM WHALE'},
        6 : {"question" : "How many legs does a spider have?",
        "answer" : '8'},
        7 : {"question" : "How many hearts does an octopus have?",
        "answer" : "3"},
        8 : {"question" : "What the the most compact arrangement of atoms called?",
        "answer" : "SOLID"},
        9 : {"question" : "What is the nearest planet to the sun?",
        "answer" : "MERCURY"},
        10 : {"question" : "Who is the lead in the Hollywood Movie 'Pirates of the Carribean'?",
        "answer" : "CAPTAIN JACK SPARROW"},
        11 : {"question" : "Who was the 44th president of the United States of America?",
        "answer" : "BARRACK OBAMA"},
        12 : {"question" : "Who was the 43rd president of the United States of America?",
        "answer" : "GEORGE W BUSH"},
        13 : {"question" : "What is the national symbolic animal of Scotland?",
        "answer" : "UNICORN"},
        14 : {"question" : "Prior to alcohol, what was used in thermometers?",
        "answer" : "MERCURY"},
        15 : {"question" : "Where does Sirius Black die in Harry Potter: The Order of the Phoenix?",
        "answer" : "DEATH CHAMBER"},
        16 : {"question" : "What is the standard size of a pint, to the nearest 10ml?",
        "answer" : "470"},
        17 : {"question" : "What is the standard size of a schooner, to the nearest 10ml?",
        "answer" : "430"},
        18 : {"question" : "What is the standard size of a jug of beer, to the nearest 10ml?",
        "answer" : "1140"},
        19 : {"question" : "What is the size of an alcoholic shot, to the nearest 5ml?",
        "answer" : "45"},
        20 : {"question" : "What is the standard size of a schooner, to the nearest 5ml?",
        "answer" : "425"},
        21 : {"question" : "What kind of beer is a Guiness?",
        "answer" : "STOUT"},
        22 : {"question" : "What spirit is produced by distilling Agave cactus?",
        "answer" : "TEQUILA"},
        23 : {"question" : "What is the opposite of matter?",
        "answer" : "ANTIMATTER"},
        24 : {"question" : "Which of Newton's 3 Laws, is algebraically represented by: F = ma?",
        "answer" : "2ND"},
        25 : {"question" : "When Pluto was a planet, what type of planet was it?",
        "answer" : "DWARF"},
        26 : {"question" : "How many teeth does an adult human have?",
        "answer" : "32"},
        27 : {"question" : "How many bones does a baby have approximately?",
        "answer" : "300"},
        28 : {"question" : "What is the current population of Australia to the neart million",
        "answer" : "26"},
        29 : {"question" : "In which Chinese mainland town did COVID-19 originate?",
        "answer" : "WUHAN"},
        30 : {"question" : "In what year were the two nuclear warheads dropped on Nagasaki and Hiroshima?",
        "answer" : "1945"},
        31 : {"question" : "In what year did Apollo 11 land on the moon",
        "answer" : "1969"},
        32 : {"question" : "In which year did Kanye West release his masterpiece album 'My Beautiful Dark Twisted Fantasy'?",
        "answer" : "2010"},
        33 : {"question" : "How many albums has Kanye West released to date, including collaborations?",
        "answer" : "10"},
        34 : {"question" : "What is the box office of the Hollywood film Avatar to the nearest 0.1 billion?",
        "answer" : "2.8"},
        35: {"question" : "How many mainstream Lucasfilm Star Wars Movies are there?",
        "answer" : "11"},
        36: {"question" : "How many players are on field in a cricket team, when fielding?",
        "answer" : "11"},
        37 : {"question" : "What is the default position of the 2nd umpire on a cricket field",
        "answer" : "SQUARE LEG"},
        38 : {"question" : "How many players are on each team in a football (soccer) match",
        "answer" : "11"},
        39 : {"question" : "What is the tennis Grandslam tournament in France called?",
        "answer" : "ROLAND GARROS"},
        40 : {"question" : "Which of the following is not an Olympic Sport: Squash, Skeleton, Equestrian, BMX",
        "answer" : "SQUASH"},
        41 : {"question" : "What subsidiary car manufacturer and brand is owned by BMW?",
        "answer" : "MINI"},
        42 : {"question" : "What car manufacturer names their cars after types of bulls?",
        "answer" : "LAMBORGHINI"},
        43 : {"question" : "What is Earth's largest continent",
        "answer" : "ASIA"},
        44 : {"question" : "What is capital of Cuba?",
        "answer" : "HAVANA"},
        45 : {"question" : "Which Central American country has a name which translates in English to 'The Savior'?",
        "answer" : "EL SALVADOR"},
        46 : {"question" : "What is the rarest colour of M&M?",
        "answer" : "BROWN"},
        47 : {"question" : "What is the BAC (Blood Alcohol Limit) to legall drive in Australia (with full license)?",
        "answer" : "0.05%"},
        48 : {"question" : "What generation of coding language is Python?",
        "answer" : "4TH"},
        49 : {"question" : "What generation of coding language is C?",
        "answer" : "3RD"},
        50 : {"question" : "What is the full name of the person who invented the word 'vomit'?",
        "answer" : "WILLIAM SHAKESPEARE"},
    }
    player_num = 0
    if player_num == len(players):
        player_num == 0
    
    player_num += 1
    question_nums = []
    selected_questions = []

    for i in range(len(quiz)):
        question_nums.append(i+1)

    selected_questions = random.sample(question_nums, 10)
    # the variable integer here (second input), determines how many questions are selected from the question bank
    # through lines 107 - 113 above, the specified number of questions are randomly selected and randomly ordered from the bank

    print()
    print()

    letter_by_letter('Enjoy your game and drink responsibly.\033[36m')

    print()
    print()        
            

    for i in selected_questions:
        player_num = 0
    if player_num == len(players):
        player_num == 0
    
    player_num += 1



        attempts = 2
        letter_by_letter(quiz[i]["question"])
        letter_by_letter(f"\nEnter your answer {players[player_num].name} Answer: ")
        answer = str(input()).upper()
        if answer == quiz[i]["answer"]:
            print()
            letter_by_letter("Correct Answer!\033[92m")
            letter_by_letter('Next Question')
            print()
        else:
            attempts -= 1
            
            if attempts == 1:
                print()
                letter_by_letter("Incorrect answer you have 1 more attempt. You're halfway to another drink!\033[95m")
                print()
                # player only drinks after running out of both attempts
                letter_by_letter(quiz[i]["question"])
                letter_by_letter(f"\nHave another go {players[player_num].name} Answer: ")
                answer_2 = str(input()).upper()
                if answer_2 == quiz[i]["answer"]:
                    print()
                    letter_by_letter(f"Correct Answer!, good job {players[player_num].name}\033[95m")
                else:
                    print()
                    letter_by_letter(f'''Incorrect, you have run out of attempts. 
    The correct answers was {quiz[i]["answer"]}\n. 
    Pitiful really. Drink up {players[player_num].name}!\033[95m\n''')
                players[player_num].drink()
                print()
                letter_by_letter('Next Question')
                print()

            elif attempts == 0:
                print(f'''Incorrect, you have run out of attempts. 
    The correct answers was {quiz[i]["answer"]}. 
    Pitiful really. Drink up {players[player_num].name}!\033[95m''')
                players[player_num].drink()
    ##################################################### players[player_num].drink ###############################################################
                print()
                letter_by_letter('Next Question')
                print()

    letter_by_letter("Well done, youve finished the game!\033[36m")
    
    return

