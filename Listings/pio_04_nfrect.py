#pio4_nf_rect.py      
from rp2 import PIO, StateMachine, asm_pio
from machine import Pin

pin_out = Pin(15)

@asm_pio(set_init = PIO.OUT_LOW)
def rectgen():                            # 1 period = 100 cycles
    set(pins, 0)   [29]     # 30 cycles
    nop()          [19]     # 20 cycles
    set(pins, 1)   [29]     # 30 cycles
    nop()          [19]     # 20 cycles


def stop_sm():
    # Stop sm and set output to 0: 
    print ("Stopped")
    sm.active(0)
    pin_out = Pin(15, Pin.OUT)
    pin_out.value(0)

while True:
    fs = input("Frequency / Hz (20 ... 1.25E6): ")
    
    try:
        f = int(float(fs))
        print(f, "Hz")
        sm = StateMachine(0, rectgen, freq= 100* f, set_base = pin_out)
        sm.active(1)
    except:
        stop_sm()
    if not fs:
        break
