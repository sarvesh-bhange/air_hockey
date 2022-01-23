import pygame
from constant import *

class Bar (object):
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.score=0
        self.vertical_vel= +vel


    def draw(self, surface):
        bar_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, self.colour,bar_rect)
        
    def move(self,keys,up_key,down_key,wall1,wall2):
        if(keys[up_key] and self.y-vel  >= wall1.y+wall1.height):
            self.y-=vel

        if(keys[down_key]and self.y+vel+BAR_HEIGHT<=wall2.y):
            self.y+=vel

                              
