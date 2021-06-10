#Michael Saladino
"""

Saladino,Michael.py

Analyzing Caps Games

Create a function to get random rols of 2 dice
Create a function to simulate one game of craps
    here we return if you win or lose and the number of attempts
Set up variables for the numbers of wins and loses, experiment number, and a list of rolls
The for loop runs as how many times you set in experiment and plays a  game
    if the result of the same is win or loss then it adds to that variable
    also adds 1 to the rolls index for how many attempts are passed

No Test Data


"""

import random

def roll_dice(): # returns the sum of two Dice Rolls
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    return die1 + die2

def game_loop():

    roll = roll_dice()
    if roll in [7,11]:
        return 'Win',1 # return the outcome and attempts it took to decide
    elif roll in [2,3,12]:
        return 'Loss',1 
    else:
        gameState = "Continue"
        attempts = 1 # track the total rounds
        my_point = roll
        while gameState == "Continue":
            roll=roll_dice()
            attempts += 1 # add 1 until the outcome is decided
            if roll == my_point:
                gameState = "Win"
                return gameState,attempts # return the outcome and rounds
                
            elif roll == 7:
                gameState = "Loss"
                return gameState,attempts # return the outcome and rounds
            else:
                gameState = "Continue"


wins = 0
loss = 0
rolls = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

experiments = 1000000

for x in range(experiments):
    
    outcome,attempts = game_loop()
    
    if outcome == 'Win':
        wins += 1
    else:
        loss += 1
    if attempts <= len(rolls):
        rolls[attempts-1] += 1
    else:
        rolls[-1] += 1

#Win / Loss Percent
print('Percentage of wins: {:.2f}%'.format(wins * 100 / (experiments)))
print('Percentage of losses: {:.2f}%'.format(loss * 100 / (experiments)))

print()
print('Percentage of wins/losses based on rolls')
print()
print('{:>25}{:>20} '.format('% Resolved','Cummulative %'))
print('{:<5}{:>20} {:>20}'.format('Rolls','on this roll','of games resolved'))

for x in range(len(rolls)):
    percentResolved = rolls[x] * 100 / experiments
    totalPercentResolved = 100*sum(rolls[0:x]) / experiments
    
    if x != len(rolls) - 1:
        print('{:>5}{:>20.2f}%{:>20.2f}%'.format(x + 1,percentResolved,totalPercentResolved))
    else:
        print('{:>5}{:>20.2f}%{:>20.2f}%'.format(x + 1, percentResolved, 100 * sum(rolls)/experiments))

