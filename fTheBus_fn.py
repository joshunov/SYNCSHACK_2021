import random
import time
from termcolor import colored


def letter_by_letter(string):
    for i in string:
        print(i, end=(''), flush=True)
        time.sleep(0.035)
    return ''

def fTheBus(player_list):
    count = 0

    letter_by_letter('\nThe order of players is as follows:\n')
    for i in range(len(player_list)):
        print(f'{i+1}. {player_list[i].name} ')

    letter_by_letter('\n------GAME RULES------\n')
    letter_by_letter('1. If you make a correct guess in Rounds 1 - 3, you may give a drink to someone else.\n')
    letter_by_letter('2. If you make a correct guess in the 4th and final round, you may give out three drinks.\n')
    letter_by_letter('3. If you make an incorrect guess in any round you will drink.\n')
    letter_by_letter('4. Each player will play the round designated to their number.\n')
    letter_by_letter('5. Once the designated player has either won or made an incorrect guess, their round is over.\n')
    letter_by_letter('6. There is a total number of rounds equal to the number of players\n')
    letter_by_letter('Note: all spelling must be correct!\n')
    print(' ')

    for players in range(len(player_list)):
        
        letter_by_letter(f"It is {colored(player_list[players].name, attrs= ['bold'])}\'s turn\n")

        rank1 = random.choice(('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'))
        rank1int = 0
        if rank1 == 'A' or rank1 == 'J' or rank1 == 'Q' or rank1 == 'K':
            if rank1 == 'A':
                rank1int = 1
            elif rank1 == 'J':
                rank1int = 11
            elif rank1 == 'Q':
                rank1int = 12
            elif rank1 == 'K':
                rank1int = 13
        else:
            rank1int = rank1

        suit1 = random.choice(('Clubs', 'Diamonds', 'Hearts', 'Spades'))
        colour1 = 'white'
        if suit1 == 'Clubs' or suit1 == 'Spades':
            colour1 = 'black'
        elif suit1 == 'Hearts' or suit1 == 'Diamonds':
            colour1 = 'red'
        card1 = rank1 + ' of ' + suit1

