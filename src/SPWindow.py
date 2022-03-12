# The window is where everything is drawn and where everything is connected to

from pyglet import clock, window
from .import SPInputHandler as IH
from .SPObject import SPObject


class SPWindow(window.Window):

    # Pre: Passed a width and height > 0 and the windows title
    # Post: Create a pyglet window with the passed params
    # Descr: Create a new window
    def __init__(self, width: int = 0, height: int = 0, title: str = None) -> None:
        # Call the super constructor -> pyglet.window.Window
        super(SPWindow, self).__init__(width, height, title, vsync=False)
        
        # Set up the controls, including a controller if applicable
        self.attachHandlers()
        # Clock to call drawFrame 60 times a second
        clock.schedule_interval(self.gameLoop, 1 / 60.0)

    # Pre: The calling object has been instatiated correctly
    # Post: Event Handlers are setup for the window/game
    # Descr: Set the event handlers with the funcs from SPInputHandler.py
    def attachHandlers(self) -> None:
        self.on_key_press = IH.on_key_press
        self.on_key_release = IH.on_key_release

    # Pre: Passed an object with a location
    # Post: Calls the objects off<Direction> and returns flag
    # Descr: Check if the object is off the screen at all
    def checkOffScreen(self, obj: SPObject) -> bool:

        # Makes sure the entire obj is off the screen
        if obj.x< 0:
            obj.offLeft()
            offscreen = True
        elif obj.x + obj.width > self.width:
            obj.offRight(self.width)
            offscreen = True
        # Makes sure the entire obj is off the screen
        elif obj.y < 0:
            obj.offBottom()
            offscreen = True
        elif obj.y + obj.height > self.height:
            obj.offTop(self.height)
            offscreen = True


    def gameLoop(self, dt: float) -> None:
        # Logging for perf
        if(dt > 0.018):
            print("Tick took too long -> {}".format(dt))

        # Clear the screen
        self.clear()
        # Iterate over all the objects and draw them
        for obj in SPObject.ALL_OBJS:
            # Check object of key focus and add inputs
            if obj.has_focus:
                obj.checkKeys(IH.directions_pushed)
            obj.update()  # Update objects location
            self.checkOffScreen(obj)  # Check if the object is off the screen now 
            obj.draw()  # Draw then object to the screen
        # Check for any collisions
        SPObject.checkCollisions()
            
