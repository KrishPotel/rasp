import RPIO

RPIO.setup(21, RPIO.OUT)

# set gpio 21 to high
RPIO.output(21, True)