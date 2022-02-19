from Button import Button
from constant import *
import pygame
from events import START_WINDOW

class WinWindow(object):
    def __init__(self):

        self.back_button= Button(20,10,40,80,30,WHITE,'back')
        
        self.Windowcolour= PURPLE                    

    def draw_font(self,surface):

        white_man= pygame.font.SysFont('comicsans',100)

        red_man= pygame.font.SysFont('comicsans',100)

        white_man_render= white_man.render('White',1,(WHITE))

        red_man_render= red_man.render('Red',1,(RED))

        self.red_man_rect= red_man_render.get_rect()
        self.red_man_rect.x = 100
        self.red_man_rect.y = HEIGHT/2-(self.red_man_rect.height/2)

        self.white_man_rect= white_man_render.get_rect()

        self.white_man_rect.x = 800
        self.white_man_rect.y= HEIGHT/2-(self.white_man_rect.height/2)

        surface.blit(white_man_render,(self.red_man_rect.x,self.red_man_rect.y))
        
        surface.blit(red_man_render,(self.white_man_rect.x,self.white_man_rect.y))

    def win_event(self,win,white_score,red_score):

        winner_font= pygame.font.SysFont('comicsans',100)

        if white_score == red_score:
            draw_font_render = winner_font.render('DRAW',1,(BLUE))
            draw_font_rect =  draw_font_render.get_rect()
            win.blit(draw_font_render,(WIDTH/2-(draw_font_rect.width/2),self.red_man_rect.y))
        else:
            winner_font_render = winner_font.render('WINNER',1,(BLUE))
            winner_font_rect =  winner_font_render.get_rect()

            if white_score > red_score:
                win.blit(winner_font_render,(50,self.white_man_rect.y-winner_font_rect.height))

            elif red_score > white_score:
                win.blit(winner_font_render,(700,self.red_man_rect.y-winner_font_rect.height))                
            
    
    
    def back(self,events,navigate):

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.back_button.isover():
                    navigate("START_WINDOW")


    
    def render(self,surface,events,navigate,props):
        surface.fill((self.Windowcolour))
        self.back_button.draw(surface)
        self.draw_font(surface)
        self.win_event(surface,props[0],props[1])

        self.back(events,navigate)
        
        pygame.display.update()