import RPi.GPIO as GPIO
import time

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BOARD)

# Define GPIO pin for the LED
led_pin = 3

# Set up LED pin as output
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        # Turn LED on
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED ON")
        time.sleep(1)
        
        # Turn LED off
        GPIO.output(led_pin, GPIO.LOW)
        print("LED OFF")
        time.sleep(1)

except KeyboardInterrupt:
    pass

# Clean up GPIO
GPIO.cleanup()
