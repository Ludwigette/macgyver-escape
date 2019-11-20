# game.py ---
#
# Filename: game.py
# Author: Louise <louise>
# Created: Fri Nov 15 17:27:09 2019 (+0100)
# Last-Updated: Wed Nov 20 17:22:34 2019 (+0100)
#           By: Louise <louise>
#
import random
import logging


class Game:
    """Game logic class."""
    def __init__(self, file_object, width=15, height=15):
        # Loading every character in file object except for newlines
        self.map = [char
                    for line in file_object.readlines()
                    for char in line if char != '\n']

        self.width = width
        self.height = height
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

        # Misc.
        self.victory = False

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
            "objects": self.objects,
            # Victory status
            "victory": self.victory
        }

    # Send an event (U for Up, R for Right, D for Down, L for Left)
    # Returns a tuple of a boolean representing if the state of victory
    # was changed (defeat or victory) and the new Game object
    def send_event(self, event):
        current_y, current_x = divmod(self.position, self.width)

        # New position
        if event == "U":
            new_y, new_x = current_y - 1, current_x
        elif event == "R":
            new_y, new_x = current_y, current_x + 1
        elif event == "D":
            new_y, new_x = current_y + 1, current_x
        elif event == "L":
            new_y, new_x = current_y, current_x - 1

        # Checking if new position is within bounds
        if not (0 <= new_y < self.height and 0 <= new_x < self.width):
            return False, self

        # Checking if new position is a wall
        new_position = new_y * self.width + new_x
        if self.map[new_position] == "W":
            return False, self

        # Checking if new position is that of the guard, and if it is,
        # check defeat or victory
        if new_position == self.guard:
            return True, self
            
        # Updating position
        self.position = new_position
        return False, self
