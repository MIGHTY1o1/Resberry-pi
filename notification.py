import time
import random  
import RPi.GPIO as GPIO
from pushover import PushoverClient

# Set up GPIO pin for the LED
led_pin = 3
num_flickers = 3  # Number of flickers

# Set up GPIO pin for the speaker
speaker_pin = 11  # Assuming the speaker is connected to GPIO pin 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(speaker_pin, GPIO.OUT)  # Initialize speaker pin

# Pushover API token and user key
api_token = 'auovf13oue7vcvyvdzsw99sho4ztor'
user_key = 'uzoour449p6msxip2gpizxzk4c1a3i'

# Initialize Pushover client
client = PushoverClient()

# Set API token and user key separately
client.conf['app_key'] = api_token
client.conf['user_key'] = user_key

# Function to blink LED
def blink_led(led_pin, num_flickers=3):
    for _ in range(num_flickers):
        GPIO.output(led_pin, GPIO.HIGH)  # Turn the LED on
        time.sleep(0.1)  # LED on duration
        GPIO.output(led_pin, GPIO.LOW)  # Turn the LED off
        time.sleep(0.1)  # LED off duration

# Function to beep
def beep(speaker_pin, num_beeps=3):
    for _ in range(num_beeps):
        GPIO.output(speaker_pin, GPIO.HIGH)  # Turn the speaker on
        time.sleep(0.1)  # Beep duration
        GPIO.output(speaker_pin, GPIO.LOW)  # Turn the speaker off
        time.sleep(0.1)  # Time between beeps

# Function to handle Pushover notifications
def handle_notification(message):
    print("Notification Received:", message)
    blink_led(led_pin)
    beep(speaker_pin)

# Send a message using Pushover
response = client.send_message("Hello musturd colony!")

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    handle_notification("happy hacking!")

# Clean up GPIO
GPIO.cleanup()
