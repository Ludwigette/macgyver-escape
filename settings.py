# settings.py --- 
# 
# Filename: settings.py
# Author: Louise <louise>
# Created: Mon Nov 18 11:00:41 2019 (+0100)
# Last-Updated: Thu Nov 21 14:08:08 2019 (+0100)
#           By: Louise <louise>
#
import os

# General settings
BASE_DIR = os.path.dirname(__file__)

# Game settings
MAP_WIDTH = 15
MAP_HEIGHT = 15

# PygameFrontend settings
PYGAME_ASSETS_DIR = os.path.join(BASE_DIR, "assets")

PYGAME_BG_COLOR = (255, 255, 255)
PYGAME_TEXT_COLOR = (0, 0, 0)

PYGAME_ASSETS_FLOOR = os.path.join(PYGAME_ASSETS_DIR, "floor.bmp")
PYGAME_ASSETS_WALL = os.path.join(PYGAME_ASSETS_DIR, "wall.bmp")
PYGAME_ASSETS_MACGYVER = os.path.join(PYGAME_ASSETS_DIR, "macgyver.bmp")
PYGAME_ASSETS_GUARD = os.path.join(PYGAME_ASSETS_DIR, "murdock.bmp")
PYGAME_ASSETS_NEEDLE = os.path.join(PYGAME_ASSETS_DIR, "needle.bmp")
PYGAME_ASSETS_ETHER = os.path.join(PYGAME_ASSETS_DIR, "ether.bmp")
PYGAME_ASSETS_TUBE = os.path.join(PYGAME_ASSETS_DIR, "tube.bmp")
PYGAME_ASSETS_SYRINGE = os.path.join(PYGAME_ASSETS_DIR, "syringe.bmp")
