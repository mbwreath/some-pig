from random import randint

def one_round(total, strategy):
    round = 0
    while True:
        value = randint(1,6)
        round = round + value

        if value == 1:
            round = 0
            print('your turn is over')
            break

        #build strategy logic and when to stop/keep rolling

    return round
