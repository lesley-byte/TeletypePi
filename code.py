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
    (1): (0, "2"),
    (2): (0, "3"),
    (3): (0, "4"),
    (4): (0, "5"),
    (5): (0, "6"),
    (6): (0, "7"),
    (7): (0, "8"),
    (8): (0, "9"),
    (9): (0, "0"),
    (10): (0, ":"),
    (11): (0, Keycode.KEYPAD_MINUS),
    (12): (0, "HERE IS"),
    (13): (0, Keycode.ESCAPE),
    (14): (0, "Q"),
    (15): (0, "W"),
    (16): (0, "E"),
    (17): (0, "R"),
    (18): (0, "T"),
    (19): (0, "Y"),
    (20): (0, "U"),
    (21): (0, "I"),
    (22): (0, "O"),
    (23): (0, "P"),
    (24): (0, "LINE FEED"),
    (25): (0, "RETURN"),
    (26): (0, "REAL CONTROL BUTTON"),
    (27): (0, "A"),
    (28): (0, "S"),
    (29): (0, "D"),
    (30): (0, "F"),
    (31): (0, "G"),
    (32): (0, "H"),
    (33): (0, "J"),
    (34): (0, "K"),
    (35): (0, "L"),
    (36): (0, ":"),
    (37): (0, "RUB OUT"),
    (38): (0, "REPT"),
    (39): (0, "BREAK"),
    (40): (0, "REAL SHIFT"),
    (41): (0, "Z"),
    (42): (0, "X"),
    (43): (0, "C"),
    (44): (0, "V"),
    (45): (0, "B"),
    (46): (0, "N"),
    (47): (0, "M"),
    (48): (0, ","),
    (49): (0, "."),
    (50): (0, "/"),
    (51): (0, "REAL SHIFT"),
    (52): (0, Keycode.SPACEBAR),
}

keymap2 = {  # The assignment of keyboard values to the addresses above
    (0): (3, ""), # Shifts back to keymap1
    (1): (0, """\""""),
    (2): (0, "#"),
    (3): (0, "$"),
    (4): (0, "%"),
    (5): (0, "&"),
    (6): (0, Keycode.QUOTE),
    (7): (0, "("),
    (8): (0, ")"),
    (9): (0, "SP"),
    (10): (0, "*"),
    (11): (0, Keycode.EQUALS),
    (12): (0, "HERE IS"),
    (13): (0, Keycode.ESCAPE),
    (14): (0, "X-ON"),
    (15): (0, "W"),
    (16): (0, "E"),
    (17): (0, "R"),
    (18): (0, "T"),
    (19): (0, "Y"),
    (20): (0, "U"),
    (21): (0, "I"),
    (22): (0, "LEFT ARROW"),
    (23): (0, "@"),
    (24): (0, "LINE FEED"),
    (25): (0, "RETURN"),
    (26): (0, "REAL CONTROL BUTTON"),
    (27): (0, "A"),
    (28): (0, "X-OFF"),
    (29): (0, "D"),
    (30): (0, "F"),
    (31): (0, "BELL"),
    (32): (0, "H"),
    (33): (0, "J"),
    (34): (0, "["),
    (35): (0, Keycode.BACKSLASH),
    (36): (0, "+"),
    (37): (0, "RUB OUT"),
    (38): (0, "REPT"),
    (39): (0, "BREAK"),
    (40): (0, "REAL SHIFT"),
    (41): (0, "Z"),
    (42): (0, "X"),
    (43): (0, "C"),
    (44): (0, "V"),
    (45): (0, "B"),
    (46): (0, "UP ARROW"),
    (47): (0, "]"),
    (48): (0, "<"),
    (49): (0, ">"),
    (50): (0, "?"),
    (51): (0, "REAL SHIFT"),
    (52): (0, Keycode.SPACEBAR),
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
                # somewhere here i need to unshift maybe?
                        
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
                print(keymap[keycode_LUT.index(key_event.key_number)][1])
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
                   0       )"""
                print(keymap[keycode_LUT.index(key_event.key_number)][1])

        if key_event.released: 
            print("i'm actually registering a release")
            #if keymap[keycode_LUT.index(key_event.key_number)][0] == 1:  # un-shift
            if (key_event.key_number) == 1:  # un-shift# un-shift  *******************you have to ask it about key_event.key_number if you want to ask if a specific key was released!!!!
                shift_mod = False
                keymap = keymap1
                print("im actually registering an un-shift")
                print(key_event)
                print(key_event.key_number)
            elif keymap[keycode_LUT.index(key_event.key_number)][0] == 2:  # un-ctrl
                ctrl_mod = False
                keymap = keymap1
                time.sleep(0.1)
                print(keymap[keycode_LUT.index(key_event.key_number)][1])
                kbd.release_all()
