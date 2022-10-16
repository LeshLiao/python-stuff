try:
    import RPi.GPIO as GPIO
    import time
except RuntimeError:
    print("import failed!")
LED_PIN = 17

def setup():
    #GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)#GPIO.BOARD GPIO編號或Port Pin編號
    GPIO.setup(LED_PIN , GPIO.OUT)
    GPIO.output(LED_PIN , 0)
def blink():
    GPIO.output(LED_PIN , 1)
    time.sleep(0.01)
    GPIO.output(LED_PIN , 0)
    time.sleep(0.01)
if __name__ == '__main__':
    try:
        setup()
        while True:
            blink()
    except:
        print("some error")
    finally:
        print("clean up")
        GPIO.cleanup() # cleanup all GPIO
