# The window is where everything is drawn and where everything is connected to

from pyglet import clock, window
from .import SPInputHandler
from .SPObject import SPObject


class SPWindow(window.Window):

    # Pre: Passed a width and height > 0 and the windows title
    # Post: Create a pyglet window with the passed params
    # Descr: Create a new window
    def __init__(self, width: int = 0, height: int = 0, title: str = None) -> None:
        # Call the super constructor -> pyglet.window.Window
        super(SPWindow, self).__init__(width, height, title)
        # Set up the controls, including a controller if applicable
        self.attachHandlers()
        # Clock to call drawFrame 60 times a second
        clock.schedule_interval(self.drawFrame, 1 / 60.0)

    # Pre: The calling object has been instatiated correctly
    # Post: Event Handlers are setup for the window/game
    # Descr: Set the event handlers with the funcs from SPInputHandler.py
    def attachHandlers(self) -> None:
        self.on_key_press = SPInputHandler.on_key_press
        self.on_key_release = SPInputHandler.on_key_release

    # Pre: Passed an object with a location
    # Post: Calls the objects off<Direction> and returns flag
    # Descr: Check if the object is off the screen at all
    def checkOffScreen(self, obj: SPObject) -> bool:

        # Makes sure the entire obj is off the screen
        if obj.x< 0:
            obj.offLeft()
            offscreen = True
        elif obj.x + obj.width > self.width:
            obj.offRight()
            offscreen = True
        # Makes sure the entire obj is off the screen
        elif obj.y < 0:
            obj.offBottom()
            offscreen = True
        elif obj.y + obj.height > self.height:
            obj.offTop()
            offscreen = True


    # Pre: None
    # Post: All objects are drawn to the screen
    # Descr: Called 60 times a second to draw all the objects to the screen
    def drawFrame(self, dt: float) -> None:
        self.clear()
        # Iterate over all created objects
        for obj in SPObject.ALL_OBJS:
            self.checkOffScreen(obj)
            obj.draw()
