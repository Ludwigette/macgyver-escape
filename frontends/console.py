# console.py --- 
# 
# Filename: console.py
# Author: Louise <louise>
# Created: Mon Nov 18 14:48:50 2019 (+0100)
# Last-Updated: Mon Nov 18 15:21:53 2019 (+0100)
#           By: Louise <louise>
# 

class ConsoleFrontend:
    def __init__(self, width = 15, height = 15):
        self.width = 15
        self.height = 15
        
    def main_loop(self, game):
        state = game.game_state()
        
        for i, char in enumerate(state['map']):
            y, x = divmod(i, self.width)
            # Print element without a newline, except if we're
            # about to enter another line
            print(char, end = "" if x != 14 else "\n")
