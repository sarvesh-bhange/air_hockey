import pygame
import random
from constant import *
from Bar import Bar

class ball(object):
    def __init__(self,x,y,radius):
        self.x=x
        self.y=y
        self.radius=radius
        self.horizontal_vel=+BALL_HORIZONTAL_SPEED
        self.vertical_vel=+BALL_VERTICAL_SPEED


    def draw(self,surface):

        pygame.draw.circle(surface,(DARK_BLUE),(self.x,self.y),self.radius)

    def move(self,wall1,wall2,white_bar,red_bar,screen_width):

        ball_top=self.y - self.radius
        ball_bottom=self.y + self.radius
        ball_right= self.x+self.radius
        ball_left= self.x-self.radius 

        # Vertical wall collision
        if ball_top <= wall1.y+ wall1.height:
            self.vertical_vel= -self.vertical_vel

        if ball_bottom >= wall2.y:
            self.vertical_vel= -self.vertical_vel

        future_ball_right = ball_right + self.horizontal_vel
        future_ball_y = self.y + self.vertical_vel


        # Horizontal bar collision
        if future_ball_right >= red_bar.x and future_ball_y > red_bar.y and future_ball_y < red_bar.y+red_bar.height:
            self.horizontal_vel= -self.horizontal_vel
        
        elif ball_right + self.horizontal_vel > screen_width:
            white_bar.score +=1
            
            self.reset()

        if ball_left +self.horizontal_vel <= white_bar.x+white_bar.width and self.y >= white_bar.y and self.y <= white_bar.y+white_bar.height:
            self.horizontal_vel= -self.horizontal_vel

        elif ball_left + self.horizontal_vel <0:
            red_bar.score +=1

            self.reset()

        self.x+=self.horizontal_vel
        self.y+= self.vertical_vel
    
    def reset(self):
        self.x= WIDTH/2

        self.y= HEIGHT/2

        self.vertical_vel = random.choice([+1,-1])* BALL_VERTICAL_SPEED

        self.horizontal_vel = random.choice([+1,-1]) * BALL_HORIZONTAL_SPEED
    

