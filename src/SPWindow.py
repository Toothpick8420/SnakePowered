# The window is where everything is drawn and where everything is connected to
import pyglet
from . import SPInputHandler

class SPWindow(pyglet.window.Window):

    # Pre: Passed a width and height > 0 and the windows title
    # Post: Create a pyglet window with the passed params 
    # Descr: Create a new window
    def __init__(self, width: int = 0, height: int = 0, title: str = None) -> None:
        # Call the super constructor -> pyglet.window.Window 
        super(SPWindow, self).__init__(width ,height, title) 
        # Set up the controls, including a controller if applicable
        # FIXME: Add controller support
        self.attachHandlers()

    # Pre: The calling object has been instatiated correctly
    # Post: Event Handlers are setup for the window/game
    # Descr: Set the event handlers with the funcs from SPInputHandler.py
    def attachHandlers(self) -> None:   
        self.on_key_press = SPInputHandler.on_key_press
        self.on_key_release = SPInputHandler.on_key_release