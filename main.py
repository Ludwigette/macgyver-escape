#!/usr/bin/env python3
# main.py ---
#
# Filename: main.py
# Author: Louise <louise>
# Created: Fri Nov 15 17:21:33 2019 (+0100)
# Last-Updated: Wed Nov 20 12:54:24 2019 (+0100)
#           By: Louise <louise>
#
import logging
from argparse import ArgumentParser
from settings import MAP_WIDTH, MAP_HEIGHT
from game import Game
from frontends.pygame import PygameFrontend


def main():
    """Main function. It parses argument, instances the
    Game object and Frontend, and calls the main loop."""

    argument_parser = ArgumentParser(description="""
    Labyrinth game where you have to get
    MacGyver out.
    """)

    args = argument_parser.parse_args()

    # Initializating Game object. If the file cannot be opened,
    # the state cannot be recovered.
    try:
        with open("map.txt", "r") as file:
            game = Game(file, width=MAP_WIDTH, height=MAP_HEIGHT)
    except FileNotFoundError:
        logging.critical("Couldn't open map file (map.txt).")
        exit()

    # Initializing Frontend object.
    frontend = PygameFrontend()

    # Main loop
    frontend.main_loop(game)


if __name__ == "__main__":
    main()
