from adafruit_circuitplayground import cp
import time
import random 

while True:
    Brightness = random.triangular(0.2, 0.4)
    cp.pixels.brightness = Brightness
    cp.pixels.fill((215, 235, 8))
    time.sleep(0.010)