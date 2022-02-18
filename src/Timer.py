import pygame
from constant import TIME
from constant import *
from events import TIMMER_EVENT


class Timer(object):
    def __init__(self,x,y,colour):

        self.x=x
        self.y=y
        self.time= TIME
        self.colour=colour

    def draw(self,surface,events):

        for event in events:
            if event.type ==TIMMER_EVENT:
                self.time-=1        

        timer_font= pygame.font.SysFont('comicsans',50)

        timer_font_render= timer_font.render('Time '+str(self.time//60)+" : "+str(self.time%60),1,(self.colour))
        timer_blit= surface.blit(timer_font_render,(self.x,self.y))

    def reset(self):
        self.time = TIME


