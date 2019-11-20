# game.py ---
#
# Filename: game.py
# Author: Louise <louise>
# Created: Fri Nov 15 17:27:09 2019 (+0100)
# Last-Updated: Wed Nov 20 10:09:16 2019 (+0100)
#           By: Louise <louise>
#
import logging, random

class Game:
    def __init__(self, file_object, width = 15, height = 15):
        # Loading every character in file object except for newlines
        self.map = [char
                    for line in file_object.readlines()
                    for char in line if char != '\n']
        if len(self.map) != width * height:
            logging.warning("Map file is not 15x15. Might not be a map file.")
            logging.warning("The map array will be cut down to 15x15.")
            self.map = self.map[:width * height]

        # Init object locations
        free_spaces = [i for i, char in enumerate(self.map)if char == ' ']
        objects_positions = random.sample(free_spaces, 3)
        self.objects = {
            "needle": objects_positions[0],
            "tube": objects_positions[1],
            "ether": objects_positions[2]
        }
        
        # no need to keep initial position in map, both of macgyver and murdock
        self.position = self.map.index('M')
        self.map[self.position] = ' '
        self.guard = self.map.index('B')
        self.map[self.guard] = ' '
        
    # Returns game state (array of chars)
    def game_state(self):
        return {
            # Map
            "map": self.map,
            # MacGyver position
            "position": self.position,
            # Murdock position
            "guard": self.guard,
            # Objects position
            "objects": self.objects
        }

    # Send an event (U for Up, R for Right, D for Down, L for Left)
    # Returns a tuple of a boolean representing if the event was possible,
    # and the new Game object
    def send_event(self, event):
        pass
