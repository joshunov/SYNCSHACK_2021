def winning_horse(dict):
    for key in dict.keys():
        if dict[key] == 9:
            winner = key
    
    return winner