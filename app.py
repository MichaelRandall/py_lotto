#!/usr/bin/env python
import random

draw_count = 5 #number of draws before lotto drawing date
draw_holder = [] #holds all the draws or user ticket values

# generate a lotto ball holder and populate it with all the numbers for drawing
## use a list with a range of numbers from 1 to 49
ball_cage = list(range(1,50))
print(ball_cage) # test that ball cage contains correct range
 
# generate a lotto draw - list 4 (6) random numbers - for win numbers and draws
def draw():
    draw = sorted(random.sample(range(1,50),4))
    return draw

lotto_draw = draw() # draw the set of numbers that users must match

# need to generate multiple draws and store them for comparison later
counter = 0
while counter < draw_count:
    draw_holder.append(draw())
    counter = counter + 1

print(draw_holder)



# compare draws to the lotto draw numbers
# print count, draw number and win number
# print all draw numbers
