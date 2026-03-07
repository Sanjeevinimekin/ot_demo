from gpiozero import LED
from time import sleep

VERSION = "1.0"

led = LED(17)

print(f"Running Version {VERSION}")

while True:
    led.on()
    sleep(5)
    led.off()
    sleep(5) 
