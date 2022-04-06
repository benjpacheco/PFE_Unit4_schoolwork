import cards

def oneGame(initial):
    countGame = 0
    bankroll = initial
    while 0 < bankroll < 2*initial:
        hand = []
        countGame += 1
        d = cards.shuffledDeck()
        for number in range(4):  
            card = d[number]
            hand.append(cards.suitOf(card))
        for card in hand:
            if card == 'hearts':
                bankroll += 1
        if 'hearts' not in hand:
            bankroll -= 1
    return countGame
def experiment(initial, repetitions):
    count = 0
    for number in range(repetitions):
        count += oneGame(initial)
    print('Average number of rounds:', count/repetitions)
    print()

while True:
 n = int(input('Enter initial amount: '))
 experiment(n, 1000)
