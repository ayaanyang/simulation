import numpy as np
import sys
import os
import random
from tqdm import trange

"""
there is 3 door
one is win
other two are boom 
player select a door
and master let him know one boom door that he didn't choose
player has two options
first is maintain his decision
second is change his decision

scenario2 code is second option that player changes his decision
"""

cnt_win = 0
cnt_loss = 0
cnt_for = 0
game_num = 100000000

def left_shift(num):
    if num >= 1:
        return num - 1
    elif num == 0:
        return 2

def right_shift(num):
    if num < 2:
        return num + 1
    elif num == 2:
        return 0
def change_choice(player_choice, win_door, door=[0, 0, 0]):
    door[win_door] += 1
    # ex) door = [0, 1, 0]
    if player_choice == win_door:





print("true is: ",cnt_win)
print("false is: ",cnt_loss)
print("win rate is: ",cnt_win/(cnt_win+cnt_loss))
print("loss rate is: ",cnt_loss/(cnt_win+cnt_loss))
