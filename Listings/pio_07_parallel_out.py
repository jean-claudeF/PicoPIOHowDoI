# pio_07_parallel_out.py
from rp2 import PIO, StateMachine, asm_pio
from machine import Pin
from time import sleep_us

         
pin_out = Pin(8)         # Here: pins 8...15

@asm_pio(out_init = (PIO.OUT_LOW,) * 8, out_shiftdir = PIO.SHIFT_RIGHT)
def parallel_out():
    pull()
    out(pins, 8)
    

sm = StateMachine(0, parallel_out, freq = 125_000_000, out_base = pin_out)
sm.active(1)

while True:
    for i in range(255):
        sm.put(i)
        sleep_us(10)
