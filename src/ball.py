import pygame
from constant import *

class ball(object):
    def __init__(self,x,y,radius):
        self.x=x
        self.y=y
        self.radius=radius
        self.horizontal_vel=+BALL_HORIZONTAL_SPEED
        self.vertical_vel=+BALL_VERTICAL_SPEED


    def draw(self,surface):

        pygame.draw.circle(surface,(DARK_BLUE),(self.x,self.y),self.radius)

    def move(self,wall1,wall2,white_bar,red_bar):

        ball_top=self.y - self.radius
        ball_bottom=self.y + self.radius
        ball_right= self.x+self.radius
        ball_left= self.x-self.radius 

        # Vertical wall collision
        if ball_top <= wall1.y+ wall1.height:
            self.vertical_vel= -self.vertical_vel

        if ball_bottom >= wall2.y:
            self.vertical_vel= -self.vertical_vel


        # Horizontal bar collision
        if ball_right >= red_bar.x and self.y >= red_bar.y and self.y <= red_bar.y+red_bar.height:
            self.horizontal_vel= -self.horizontal_vel

            
        
        if ball_left <= white_bar.x+white_bar.width and self.y >= white_bar.y and self.y <= white_bar.y+white_bar.height:
            self.horizontal_vel= -self.horizontal_vel

        self.x+=self.horizontal_vel
        self.y+= self.vertical_vel

