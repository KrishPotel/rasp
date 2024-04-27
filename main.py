import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

red = 5
GPIO.setup(red, GPIO.OUT)
while True:
    GPIO.output(red, GPIO. HIGH)