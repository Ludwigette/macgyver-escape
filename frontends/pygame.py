# pygame.py ---
#
# Filename: pygame.py
# Author: Louise <louise>
# Created: Fri Nov 15 17:59:55 2019 (+0100)
# Last-Updated: Thu Nov 21 11:28:56 2019 (+0100)
#           By: Louise <louise>
#
from .general import Frontend
import pygame
import logging
import settings

class PygameFrontend(Frontend):
    def __init__(self, width=15, height=15, scale=20):
        pygame.init()
        self.width = width
        self.height = height
        self.scale = scale
        self.screen = pygame.display.set_mode((width * scale,
                                               height * scale))
        self.running = False

        # TODO: config path
        self.bigfont = pygame.font.SysFont("serif", self.scale * 2)
        self.littlefont = pygame.font.SysFont("serif", self.scale)
        
        self.assets = {
            "floor": pygame.image.load(settings.PYGAME_ASSETS_FLOOR),
            "wall":  pygame.image.load(settings.PYGAME_ASSETS_WALL),
            "macgyver": pygame.image.load(settings.PYGAME_ASSETS_MACGYVER),
            "guard": pygame.image.load(settings.PYGAME_ASSETS_GUARD),
            "needle": pygame.image.load(settings.PYGAME_ASSETS_NEEDLE),
            "ether": pygame.image.load(settings.PYGAME_ASSETS_ETHER),
            "tube": pygame.image.load(settings.PYGAME_ASSETS_TUBE),
            "syringe": pygame.image.load(settings.PYGAME_ASSETS_SYRINGE),
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

    def print_centered(self, font, text, y_position):
        text = font.render(text, True, (0, 0, 0))
        rect = text.get_rect()
        rect.x = (self.width * self.scale - rect.w) // 2

        if y_position == "top":
            rect.y = (self.height * self.scale // 2) - rect.h
        elif y_position == "bottom":
            rect.y = (self.height * self.scale // 2)

        self.screen.blit(text, rect)
        
    def defeat(self):
        self.print_centered(self.bigfont, "You lost!", "top")
        self.print_centered(self.littlefont,
                            "You failed to collect all items.",
                            "bottom")
        pygame.display.flip()
        pygame.time.wait(4000)
        
        self.running = False

    def victory(self):
        self.print_centered(self.bigfont, "You win!", "top")
        self.print_centered(self.littlefont,
                            "You escape unnoticed.",
                            "bottom")
        pygame.display.flip()
        pygame.time.wait(4000)
        
        self.running = False
        
    def main_loop(self, game):
        self.running = True

        while self.running:
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
                    self.running = False
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
                        change, game = game.send_event(event_key)
                        # If change is True but not victory, then it's defeat
                        if change and game.game_state()["victory"] == True:
                            self.victory()
                        elif change:
                            self.defeat()
