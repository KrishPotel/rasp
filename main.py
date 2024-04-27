import gpio

gpio.setup(21,gpio.OUT)

while True:
    gpio.output(21,gpio.HIGH)