# pio_03_hfrect.py
from rp2 import PIO, StateMachine, asm_pio
from machine import Pin

pin_out = Pin(15)

@asm_pio(set_init = PIO.OUT_LOW)
def rectgen():
    set(pins, 0)
    set(pins, 1)

while True:
    freq = input("Frequency/kHz (1 ... 62250): ")
    if not freq:
        break
    
    f = int(float(freq) * 1000)
    print(f, "Hz")
    
    sm = StateMachine(0, rectgen, freq= 2* f, set_base = pin_out)
    sm.active(1)
    
sm.active(0)           # Comment this out if sm should continue running
sm = None