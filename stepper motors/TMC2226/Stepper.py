
import machine
import utime

steps = 200
microsteps = 64
total_steps =  steps * microsteps

step = machine.Pin(0, machine.Pin.OUT)
direct = machine.Pin(1,  machine.Pin.OUT)

direct.value(1)
step.value(1)
