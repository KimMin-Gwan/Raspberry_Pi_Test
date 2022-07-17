import RPi.GPIO as GPIO
import time
pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)

p = GPIO.PWM(pin,50)
p.start(0)

try:
        while True:
                time.sleep(2)
                p.ChangeDutyCycle(2)
                time.sleep(2)
                p.ChangeDutyCycle(12)
                time.sleep(2)
except KeyboardInterrupt:
        p.stop()
        
GPIO.cleanup()
