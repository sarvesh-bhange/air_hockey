import pygame
from constant import *
from Bar import  Bar
from Wall import Wall
from ball import ball
pygame.font.init()

win=pygame.display.set_mode((WIDTH,HEIGHT))

clock=pygame.time.Clock()

white_bar=Bar(0,HEIGHT/2-BAR_HEIGHT/2,BAR_WIDTH,BAR_HEIGHT,WHITE)

red_bar=Bar(WIDTH-BAR_WIDTH,HEIGHT/2-BAR_HEIGHT/2,BAR_WIDTH,BAR_HEIGHT,RED)

wall1= Wall(0,HEADER_HEIGHT,BORDER_WIDTH,BORDER_HEIGHT,BLACK)
wall2= Wall(0,HEIGHT - BORDER_HEIGHT,BORDER_WIDTH,BORDER_HEIGHT,BLACK)

ball=ball(100,PLAY_AREA_HEIGHT/2,BALL_RADIUS)

def draw_font(surface,white_score,red_score):
    score_font = pygame.font.SysFont('comicsans',40)

    game_title=pygame.font.SysFont('comicsans',70)

    game_title_render=game_title.render('AIR HOCKEY',1,(WHITE))

    game_text_rect= game_title_render.get_rect()


    red_score_render= score_font.render('Score : '+str(red_score),1,(RED))
    
    white_score_render= score_font.render('Score : '+str(white_score),1,(WHITE))

    white_text_height=white_score_render.get_height()

    red_text_rect = red_score_render.get_rect()

    surface.blit(red_score_render,(WIDTH-(10+red_text_rect.width),HEADER_HEIGHT/2-(red_text_rect.height/2)))

    surface.blit(white_score_render,(10,HEADER_HEIGHT/2-white_text_height/2))

    surface.blit(game_title_render,(WIDTH/2-(game_text_rect.width/2),HEADER_HEIGHT/2-(game_text_rect.height/2)))

def draw_window():
    win.fill(BLUE,(0,0,WIDTH,HEIGHT))
    white_bar.draw(win)
    red_bar.draw(win)
    wall1.draw(win)
    wall2.draw(win)
    draw_font(win,white_bar.score,red_bar.score)
    ball.draw(win)
    pygame.display.update()

# Main Loop

run=True

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    
    red_bar.move(keys,pygame.K_UP, pygame.K_DOWN,wall1,wall2)
    white_bar.move(keys,pygame.K_w,pygame.K_s,wall1,wall2)

    ball.move(wall1,wall2,white_bar,red_bar)

    draw_window()
    pygame.quit
