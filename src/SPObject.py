# All objects in the game should be created with this object or extend it

from pyglet import clock, image, sprite, window
from . import SPInputHandler as IH


class SPObject(sprite.Sprite):

    ALL_OBJS = []  # A list to store all created objects

    def __init__(
        self,
        file_path: str,
        x_loc: float = 0,
        y_loc: float = 0,
        has_focus: bool = False,
    ) -> None:
        # Call the super constructor with the created sprite
        sprite: image.AbstractImage = image.load(file_path)
        super(SPObject, self).__init__(sprite, x_loc, y_loc)
        # Object velocity
        self.x_vel: float = 0
        self.y_vel: float = 0
        self.mvmt_spd: float = 5
        # Keyboard focus for movement
        self.has_focus = has_focus
        # Add the created object to the list of objects
        SPObject.ALL_OBJS.append(self)
        # Schedule the update function to be called every 60 seconds
        clock.schedule_interval(SPObject.tick, 1 / 60.0)

    # Pre: None
    # Post: Object velocity changed to move direction
    # Descr: Update the velocity to move direction
    def accelerateUp(self) -> None:
        self.y_vel = self.mvmt_spd

    def accelerateDown(self) -> None:
        self.y_vel = -(self.mvmt_spd)

    def accelerateRight(self) -> None:
        self.x_vel = self.mvmt_spd

    def accelerateLeft(self) -> None:
        self.x_vel = -(self.mvmt_spd)

    # Pre: Passed object and self have correct hitboxs
    # Post: Returns True if hitboxes overlap
    # Descr: Compares hitboxes of 2 objects to check for collision
    def hasCollided(self, obj) -> bool:
        
        # Right edge of Self to the left edge of obj
        return (
            self.x + self.width > obj.x
            and self.x < obj.x + obj.width
            and self.y < obj.y + obj.height
            and self.y + self.height > obj.y
        )

    # Pre: None
    # Post: All objects location has been updated with velocity
    # Descr: Update the objects location with their velocity
    def tick(dt: float) -> None:
        # Iterate over all objects
        for obj in SPObject.ALL_OBJS:
            # Perform changes based on keyboard input
            if obj.has_focus:
                obj.checkKeys()
            # Get the new location
            new_x: float = obj.x + obj.x_vel
            new_y: float = obj.y + obj.y_vel
            # Update the location
            obj.update(new_x, new_y)

        # Check for collisions after moving
        SPObject.checkCollisions()

    # Pre: None
    # Post: All objects have been checked for collisions
    # Descr: Check for collisions
    def checkCollisions() -> None:
        # Iterate over every object
        for idx, obj in enumerate(SPObject.ALL_OBJS):
            # Compare to every other object
            for idx2, obj2 in enumerate(SPObject.ALL_OBJS):
                # Check if they are the same object
                if idx == idx2:
                    continue
                if obj.hasCollided(obj2):
                    obj.onCollision(obj2)
                    obj2.onCollision(obj)

    # ABSTRACT FUNCTIONS MEANT TO BE OVERLOADED

    # Pre: Objects have collied
    # Post: Action to perform on collision is performed
    # Descr: Performs an function upon colliding -> overload
    def onCollision(self, obj) -> None:
        pass

    # Pre: None
    # Post: Action is performed based on key inputs
    # Descr: Performs an action based on keyboard input
    def checkKeys(self) -> None:
        pass

    # Pre: Object is off<side> of the screen
    # Post: Action is performed due to being off screen
    # Descr: Performs an action upon leaving the screen
    def offTop(self, screen_height: int) -> None:
        pass

    def offBottom(self) -> None:
        pass

    def offRight(self, screen_width: int) -> None:
        pass

    def offLeft(self) -> None:
        pass
