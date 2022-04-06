
import random

def oneGame(initial):
    countFlips = 0
    bankroll = initial
    while 0 < bankroll < 2*initial:
        flip = random.choice(['heads', 'tails'])
        countFlips += 1
        if flip == 'heads':
            bankroll += 1
        else:
            bankroll -= 1
    return countFlips

print(oneGame(10))
print(oneGame(10))
print(oneGame(10))
