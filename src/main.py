import pygame
import os
from constant import *
from Bar import  Bar

win=pygame.display.set_mode((WIDTH,HEIGHT))

clock=pygame.time.Clock()

white_bar=Bar(0,HEIGHT/2-BAR_HEIGHT/2,BAR_WIDTH,BAR_HEIGHT,WHITE)

black_bar=Bar(WIDTH-BAR_WIDTH,HEIGHT/2-BAR_HEIGHT/2,BAR_WIDTH,BAR_HEIGHT,BLACK)

border1=pygame.Rect(0,460,BORDER_WIDTH,BORDER_HEIGHT)

border2=pygame.Rect(0,0,BORDER_WIDTH,BORDER_HEIGHT)


def draw_window():
    win.fill(PURPLE,(0,0,WIDTH,HEIGHT))
    white_bar.draw(win)
    black_bar.draw(win)
    pygame.draw.rect(win,(BLACK),border1)
    pygame.draw.rect(win,(BLACK),border2)
    pygame.display.update()

# Main Loop

run=True

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    
    black_bar.move(keys,pygame.K_UP, pygame.K_DOWN,border1,border2)
    white_bar.move(keys,pygame.K_w,pygame.K_s,border1,border2)
    
    draw_window()
    pygame.quit