#round 1
        attempt = 1

        while attempt <= 3:
            round_1 = input('Red or Black? ').lower()
            verify = False

            while verify == False:
                if round_1 not in ['red', 'black']:
                    round_1 = input("please enter either black or red: ").lower()
                else:
                    break
                    

            letter_by_letter(f'\n----- {card1} -----\n')
            if round_1 == colour1:
                letter_by_letter(f'Correct, {player_list[players].name} may give out one drink.')
                drink1 = int(input('\nWhich player number is drinking? '))
                print(' ')
                player_list[drink1-1].drink()
            elif round_1 != colour1:
                # count += 1
                print(f'Incorrect,{player_list[players].name} you must drink.')
                # print('\n--- Round {} of {} complete ---'.format(count, len(player_list)))
                print(' ')
                player_list[players].drink()
                attempt += 1
                continue
            

            rank2 = random.choice(('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'))
            rank2int = 0
            if rank2 == 'A' or rank2 == 'J' or rank2 == 'Q' or rank2 == 'K':
                if rank2 == 'A':
                    rank2int = 1
                elif rank2 == 'J':
                    rank2int = 11
                elif rank2 == 'Q':
                    rank2int = 12
                elif rank2 == 'K':
                    rank2int = 13
            else:
                rank2int = rank2
            suit2 = random.choice(('Clubs', 'Diamonds', 'Hearts', 'Spades'))
            card2 = rank2 + ' of ' + suit2

    #round 2

            round_2 = input('\nHigher or Lower? ').lower()

            while verify == False:
                if round_2 not in ['higher', 'lower']:
                        round_2 = input("please enter either higher or lower: ").lower()
                else:
                    break

            
            print(f'\n----- {card2} -----')
            if round_2 == 'higher' and int(rank2int) > int(rank1int):
                print(f'Correct, {player_list[players].name} you may give out one drink.')
                drink2 = int(input('\nWhich player number is drinking? '))
                player_list[drink2].drink()
                print(' ')
            elif round_2 == 'lower' and int(rank2int) < int(rank1int):
                print(f'Correct, {player_list[players].name} you may give out one drink.')
                drink2 = int(input('\nWhich player number is drinking? '))
                player_list[drink2].drink()
                print(' ')
            else:
                # count += 1
                attempt += 1
                print('Incorrect, you must drink.')
                # print(f'\n--- Round {count} of {len(player_list)} complete ---')
                player_list[players].drink()
                print(' ')
                continue

            rank3 = random.choice(('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'))
            rank3int = 0
            if rank3 == 'A' or rank3 == 'J' or rank3 == 'Q' or rank3 == 'K':
                if rank3 == 'A':
                    rank3int = 1
                elif rank3 == 'J':
                    rank3int = 11
                elif rank3 == 'Q':
                    rank3int = 12
                elif rank3 == 'K':
                    rank3int = 13
            else:
                rank3int = rank3
            suit3 = random.choice(('Clubs', 'Diamonds', 'Hearts', 'Spades'))
            card3 = rank3 + ' of ' + suit3

            if int(rank1int) > int(rank2int):
                highest = int(rank1int)
                lowest = int(rank2int)
            else:
                highest = int(rank2int)
                lowest = int(rank1int)

    #Round 3
            round_3 = input('\nInside or Outside? ').lower()

            while verify == False:
                if round_3 not in ['inside', 'outside']:
                    round_3 = input("please enter either inside or outside: ").lower()
                else:
                    break


            print(f'\n----- {card3} -----')
            if round_3 == 'inside' and int(rank3int) < highest and int(rank3int) > lowest:
                print(f'Correct, {player_list[players].name} you may give out one drink.')
                drink3 = int(input('\nWhich player number is drinking? '))
                drink2[drink3].drink()
                print(' ')
            elif round_3 == 'outside' and int(rank3int) > highest or int(rank3int) < lowest:
                print(f'Correct, {player_list[players].name} you may give out one drink.')
                drink3 = int(input('\nWhich player number is drinking? '))
                player_list[drink3].drink()
                print(' ')
            else:
                # count += 1
                attempt += 1
                print(f'Incorrect, {player_list[players].name} you must drink.')
                # print(f'\n--- Round {count} of {len(player_list)} complete ---')
                player_list[players].drink()
                print(' ')
                continue

            rank4 = random.choice(('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'))
            suit4 = random.choice(('Clubs', 'Diamonds', 'Hearts', 'Spades'))
            card4 = rank4 + ' of ' + suit4

    #Round 4
            round_4 = input('\nGuess a Suit (Clubs, Diamonds, Hearts, Spades): ').lower()

            while verify == False:
                if round_4 not in ['clubs', 'diamonds', 'hearts', 'spades']:
                    round_4 = input("please enter either a suit (Clubs, Diamonds, Hearts, Spades): ").lower()
                else:
                    break

            print(f'\n----- {card4} -----')
            suit4 = suit4.lower()
            if round_4 == suit4:
                print('Correct, you may give out three drinks.')
                drink4_1 = int(input('\nWhich player will drink first? '))
                player_list[drink4_1].drink()
                drink4_2 = int(input('\nWhich player will drink second? '))
                player_list[drink4_2].drink()
                drink4_3 = int(input('\nWhich player will drink third? '))
                player_list[drink4_3].drink()
                print(' ')
                print('----- YOU WON! -----')
                print('--------THANKYOU FOR PLAYING--------')
                # count += 1
                print('--- Round {} of {} complete ---'.format(count, len(player_list)))
            else:
                count += 1
                # attempt += 1
                print('Incorrect, you must drink.')
                # print(f'\n--- Round {count} of {len(player_list)} complete ---')
                player_list[players].drink()
                print(' ')
                continue

        count += 1
        print(f'\n--- Round {count} of {len(player_list)} complete ---')


        break

    print('------------ GAME OVER -------------')
    print('--------THANKYOU FOR PLAYING--------')
    return True


