from Timer import Timer
import pygame
import os
pygame.mixer.init()
from Ball import Ball
from Bar import Bar
from Wall import Wall
from constant import *
from Button import Button
from events import START_WINDOW

class GameWindow(object):
    def __init__(self):


        pygame.mixer.music.load(os.path.join(os. getcwd(),'src/Sounds/background_2.mp3'))
        pygame.mixer.music.set_volume(0.1) 

        self.white_bar=Bar(0,HEIGHT/2-BAR_HEIGHT/2,BAR_WIDTH,BAR_HEIGHT,WHITE)

        self.red_bar=Bar(WIDTH-BAR_WIDTH,HEIGHT/2-BAR_HEIGHT/2,BAR_WIDTH,BAR_HEIGHT,RED)

        self.wall1= Wall(0,HEADER_HEIGHT,BORDER_WIDTH,BORDER_HEIGHT,BLACK)
        self.wall2= Wall(0,HEIGHT - BORDER_HEIGHT,BORDER_WIDTH,BORDER_HEIGHT,BLACK)

        self.ball=Ball(WIDTH/2,HEIGHT/2,BALL_RADIUS)

        self.timer= Timer(500-50,10,WHITE)

        self.reset_button= Button(700,40,40,80,30,WHITE,'Reset')

        self.back_button= Button(300,40,40,80,30,WHITE,'Back')

    def draw_font(self,surface,white_score,red_score):

        white_man= pygame.font.SysFont('comicsans',40)

        red_man= pygame.font.SysFont('comicsans',40)

        white_man_render= white_man.render('White',1,(WHITE))

        red_man_render= red_man.render('Red',1,(RED))

        score_font = pygame.font.SysFont('comicsans',40)

        red_score_render= score_font.render('Score : '+str(red_score),1,(RED))
        
        white_score_render= score_font.render('Score : '+str(white_score),1,(WHITE))

        white_text_height=white_score_render.get_height()

        red_text_rect = red_score_render.get_rect()

        red_man_rect= red_man_render.get_rect()

        surface.blit(red_score_render,(WIDTH-(10+red_text_rect.width),40))

        surface.blit(red_man_render,(WIDTH-(10+red_man_rect.width),10))

        surface.blit(white_score_render,(10,40))

        surface.blit(white_man_render,(10,10))
    
    def reset(self):
        self.timer.reset()
        self.white_bar.score=0
        self.red_bar.score=0

    def draw_window(self, win,events):
        win.fill(BLUE,(0,0,WIDTH,HEIGHT))
        self.white_bar.draw(win)
        self.red_bar.draw(win)
        self.wall1.draw(win)
        self.wall2.draw(win)
        self.draw_font(win,self.white_bar.score,self.red_bar.score)
        self.ball.draw(win)
        self.timer.draw(win,events)
        self.reset_button.draw(win)
        self.back_button.draw(win)
        pygame.display.update()

    def move_objects(self):
        keys=pygame.key.get_pressed()
        
        self.red_bar.move(keys,pygame.K_UP, pygame.K_DOWN,self.wall1,self.wall2)
        self.white_bar.move(keys,pygame.K_w,pygame.K_s,self.wall1,self.wall2)

        self.ball.move(self.wall1,self.wall2,self.white_bar,self.red_bar,WIDTH)

    def render(self, surface,events,navigate,props):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play(-1)

        if self.back_button.isclick(events):
            navigate('START_WINDOW')
            self.reset()
            pygame.mixer.music.fadeout(1000)
        
        if self.reset_button.isclick(events):
            self.reset()
                
        if self.timer.time == 0:
            pygame.mixer.music.fadeout(1000)
            navigate("WIN_WINDOW",(self.white_bar.score,self.red_bar.score))
            self.reset()

        self.move_objects()
        self.draw_window(surface,events)