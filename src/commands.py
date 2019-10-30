import RPi.GPIO as gpio
import time

def config():
    print("initializing...")
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)    


def main():
    print("Going forward!")
    forward(4)
    print("Going backwards!")
    backwards(2)


def forward(time_s):
    config()
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, True)
    gpio.output(24, False)      
    time.sleep(time_s)
    gpio.cleanup()

def backwards(time_s):
    config()
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, False)
    gpio.output(24, True)
    time.sleep(time_s)
    gpio.cleanup()
    
if __name__ == '__main__':
    main()
