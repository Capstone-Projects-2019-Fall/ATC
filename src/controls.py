#!/usr/bin/env python3

from nanpy import (ArduinoApi, SerialManager)
from time import sleep

ML1 = 5
ML2 = 4
MR1 = 13
MR2 = 12

EL = 3
ER = 11

try:
    connection = SerialManager()
    a = ArduinoApi(connection = connection)
    print("connected!")
except:
    print("Failed to connect to Arduino")

# setup the pinModes as if we were in the Arduino IDE
a.pinMode(ER, a.OUTPUT)
a.pinMode(EL, a.OUTPUT)
a.pinMode(ML1, a.OUTPUT)
a.pinMode(ML2, a.OUTPUT)
a.pinMode(MR1, a.OUTPUT)
a.pinMode(MR2, a.OUTPUT)

try:
    while True:
        a.digitalWrite(ML1, a.HIGH)
        a.digitalWrite(ML2, a.LOW)
        a.digitalWrite(MR1, a.HIGH)
        a.digitalWrite(MR2, a.LOW)
        a.analogWrite(EL, 80)
        a.analogWrite(ER, 255)
except:
    a.digitalWrite(ML1, a.LOW)    # cut off voltage to these pins if something went wrong
    a.digitalWrite(MR1, a.LOW)    # cut off voltage to these pins if something went wrong
