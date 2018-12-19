#!/usr/bin/env python
import random
import argparse

# get user input from command line to determine number of draws to generate
parser = argparse.ArgumentParser(description='Specify the number of user draws.')
parser.add_argument('-d','--draw_count', type=int, help='an integer for number of draws')
args = parser.parse_args()
draw_count = args.draw_count


draw_holder = [] #holds all the draws or user ticket values


# generate a lotto ball holder and populate it with all the numbers for drawing
## use a list with a range of numbers from 1 to 49
ball_cage = list(range(1,50))
# print(ball_cage) # test that ball cage contains correct range
 
# generate a lotto draw - list (6) random numbers - for win numbers and draws
def draw():
    draw = sorted(random.sample(range(1,50),6))
    return draw

lotto_draw = draw() # draw the set of numbers that users must match

# need to generate multiple draws and store them for comparison later
counter = 0
while counter < draw_count:
    draw_holder.append(draw())
    counter = counter + 1


# compare draws to the lotto draw numbers
for draw in draw_holder:
    if draw == lotto_draw:
        print("Win " + str(draw) + " - " + str(lotto_draw))
    else:
        print("Lose" + str(draw) + " - " + str(lotto_draw))
# print count, draw number and win number
# print all draw numbers
