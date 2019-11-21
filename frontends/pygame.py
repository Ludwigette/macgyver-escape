# pygame.py ---
#
# Filename: pygame.py
# Author: Louise <louise>
# Created: Fri Nov 15 17:59:55 2019 (+0100)
# Last-Updated: Thu Nov 21 14:49:22 2019 (+0100)
#           By: Louise <louise>
#
from .general import Frontend
import pygame
import settings


class PygameFrontend(Frontend):
    def __init__(self, width=15, height=15, scale=20):
        pygame.init()
        self.width = width
        self.height = height
        self.scale = scale
        self.screen = pygame.display.set_mode((width * scale,
                                               (height + 1) * scale))
        self.running = False

        self.bigfont = pygame.font.SysFont("serif", self.scale * 2)
        self.littlefont = pygame.font.SysFont("serif", self.scale)
        self.tinyfont = pygame.font.SysFont("serif", int(self.scale / 1.50))

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
        """
        Print a sprite on the screen. You give it a position on the map
        and it prints it centermost of the tile it can.
        """
        pos_y, pos_x = divmod(position, self.width)
        rect = sprite.get_rect()
        rect.x = pos_x * self.scale + (self.scale - rect.w) // 2
        rect.y = pos_y * self.scale + (self.scale - rect.h) // 2
        self.screen.blit(sprite, rect)

    def print_centered(self, font, text, y_position):
        """
        Print text with font, either on top of the middle line or underneath.
        """
        text = font.render(text, True, settings.PYGAME_TEXT_COLOR)
        rect = text.get_rect()
        rect.x = (self.width * self.scale - rect.w) // 2

        if y_position == "top":
            rect.y = (self.height * self.scale // 2) - rect.h
        elif y_position == "bottom":
            rect.y = (self.height * self.scale // 2)

        self.screen.blit(text, rect)

    def draw_base_map(self, state):
        """Draw the base map, i.e. the maze"""
        for i, content in enumerate(state["map"]):
            y, x = divmod(i, self.width)
            position_to_blit = pygame.Rect(x * self.scale, y * self.scale,
                                           self.scale, self.scale)
            if content == "W":
                self.screen.blit(self.assets["wall"], position_to_blit)
            else:
                self.screen.blit(self.assets["floor"], position_to_blit)

    def draw_overlays(self, state):
        """Draw overlays, (the hero, the gard, and the objects)"""
        self.print_overlay_sprite(self.assets["macgyver"],
                                  state["position"])
        self.print_overlay_sprite(self.assets["guard"],
                                  state["guard"])
        for obj, pos in state["objects"].items():
            self.print_overlay_sprite(self.assets[obj],
                                      pos)

    def draw_inventory(self, state):
        text_inv = self.tinyfont.render("Inventory:", True,
                                        settings.PYGAME_TEXT_COLOR)
        rect_inv = text_inv.get_rect()
        rect_inv.y = self.height * self.scale
        self.screen.blit(text_inv, rect_inv)

        # Draw all objects in inventory
        pos_x = rect_inv.w
        for obj in state["inventory"]:
            rect = self.assets[obj].get_rect()
            # The X position is where we left off, with a small margin
            rect.x = pos_x + (self.scale // 5)
            rect.y = (self.height * self.scale) + (self.scale - rect.h) // 2
            self.screen.blit(self.assets[obj], rect)

            # Modify X position for next object
            pos_x = rect.x + rect.w

    def draw_game(self, game):
        """Draw the game state on self.screen"""
        state = game.game_state()

        self.screen.fill(settings.PYGAME_BG_COLOR)
        self.draw_base_map(state)
        self.draw_overlays(state)
        self.draw_inventory(state)

        # Finish drawing
        pygame.display.flip()

    def draw_defeat(self):
        """Draw the defeat screen, wait 4 seconds and exit the main loop"""
        self.print_centered(self.bigfont, "You lost!", "top")
        self.print_centered(self.littlefont,
                            "You failed to collect all items.",
                            "bottom")
        pygame.display.flip()
        pygame.time.wait(4000)

        self.running = False

    def draw_victory(self):
        """Draw the victory screen, wait 4 seconds and exit the main loop"""
        self.print_centered(self.bigfont, "You win!", "top")
        self.print_centered(self.littlefont,
                            "You escape unnoticed.",
                            "bottom")
        pygame.display.flip()
        pygame.time.wait(4000)

        self.running = False

    def treat_events(self, game):
        """
        Polling events and sending them to game logic (or exiting the game)
        """

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
                    # in each call, we call again the drawing function to
                    # draw the new position of the hero before the end
                    if change and game.game_state()["victory"]:
                        self.draw_game(game)
                        self.draw_victory()
                    elif change:
                        self.draw_game(game)
                        self.draw_defeat()

    def main_loop(self, game):
        self.running = True

        while self.running:
            self.draw_game(game)
            self.treat_events(game)
