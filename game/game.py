# game.py ---
#
# Filename: game.py
# Author: Louise <louise>
# Created: Fri Nov 15 17:27:09 2019 (+0100)
# Last-Updated: Fri Nov 22 11:53:34 2019 (+0100)
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
        self.inventory = []

    # Returns game state (array of chars)
    def game_state(self):
        return {
            # Map
            "map": self.map,
            # MacGyver position
            "position": self.position,
            # Murdock position
            "guard": self.guard,
            # Objects yet to find's position
            "objects": self.objects,
            # Inventory (objects found)
            "inventory": self.inventory,
            # Victory status
            "victory": self.victory
        }

    def is_new_position_possible(self, new_x, new_y):
        new_position = new_y * self.width + new_x

        # Checking if new position is within bounds
        if not (0 <= new_y < self.height and 0 <= new_x < self.width):
            return False

        # Checking if new position is a wall
        if self.map[new_position] == "W":
            return False

        return True

    def obtain_object(self, position):
        """
        Check if there's an object in the new position, and if there is,
        put it out of the map and into the inventory of the player.
        """

        for obj, pos in self.objects.items():
            if position == pos:
                # If that's the case, delete from
                # the list of objects yet to find
                # and add to inventory
                self.inventory.append(obj)
                del self.objects[obj]

                # If all items have been collected,
                # craft the syringe
                if ("needle" in self.inventory and
                        "tube" in self.inventory and
                        "ether" in self.inventory):
                    self.inventory.remove("needle")
                    self.inventory.remove("tube")
                    self.inventory.remove("ether")
                    self.inventory.append("syringe")

                return

    def check_end_of_game(self):
        """
        Check if the position is that of the guard, and if it is,
        check if victory has been obtained (if the syringe is in
        the inventory)
        """
        if self.position == self.guard:
            self.victory = "syringe" in self.inventory
            return True
        return False

    def send_event(self, event):
        """
        Send an event (U for Up, R for Right, D for Down, L for Left)
        Returns a tuple of a boolean representing if the state of victory
        was changed (defeat or victory) and the new Game object
        """
        current_y, current_x = divmod(self.position, self.width)

        # Get new position
        if event == "U":
            new_y, new_x = current_y - 1, current_x
        elif event == "R":
            new_y, new_x = current_y, current_x + 1
        elif event == "D":
            new_y, new_x = current_y + 1, current_x
        elif event == "L":
            new_y, new_x = current_y, current_x - 1

        if not self.is_new_position_possible(new_x, new_y):
            return False, self

        # If new position is possible, we update the state,
        # and do all the neccessary checks.
        new_position = new_y * self.width + new_x
        self.position = new_position
        self.obtain_object(new_position)
        
        return self.check_end_of_game(), self
