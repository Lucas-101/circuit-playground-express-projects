from adafruit_circuitplayground import cp

Brightness = 1
cp.pixels.brightness = Brightness

while True:
    if cp.button_a:
        cp.pixels.fill((255, 255, 255))

        pass
    elif cp.button_b:
        cp.pixels.fill((0, 0, 0))

        pass
