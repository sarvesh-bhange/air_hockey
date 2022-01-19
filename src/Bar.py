import pygame
from constant import *

class Bar (object):
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def draw(self, surface):
        print(self.y)
        bar_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, self.colour,bar_rect)
        
    def move(self,keys,up_key,down_key,wall,wall2):
        if(keys[up_key] and self.y-vel  > BORDER_HEIGHT):
            self.y-=vel

        if(keys[down_key]and self.y+vel+BAR_HEIGHT<wall.y):
            self.y+=vel

                              
