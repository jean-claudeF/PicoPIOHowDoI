# pio_06_blink   1Hz
from rp2 import PIO, StateMachine, asm_pio
from machine import Pin
import time

led = Pin(25, Pin.OUT)       # internal LED
f = 1                        # in Hz

@asm_pio(set_init = PIO.OUT_LOW)
def blink():
    
    # half period with 1          1000 cycles:
    set(pins, 1)                  # 1 
    set(x, 31)      [6]           # 1 + 6
    label("delay_1")
    nop()           [29]          # (1+29) 
    jmp(x_dec, "delay_1")         #  1      = 31, * (31+1)
    
    # half period with 0          1000 cycles
    set(pins, 0)
    set(x, 31)      [6]
    label("delay_0")
    nop()           [29]
    jmp(x_dec, "delay_0")
    
    
sm = StateMachine(1, blink, freq= 2000*f, set_base = led)
sm.active(1)
