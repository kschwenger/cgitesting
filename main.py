#!/usr/bin/python37all
# CGI script to show the state of a single GPIO input pin
# Save file as /usr/lib/cgi-bin/gpio_read.py
import RPi.GPIO as GPIO
pin = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)
print('Content-type:text/html\n\n')
print('<html><body><font color="red">')
print("Howdly!")"
print('</body> </html>')