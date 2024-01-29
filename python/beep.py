import RPi.GPIO as GPIO
import time

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BOARD)

# Define GPIO pin for the LED
led_pin = 3

# Set up LED pin as output
GPIO.setup(led_pin, GPIO.OUT)

# Define the beats pattern (1 for beat, 0 for rest)
beats = [1, 0, 1, 0, 1, 1, 0, 1]  # Example beat pattern

try:
    while True:
        for beat in beats:
            if beat == 1:
                GPIO.output(led_pin, GPIO.HIGH)  # Beat ON
                print("Beat ON")
                time.sleep(0.2)  # Duration of the beat
            else:
                GPIO.output(led_pin, GPIO.LOW)  # Rest (LED OFF)
                print("Rest")
                time.sleep(0.2)  # Duration of the rest

except KeyboardInterrupt:
    pass

# Clean up GPIO
GPIO.cleanup()
