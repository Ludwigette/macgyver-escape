# general.py ---
#
# Filename: general.py
# Author: Louise <louise>
# Created: Fri Nov 15 18:03:03 2019 (+0100)
# Last-Updated: Wed Nov 20 12:53:02 2019 (+0100)
#           By: Louise <louise>
#


class Frontend:
    """This class is intended to represent
    all frontends. They're all supposed
    to inherit from it, and overload its
    methods. It can't be instanced per se."""

    def __init__(self):
        raise TypeError("This class cannot be instanced.")

    # Runs the main loop of the game
    def main_loop(self, game):
        pass
