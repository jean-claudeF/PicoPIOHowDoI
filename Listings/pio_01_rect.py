# pio_01.py   
from machine import Pin, freq
from rp2 import PIO, StateMachine, asm_pio
freq(200_000_000) 

f = 100_000_000
pin_out = Pin(15)

@asm_pio(set_init = PIO.OUT_LOW)
def square1():
    set(pins, 1)
    set(pins, 0)
    
sm = StateMachine(0, square1, freq= 2 * f, set_base = pin_out)
sm.active(1)