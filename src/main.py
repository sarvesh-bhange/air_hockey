import pygame
from navigator import *
from constant import *
from events import TIMMER_EVENT
# from windows.GameWindow import GameWindow
# from StartWindow import StartWindow
# from windows.WinWindow import WinWindow

pygame.font.init()

win=pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption('AIR HOCKEY')


clock=pygame.time.Clock()

# game_window = GameWindow()
# start_window = StartWindow()
# win_window= WinWindow(PURPLE)

# current_window = "START_WINDOW"

pygame.time.set_timer(TIMMER_EVENT,TIME_INTERVEL)


# Main Loop

run=True

while run:
    clock.tick(FPS)

    events = pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            run=False


        # if event.type == GAME_WINDOW:
        #     current_window = "GAME_WINDOW"
        # if event.type == START_WINDOW:
        #     current_window = "START_WINDOW"
        
    navigator.render(win,events)
    # if(current_window == "START_WINDOW"):
    #     start_window.render(win,events)
    # elif(current_window == "GAME_WINDOW"):
    #     win_window.render(win,events)

pygame.quit()
