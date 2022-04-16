import random

numberOfStreaks = 0

for experimentNumber in range(10000):
# Code that creates a list of 100 'heads' or 'tails' values.
    flips = [];
    for i in range(100):
        if random.randint(0, 1) == 0:
            flips.append('H')
        else:
            flips.append('T')
# Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 0
    for i in range(1, len(flips)):
        if(flips[i] == flips[i-1]):
            streak+=1
        else:
            streak = 0
        if streak == 6:
            numberOfStreaks += 1
print(numberOfStreaks)
print('Chance of streak: %s%%' % (numberOfStreaks / 100*10000))
