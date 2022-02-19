from StartWindow import StartWindow
from constant import PURPLE
from windows.GameWindow import GameWindow
from windows.WinWindow import WinWindow

class Navigation(object):
    def __init__(self):

        self.current_window = "START_WINDOW"

        self.props=None
        

        self.windows= {
            "GAME_WINDOW" :GameWindow(),
             "START_WINDOW" : StartWindow(),
             "WIN_WINDOW" : WinWindow()
        }

    def render(self,win,events):

        self.windows[self.current_window].render(win,events,self.navigate,self.props)
        

    def navigate(self,destination_window,props=None):
        
        self.current_window= destination_window
        self.props=props



