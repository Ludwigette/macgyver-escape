# general.py ---
#
# Filename: general.py
# Author: Louise <louise>
# Created: Fri Nov 15 18:03:03 2019 (+0100)
# Last-Updated: Fri Nov 15 18:25:02 2019 (+0100)
#           By: Louise <louise>
#

# This class is intended to represent
# all frontends. They're all supposed
# to inherit from it, and overload its
# methods. It can't be instanced per se.
class Frontend:
    def __init__(self):
        raise TypeError("This class cannot be instanced.")

    # Load an image from a filename and return an internal representation.
    # The first argument is the position of the sprite in the sheet, and
    # the second is the size of the sprite. Both are a 2-integer tuple.
    def load_image(self, filename: str,
                   position: (int, int) = (0, 0),
                   size: (int, int) = (0, 0)):
        pass

    # Creates a window object with the given parameters. Returns nothing.
    def init_window(self, width: int, height: int, title: str = None):
        pass

    # Draw an image at given position. Returns nothing.
    def draw_image(self, image, position: (int, int)):
        pass

    # Returns an array of events. Each event is represented as a character.
    # R for right, D for down, L for left, U for Up, and Q for Quit
    def get_events(self):
        pass
