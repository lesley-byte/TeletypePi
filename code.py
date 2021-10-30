import os
import board
import time
import keypad
import usb_hid
import adafruit_hid  # Imported but unused...maybe will use it someday...idk
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
kbd = Keyboard(usb_hid.devices)
kbd_layout = KeyboardLayoutUS(keyboard)
keyboard_layout = KeyboardLayoutUS(keyboard)
keys = keypad.KeyMatrix(
    row_pins=(board.GP10, board.GP11, board.GP12, board.GP13, board.GP14),
    column_pins=(board.GP19, board.GP18, board.GP17, board.GP16, board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9,),
)
keycode_LUT = [  # The addresses that the microcontroller gives to the keys.
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
    14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
    28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
    43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
    62,
]
keymap1 = {  # The assignment of keyboard values to the addresses above
    (0): (1, ""), #shifts to keymap2
    (1): (0, "My Name Layer1"),
    (2): (0, "Is "),
    (3): (0, "Layer1 "),
    (4): (0, Keycode.FIVE),
    (5): (0, Keycode.SIX),
    (6): (0, Keycode.SEVEN),
    (7): (0, Keycode.EIGHT),
    (8): (0, (Keycode.CONTROL, Keycode.A)),
    (9): (0, Keycode.ZERO),
}

keymap2 = {  # The assignment of keyboard values to the addresses above
    (0): (3, ""), # Shifts back to keymap1
    (1): (0, "My Name is Layer2"),
    (2): (0, "Is "),
    (3): (0, "Layer 2 "),
    (4): (0, Keycode.FIVE),
    (5): (0, Keycode.SIX),
    (6): (0, Keycode.SEVEN),
    (7): (0, Keycode.EIGHT),
    (8): (0, (Keycode.CONTROL, Keycode.A)),
    (9): (0, Keycode.ZERO),
}
shift_mod = False
ctrl_mod = False  
keymap = keymap1


while True:

    key_event = keys.events.get()
    if key_event:
        if key_event.pressed:
            if keymap[keycode_LUT.index(key_event.key_number)][0] == 1:
                shift_mod = True
                keymap = keymap2
            elif keymap[keycode_LUT.index(key_event.key_number)][0] == 2:
                ctrl_mod = True
            elif keymap[keycode_LUT.index(key_event.key_number)][0] == 3:
                shift_mod = False
                keymap = keymap1
            if shift_mod is False and ctrl_mod is False:
                # kbd.press(keymap[keycode_LUT.index(key_event.key_number)][1])
                if isinstance((keymap[keycode_LUT.index(key_event.key_number)][1]), str):  # If it's a string...
                    keyboard_layout.write((keymap[keycode_LUT.index(key_event.key_number)][1]))  # ...Print the string
                    
                elif isinstance((keymap[keycode_LUT.index(key_event.key_number)][1]), int):  # If its a single key
                    keyboard.press((keymap[keycode_LUT.index(key_event.key_number)][1]))  # "Press"...
                    keyboard.release_all()  # ..."Release"!
                elif isinstance((keymap[keycode_LUT.index(key_event.key_number)][1]), (list, tuple)):  # If its multiple keys
                    keyboard.press(*(keymap[keycode_LUT.index(key_event.key_number)][1]))  # "Press"...
                    keyboard.release_all()  # ..."Release"
            elif shift_mod is True and ctrl_mod is False:
                # kbd.press(Keycode.SHIFT, keymap[keycode_LUT.index(key_event.key_number)][1])
                
                if isinstance((keymap[keycode_LUT.index(key_event.key_number)][1]), str):  # If it's a string...
                    keyboard_layout.write(keymap[keycode_LUT.index(key_event.key_number)][1]) # ...Print the string
                elif isinstance((keymap[keycode_LUT.index(key_event.key_number)][1]), int):  # If its a single key
                    keyboard.press((keymap[keycode_LUT.index(key_event.key_number)][1]))  # "Press"...
                    keyboard.release_all()  # ..."Release"!
                    
                elif isinstance((keymap[keycode_LUT.index(key_event.key_number)][1]), (list, tuple)):  # If its multiple keys
                    keyboard.press(*(keymap[keycode_LUT.index(key_event.key_number)][1]))  # "Press"...
                    keyboard.release_all()  # ..."Release"
                    
                print(keymap[keycode_LUT.index(key_event.key_number)][1])
            elif shift_mod is False and ctrl_mod is True:
                # kbd.press(Keycode.CONTROL, keymap[keycode_LUT.index(key_event.key_number)][1])
                if isinstance((keymap[keycode_LUT.index(key_event.key_number)][1]), str):  # If it's a string...
                    keyboard_layout.write(Keycode.CONTROL, (keymap[keycode_LUT.index(key_event.key_number)][1]))  # ...Print the string
                elif isinstance((keymap[keycode_LUT.index(key_event.key_number)][1]), int):  # If its a single key
                    keyboard.press(Keycode.CONTROL, (keymap[keycode_LUT.index(key_event.key_number)][1]))  # "Press"...
                    keyboard.release_all()  # ..."Release"!
                elif isinstance((keymap[keycode_LUT.index(key_event.key_number)][1]), (list, tuple)):  # If its multiple keys
                    keyboard.press(*(keymap[keycode_LUT.index(key_event.key_number)][1]))  # "Press"...
                    keyboard.release_all()  # ..."Release"
                print(keymap[keycode_LUT.index(key_event.key_number)][1])
            elif shift_mod is True and ctrl_mod is True:
                """kbd.press(
                          Keycode.SHIFT,
                          Keycode.CONTROL,
                          keymap[keycode_LUT.index(key_event.key_number)][1]
                          )"""
                print(keymap[keycode_LUT.index(key_event.key_number)][1])

        if key_event.released:
            if keymap[keycode_LUT.index(key_event.key_number)][0] == 1:  # un-shift
                shift_mod = False
                keymap = keymap1
            elif keymap[keycode_LUT.index(key_event.key_number)][0] == 2:  # un-ctrl
                ctrl_mod = False
                keymap = keymap1
                time.sleep(0.1)
                print(keymap[keycode_LUT.index(key_event.key_number)][1])
                kbd.release_all()
