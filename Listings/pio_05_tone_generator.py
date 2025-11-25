#pio_05_tone_generator.py
from rp2 import PIO, StateMachine, asm_pio
from machine import Pin

pin_out = [Pin(16), Pin(17), Pin(18), Pin(19), Pin(20), Pin(21), Pin(22), Pin(26)]

@asm_pio(set_init = PIO.OUT_LOW)
def rectgen():                            # 1 period = 100 cycles
    set(pins, 0)   [29]     # 30 cycles
    nop()          [19]     # 20 cycles
    set(pins, 1)   [29]     # 30 cycles
    nop()          [19]     # 20 cycles


def tone(f, index):
    print(f, "Hz")
    sm = StateMachine(index,rectgen,freq= int(100* f),set_base = pin_out[index])
    sm.active(1)
    
tone(880, 0)
tone(440.1, 1)
tone(439.8, 2)
tone(439.5, 3)
tone(220.2, 4)
tone(330.5, 5)
tone(111, 6)
tone(110, 7)
