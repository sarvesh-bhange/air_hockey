import pygame
import os
pygame.font.init()
pygame.mixer.init()
from constant import *

class Button(object):
    def __init__(self,x,y,size,width,height,colour,text=""):
        self.button_click=pygame.mixer.Sound(os.path.join(os. getcwd(),'src/Sounds/button_click.wav'))
        self.x=x
        self.y=y
        self.colour=colour
        self.text=text
        self.width=width
        self.height=height
        self.size= size


    def isclick(self,events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.isover():
                    self.button_click.play()
                    return True

        return False

    def draw(self,surface):

        if self.text != "":            

            button_rect= pygame.Rect(self.x,self.y,self.width,self.height)

            pygame.draw.rect(surface,(RED),button_rect)


            button_text_font=pygame.font.SysFont('comicsans',self.size)
            
            text_render= button_text_font.render(self.text,1,(self.colour))

            text_rect = text_render.get_rect()

            button_center_x = self.x + ( self.width / 2 - text_rect.width / 2)
            button_center_y = self.y + ( self.height / 2 - text_rect.height / 2)

            surface.blit(text_render,(button_center_x,button_center_y))
        
    def isover(self):
        pos=pygame.mouse.get_pos()

        if pos[0] >= self.x and pos[0]<= self.x+self.width:
            
            if pos[1] >= self.y and pos[1] <= self.y+self.height:
                return True

        return False
            
