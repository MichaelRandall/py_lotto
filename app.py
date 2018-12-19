#!/usr/bin/env python
import random


# generate a lotto ball holder and populate it with all the numbers for drawing
## use a list with a range of numbers from 1 to 49

ball_cage = list(range(1,50))
print(ball_cage) # test that ball cage contains correct range
 
# generate a lotto draw - list 4 (6) random numbers - for win numbers and draws
def draw():
    draw = sorted(random.sample(range(1,50),4))
    print(draw)

draw() # test draw method

# compare draws to the lotto draw numbers
# print count, draw number and win number
# print all draw numbers
