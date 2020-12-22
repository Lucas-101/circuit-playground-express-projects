from adafruit_circuitplayground import cp
import time
import random 

is_on = False

while True:
     if cp.button_a:
       is_on = True

        pass
    elif cp.button_b:
        
        is_on = False

        pass


while is_on:
    Brightness = random.triangular(0.2, 0.4)
    cp.pixels.brightness = Brightness
    cp.pixels.fill((215, 235, 8))
    time.sleep(0.010)