import RPi.GPIO as GPIO
import time

# blinking function
def blink(pin):
    print(str(pin)+"High")
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(0.1)
    print(str(pin)+"Low")
    GPIO.output(pin,GPIO.LOW)
    time.sleep(2)
    return

def one_sound(pin, s):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(s)
    GPIO.output(pin,GPIO.LOW)

pin_number = 37

# to use Raspberry Pi board pin numbers (1~40)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_number, GPIO.OUT)


if __name__ == '__main__':

    try:
        #for i in range(0,50):
        #    blink(pin_number)
        one_sound(pin_number, 0.1)
    finally:
        GPIO.cleanup()
