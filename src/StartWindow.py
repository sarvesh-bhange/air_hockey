import pygame
import os
pygame.mixer.init()
from Button import Button
from constant import *
from events import GAME_WINDOW

class StartWindow(object):
    def __init__(self):
        

        self.start_button = Button(WIDTH/2 - 140/2, HEIGHT/2 - 60/2,60,100,50, BLACK, "Start")

        self.quit_button = Button(WIDTH/2 - 140/2, HEIGHT/2+40,60,100,50, BLACK, "Quit")

    def render(self, win,events,navigate,props):
        if self.start_button.isclick(events):
            navigate('GAME_WINDOW')

        if self.quit_button.isclick(events):
            pygame.event.post(pygame.event.Event(pygame.QUIT))

        win.fill((BLUE))

        self.start_button.draw(win)
        self.quit_button.draw(win)
        
        game_title= pygame.font.SysFont('comicsans',100)

        game_title_render= game_title.render('AIR HOCKEY',1,(WHITE))

        game_title_render_x= WIDTH/2- game_title_render.get_width()/2
        
        game_title_draw= win.blit(game_title_render,(game_title_render_x,40))


        pygame.display.update()
