# game.py ---
#
# Filename: game.py
# Author: Louise <louise>
# Created: Fri Nov 15 17:27:09 2019 (+0100)
# Last-Updated: Fri Nov 15 17:45:04 2019 (+0100)
#           By: Louise <louise>
#
import logging

class Game:
    def __init__(self, file_object):
        # Loading every character in file object except for newlines
        self.map = [char
                    for line in file_object.readlines()
                    for char in line if char != '\n']
        if len(self.map) != 15 * 15:
            logging.warning("Map file is not 15x15. Might not be a map file.")
            logging.warning("The map array will be cut down to 15x15.")
            self.map = self.map[:15*15]

