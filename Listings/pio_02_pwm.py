# pio_02_pwm.py     PWM
from rp2 import PIO, StateMachine, asm_pio
from machine import Pin

f = 1_000_000



@asm_pio(set_init = PIO.OUT_LOW)
def pwm1():
    set(pins, 1)  
    set(pins, 0)   [8]
   
sm = StateMachine(3, pwm1, freq= 10 * f, set_base = Pin(15))
sm.active(1)

