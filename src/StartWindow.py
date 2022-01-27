import pygame
from Button import Button
from constant import *
from events import START_GAME
from Timer import Timer

class StartWindow(object):
    def __init__(self):

        self.start_button = Button(WIDTH/2 - 140/2, HEIGHT/2 - 60/2, 140, 60, BLACK, "Start")

        self.quit_button = Button(WIDTH/2 - 140/2, HEIGHT/2+40, 140, 60, BLACK, "Quit")

    def render(self, win,events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.isover():
                    pygame.event.post(pygame.event.Event(START_GAME))

                if self.quit_button.isover():
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

        win.fill((BLUE))

        self.start_button.draw(win)
        self.quit_button.draw(win)
        pygame.display.update()
