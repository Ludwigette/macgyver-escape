# pygame.py ---
#
# Filename: pygame.py
# Author: Louise <louise>
# Created: Fri Nov 15 17:59:55 2019 (+0100)
# Last-Updated: Wed Nov 20 11:11:11 2019 (+0100)
#           By: Louise <louise>
#
from .general import Frontend
import pygame
import logging


class PygameFrontend(Frontend):
    def __init__(self, width=15, height=15, scale=20):
        pygame.init()
        self.width = width
        self.height = height
        self.scale = scale
        self.screen = pygame.display.set_mode((width * scale,
                                               height * scale))

        # TODO: config path
        self.assets = {
            "floor": pygame.image.load("assets/floor.bmp"),
            "wall":  pygame.image.load("assets/wall.bmp"),
            "macgyver": pygame.image.load("assets/MacGyver.bmp"),
            "guard": pygame.image.load("assets/murdock.bmp"),
            "needle": pygame.image.load("assets/needle.bmp"),
            "ether": pygame.image.load("assets/ether.bmp"),
            "tube": pygame.image.load("assets/tube.bmp"),
            "syringe": pygame.image.load("assets/syringe.bmp"),
        }

    # print a sprite intended to be an overlay, i.e. a sprite on top
    # of the base map. It corrects position to center it within the
    # tile.
    def print_overlay_sprite(self, sprite, position):
        pos_y, pos_x = divmod(position, self.width)
        rect = sprite.get_rect()
        rect.x = pos_x * self.scale + (self.scale - rect.w) // 2
        rect.y = pos_y * self.scale + (self.scale - rect.h) // 2
        self.screen.blit(sprite, rect)

    def main_loop(self, game):
        running = True

        while running:
            state = game.game_state()

            # Fill the screen with white
            self.screen.fill((255, 255, 255))

            # Draw the base map
            for i, content in enumerate(state["map"]):
                y, x = divmod(i, self.width)
                position_to_blit = pygame.Rect(x * self.scale, y * self.scale,
                                               self.scale, self.scale)
                if content == "W":
                    self.screen.blit(self.assets["wall"], position_to_blit)
                else:
                    self.screen.blit(self.assets["floor"], position_to_blit)

            # Draw the overlays (Macgyver, Murdock and the objects)
            self.print_overlay_sprite(self.assets["macgyver"],
                                      state["position"])
            self.print_overlay_sprite(self.assets["guard"],
                                      state["guard"])
            self.print_overlay_sprite(self.assets["needle"],
                                      state["objects"]["needle"])
            self.print_overlay_sprite(self.assets["ether"],
                                      state["objects"]["ether"])
            self.print_overlay_sprite(self.assets["tube"],
                                      state["objects"]["tube"])

            # Finish drawing
            pygame.display.flip()

            # Polling events and sending them to game logic
            # (or exiting the game)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    event_key = None

                    if event.key == pygame.K_UP:
                        event_key = "U"
                    elif event.key == pygame.K_RIGHT:
                        event_key = "R"
                    elif event.key == pygame.K_DOWN:
                        event_key = "D"
                    elif event.key == pygame.K_LEFT:
                        event_key = "L"

                    # If event_key is None, that means no valid keys
                    # were pressed
                    if event_key:
                        success, game = game.send_event(event_key)
                        if not success:
                            logging.debug("Move was not possible")
