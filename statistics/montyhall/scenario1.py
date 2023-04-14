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

scenario1 code is first option that player does not change decision
"""

cnt_win = 0
cnt_loss = 0
cnt_for = 0
game_num = 1000000
for _ in trange(game_num):
    door = [0, 0, 0]
    win_door = int(random.randrange(0,3))
    door[win_door] += 1
    player_select = int(random.randrange(0,3))
    if door[player_select] == 1:
        cnt_win += 1
    elif door[player_select] == 0:
        cnt_loss += 1
    else:
        print("error")
        sys.exit()

print("true is: ",cnt_win)
print("false is: ",cnt_loss)
print("win rate is: ",cnt_win/(cnt_win+cnt_loss))
print("loss rate is: ",cnt_loss/(cnt_win+cnt_loss))
