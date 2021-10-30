import board
import keypad

km = keypad.KeyMatrix(
    row_pins=(board.GP10, board.GP11, board.GP12, board.GP13, board.GP14),
    column_pins=(board.GP19, board.GP18, board.GP17, board.GP16, board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9,),
)

while True:
  event = km.events.get()
  if event:
    print(event)
