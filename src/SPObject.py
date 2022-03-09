# All objects in the game should be created with this object or extend it

import pyglet
from pyglet import clock

class SPObject(pyglet.sprite.Sprite):

    ALL_OBJS = []  # A list to store all created objects

    # TODO: Maybe do a try catch for creating the sprite
    # TODO: Batch sprite rendering
    def __init__(self, file_path: str, x_loc: float, y_loc: float) -> None:
        # Call the super constructor with the created sprite
        sprite: pyglet.image.AbstractImage = pyglet.image.load(file_path)
        super(SPObject, self).__init__(sprite, x_loc, y_loc)
        # Object velocity
        self.x_vel: float = 0
        self.y_vel: float = 0
        # Add the created object to the list of objects
        SPObject.ALL_OBJS.append(self)
        # Schedule the update function to be called every 60 seconds 
        clock.schedule_interval(SPObject.tick, 1/60.)

    
    # FIXME: This might be inefficient 
    # Pre: None
    # Post: All objects location has been updated with velocity
    # Descr: Update the objects location with their velocity
    def tick(dt: float) -> None:
        # Iterate over all objects
        for obj in SPObject.ALL_OBJS:
            # Get the new location
            new_x: float = obj.x + obj.x_vel
            new_y: float = obj.y + obj.y_vel
            # Update the location
            obj.update(new_x, new_y)

