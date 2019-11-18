# general.py ---
#
# Filename: general.py
# Author: Louise <louise>
# Created: Fri Nov 15 18:03:03 2019 (+0100)
# Last-Updated: Fri Nov 15 19:18:01 2019 (+0100)
#           By: Louise <louise>
#

# This class is intended to represent
# all frontends. They're all supposed
# to inherit from it, and overload its
# methods. It can't be instanced per se.
class Frontend:
    def __init__(self):
        raise TypeError("This class cannot be instanced.")

    # Runs the main loop of the game
    def main_loop(self, game):
        pass
