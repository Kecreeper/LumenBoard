import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler

from adafruit_mcp230xx.mcp23017 import MCP23017
i2c = busio.I2C(board.GP27, board.GP26)
mcp = MCP23017(i2c)
encoder_handler = EncoderHandler()
encoder_handler.pins = (
    # left encoder
    (board.GP0,  board.GP1, None),
    # right encoder
    (board.GP14, board.GP15, None)
)

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.modules.append(encoder_handler)
keyboard.extensions.append(MediaKeys())



keyboard.col_pins = (mcp.get_pin(0), mcp.get_pin(1), board.GP2, board.GP3, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP13)
keyboard.row_pins = (mcp.get_pin(2), mcp.get_pin(3), mcp.get_pin(4), mcp.get_pin(5), mcp.get_pin(6), mcp.get_pin(7))
keyboard.diode_orientation = DiodeOrientation.COL2ROW

RGBKEY = KC.TRNS # temporary
FN1 = KC.MO(1)
FN2 = KC.MO(1)   # temporary

keyboard.keymap = [
#   Layer 0
#       0         1         2        3       4       5        6       7       8         9       10        11        12        13        14        15        16        17

    [
        KC.ESC,   KC.TRNS,  KC.F1,   KC.F2,  KC.F3,  KC.F4,   KC.F5,  KC.F6,  KC.F7,    KC.F8,  KC.F9,    KC.F10,   KC.F11,   KC.F12,   RGBKEY,   KC.TRNS,  KC.TRNS,  KC.TRNS,
        KC.GRVE,  KC.N1,    KC.N2,   KC.N3,  KC.N4,  KC.N5,   KC.N6,  KC.N7,  KC.N8,    KC.N9,  KC.N0,    KC.MINS,  KC.EQL,   KC.BSPC,  KC.HOME,  KC.NO,    KC.TRNS,  KC.NO,
        KC.TAB,   KC.Q,     KC.W,    KC.E,   KC.R,   KC.T,    KC.Y,   KC.U,   KC.I,     KC.O,   KC.P,     KC.LBRC,  KC.RBRC,  KC.BSLS,  KC.END,   KC.TRNS,  KC.TRNS,  KC.TRNS,  
        KC.CAPS,  KC.A,     KC.S,    KC.D,   KC.F,   KC.G,    KC.H,   KC.J,   KC.K,     KC.L,   KC.SCLN,  KC.QUOT,  KC.ENT,   KC.NO,    KC.PGUP,  KC.NO,    KC.TRNS,  KC.NO,
        KC.LSFT,  KC.Z,     KC.X,    KC.C,   KC.V,   KC.B,    KC.N,   KC.M,   KC.COMM,  KC.DOT, KC.SLSH,  KC.RSFT,  KC.UP,    KC.NO,    KC.PGDN,  KC.NO,    KC.NO,    KC.NO,
        KC.LCTL,  KC.LWIN,  KC.LALT, KC.NO,  KC.NO,  KC.SPC,  KC.NO,  KC.NO,  KC.RALT,  FN1,    FN2,      KC.LEFT,  KC.DOWN,  KC.NO,    KC.RIGHT, KC.TRNS,  KC.TRNS,  KC.TRNS,
   ],
#  Layer 1
#       0         1         2         3         4         5         6         7         8         9         10        11        12        13        14        15        16        17
   [
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.DEL,   KC.TRNS,  KC.NO,    KC.TRNS,  KC.NO,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.NO,    KC.TRNS,  KC.NO,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.NO,    KC.NO,    KC.NO,
        KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.NO,    KC.NO,    KC.TRNS,  KC.NO,    KC.NO,    KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,  KC.TRNS,
   ]
]

if __name__ == '__main__':
    keyboard.go()