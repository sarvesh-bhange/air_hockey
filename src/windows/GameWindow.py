
import random
from Timer import Timer
import pygame
from Ball import Ball
from Bar import Bar
from Wall import Wall
from constant import *


class GameWindow(object):
    def __init__(self):
        self.white_bar=Bar(0,HEIGHT/2-BAR_HEIGHT/2,BAR_WIDTH,BAR_HEIGHT,WHITE)

        self.red_bar=Bar(WIDTH-BAR_WIDTH,HEIGHT/2-BAR_HEIGHT/2,BAR_WIDTH,BAR_HEIGHT,RED)

        self.wall1= Wall(0,HEADER_HEIGHT,BORDER_WIDTH,BORDER_HEIGHT,BLACK)
        self.wall2= Wall(0,HEIGHT - BORDER_HEIGHT,BORDER_WIDTH,BORDER_HEIGHT,BLACK)

        self.ball=Ball(WIDTH/2,HEIGHT/2,BALL_RADIUS)

        self.timer= Timer(500-50,10,WHITE)

    def draw_font(self,surface,white_score,red_score):
        score_font = pygame.font.SysFont('comicsans',40)

        red_score_render= score_font.render('Score : '+str(red_score),1,(RED))
        
        white_score_render= score_font.render('Score : '+str(white_score),1,(WHITE))

        white_text_height=white_score_render.get_height()

        red_text_rect = red_score_render.get_rect()

        surface.blit(red_score_render,(WIDTH-(10+red_text_rect.width),HEADER_HEIGHT/2-(red_text_rect.height/2)))

        surface.blit(white_score_render,(10,HEADER_HEIGHT/2-white_text_height/2))

    def draw_window(self, win,events):
        win.fill(BLUE,(0,0,WIDTH,HEIGHT))
        self.white_bar.draw(win)
        self.red_bar.draw(win)
        self.wall1.draw(win)
        self.wall2.draw(win)
        self.draw_font(win,self.white_bar.score,self.red_bar.score)
        self.ball.draw(win)
        self.timer.draw(win,events)
        pygame.display.update()

    def move_objects(self):
        keys=pygame.key.get_pressed()
        
        self.red_bar.move(keys,pygame.K_UP, pygame.K_DOWN,self.wall1,self.wall2)
        self.white_bar.move(keys,pygame.K_w,pygame.K_s,self.wall1,self.wall2)

        self.ball.move(self.wall1,self.wall2,self.white_bar,self.red_bar,WIDTH)

    def render(self, surface,events):
        self.move_objects()
        self.draw_window(surface,events)