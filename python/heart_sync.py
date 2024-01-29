import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BOARD)

# Set the GPIO pin to output mode
led_pin = 3
GPIO.setup(led_pin, GPIO.OUT)

# Define the number of steps and duration for the fade in/out effect
num_steps = 50
fade_duration = 0.5 / num_steps  # Total duration divided by number of steps

try:
    while True:
        # Fade in
        for i in range(num_steps):
            brightness = i / num_steps
            GPIO.output(led_pin, True)  # Turn on the LED
            time.sleep(fade_duration)  # Wait for the fade duration
            GPIO.output(led_pin, False)  # Turn off the LED
            time.sleep(fade_duration * (1 - brightness))  # Adjust the off time based on brightness

        # Fade out
        for i in range(num_steps, 0, -1):
            brightness = i / num_steps
            GPIO.output(led_pin, True)  # Turn on the LED
            time.sleep(fade_duration)  # Wait for the fade duration
            GPIO.output(led_pin, False)  # Turn off the LED
            time.sleep(fade_duration * (1 - brightness))  # Adjust the off time based on brightness

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt
    GPIO.cleanup()
