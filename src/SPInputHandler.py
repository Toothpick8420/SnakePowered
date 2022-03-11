# SPInputHandler handles all the input from the user
# It is just a collection of functions that serve as event handlers

from pyglet.window import key


# A list of the directions pressed for movement
directions_pushed: list[str] = []


# Keyboard input handling
valid_keys = [key.W, key.A, key.S, key.D]


def on_key_press(symbol: key, modifier: key) -> None:
    # Check if its a key press that matters
    if symbol in valid_keys:
        directions_pushed.append(symbol)


def on_key_release(symbol: key, modifers: key) -> None:
    # If the keypress is in directions pushed remove it
    if symbol in directions_pushed:
        directions_pushed.remove(symbol)
