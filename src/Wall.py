import pygame

class Wall(object):
    def __init__(self,x,y,width,height,colour):

        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.colour=colour

    def draw(self,surface):
        wall=pygame.Rect(self.x,self.y,self.width,self.height)
        pygame.draw.rect(surface,self.colour,wall)