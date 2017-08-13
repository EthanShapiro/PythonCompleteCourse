from random import randrange

def flip_coin(flip_num):
    i = 0
    heads_tails = {'Heads': 0, 'Tails': 0}
    while i < flip_num:
        choice = randrange(0, 1+1)
        if choice == 0:
            heads_tails['Heads'] += 1
        elif choice == 1:
            heads_tails['Tails'] += 1
        i += 1
    print('Heads: ' + str(heads_tails['Heads']))
    print('Tails: ' + str(heads_tails['Tails']))

flip_coin(5)

