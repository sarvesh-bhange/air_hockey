import pygame
import os
from constant import *
from Bar import  Bar

win=pygame.display.set_mode((WIDTH,HEIGHT))

clock=pygame.time.Clock()

white_bar=Bar(0,HEIGHT/2-BAR_HEIGHT/2,BAR_WIDTH,BAR_HEIGHT,WHITE)

black_bar=Bar(WIDTH-BAR_WIDTH,HEIGHT/2-BAR_HEIGHT/2,BAR_WIDTH,BAR_HEIGHT,BLACK)

def draw_window():
    win.fill(PURPLE,(0,0,WIDTH,HEIGHT))
    white_bar.draw(win)
    black_bar.draw(win)
    pygame.display.update()



# Main Loop

run=True

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit
    draw_window()
