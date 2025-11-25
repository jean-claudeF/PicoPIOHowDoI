from rp2 import PIO, StateMachine, asm_pio
from machine import Pin

f = 10_000
pin_out = Pin(15)

@asm_pio(set_init = PIO.OUT_LOW)
def pwm1():
                               # Cycles:     Output
    set(pins, 0)               # 1            0   during 2 / 3 / 4 / 5 cycles 
    #nop()                      # 1
    #nop()    [1]               # 2
    
    set(x, 2)                   # 1           
                                #---------------
    label("start_loop")          # 0 
    set(pins, 1)                 # 1          1  during (x+1) * 2 cycles
    jmp(x_dec, "start_loop")     # 1         
    
    
sm = StateMachine(1, pwm1, freq= f, set_base = pin_out)
sm.active(1)