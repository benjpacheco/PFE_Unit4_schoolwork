import random

countFlips = 0
initial = 10
bankroll = initial
while 0 < bankroll < 2*initial:
    flip = random.choice(['heads', 'tails'])
    countFlips += 1
    if flip == 'heads':
        bankroll += 1
    else:
        bankroll -= 1

print(countFlips)
