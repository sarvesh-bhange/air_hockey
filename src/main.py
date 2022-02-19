import pygame
from navigator import *
from constant import *
from events import TIMMER_EVENT


pygame.font.init()

win=pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('AIR HOCKEY')


clock=pygame.time.Clock()

pygame.time.set_timer(TIMMER_EVENT,TIME_INTERVEL)


# Main Loop

run=True

while run:
    clock.tick(FPS)

    events = pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            run=False
        
    navigator.render(win,events)


pygame.quit()
