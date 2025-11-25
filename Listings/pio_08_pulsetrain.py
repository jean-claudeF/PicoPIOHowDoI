#pio_08_pulsetrain.py
import time
from rp2 import PIO, StateMachine, asm_pio
from machine import Pin

out_pin = 15
f = 1000
n = 6

@asm_pio(set_init=PIO.OUT_LOW, in_shiftdir=PIO.SHIFT_RIGHT)
def _pulses():
    pull(block)              #   wait for input from system to OSR
    mov(x, osr)              #   count from OSR to X
    
    label("next")            #   loop = 10 cycles
    set(pins, 1)         [4] #   5 cycles
    set(pins, 0)         [3] #   4 cycles
    jmp(x_dec, "next")       #   1 cycle

def pulsetrain(f, nb):
    sm = StateMachine(0, _pulses, freq=f*10,  set_base=Pin(out_pin))
    sm.active(1)
    sm.put(n - 1)
    return sm
        
def wait_switch_off(sm, f, n):
    waittime = (1/f)*n + 0.01 
    time.sleep(waittime)
    sm.active(0)
    print("READY")

sm = pulsetrain(f, n)
wait_switch_off(sm, f, n)

