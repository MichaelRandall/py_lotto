#!/usr/bin/env python
import random # used to work with random numbers
import argparse # used to parse command line arguments
import locale # used to work with numbers and local formatting
import itertools # used to flatten a list of lists
import pandas # used for data analysis - here frequencies


# get user input from command line to determine number of draws to generate
parser = argparse.ArgumentParser(description='Specify the number of user draws.')
parser.add_argument('-d','--draw_count', type=int, help='an integer for number of draws')
parser.add_argument('-r','--reverse_game', action="store_true", help='run a game until a winner is drawn')
parser.add_argument('-s','--show_stats', action="store_true", help='display statistics after game')
parser.add_argument('-n','--number_count', type=int, help='an interger for the number of numbers drawn per lotto.')
args = parser.parse_args()
draw_count = args.draw_count
reverse = args.reverse_game
stats = args.show_stats
number_count = args.number_count

# generate a lotto ball holder and populate it with all the numbers for drawing
## use a list with a range of numbers from 1 to 49
ball_cage = list(range(1,50))

draw_holder = [] #holds all the draws or user ticket values
winner_count = 0 #holds the count of all winning tickets - all 6 match
loser_count = 0 #holds the count of all losing tickets - if not all 6 numbers match, then loser

winner_found = False
number_of_draws = 0

# generate a lotto draw - list (6) random numbers - for win numbers and draws
# draw returns a sorted list of 6 random numbers between 1 and 49
def draw():
    draw = sorted(random.sample(range(1,50),number_count))
    return draw


# draw the lotto numbers because in both instances, the lotto balls have to be drawn
lotto_draw = draw() # draw the set of numbers that users must match

if reverse:
    print('Reverse lotto, numbers are drawn until a set of numbers match the lottery numbers')
    while not winner_found:
        cur_draw = draw()
        if cur_draw == lotto_draw:
            draw_holder.append(cur_draw)
            winner_found = True
        else:
            draw_holder.append(cur_draw)
            number_of_draws = number_of_draws + 1
    print('Number of draws: ' + str(number_of_draws))
else:
    print('Standard lottory game')

    # need to generate multiple draws and store them for comparison later
    counter = 0
    while counter < draw_count:
        draw_holder.append(draw())
        counter = counter + 1


    # compare all draws to the lotto draw numbers
    for draw in draw_holder:
        if draw == lotto_draw:
            winner_count = winner_count + 1
        else:
            loser_count = loser_count + 1

    # print the results of the drawing
    print(str(winner_count) + ' winning tickets, and ' + str(loser_count) + ' losing tickets.')

print('Lottery numbers for the week: ' + str(lotto_draw))

if stats:
    my_list = list(itertools.chain(*draw_holder))
    my_series = pandas.Series(my_list)
    counts = my_series.value_counts()
    print(str(counts))
