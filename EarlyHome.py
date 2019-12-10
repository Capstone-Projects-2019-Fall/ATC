import tornado.ioloop
import tornado.web
import socket 
import io
#import picamera
import logging
import socketserver
from threading import Condition
from http import server
from nanpy import (ArduinoApi, SerialManager)
from time import sleep

# Arduino Pins
# MR = Motor Right
# ML = Motor Left
# EL = Enable Left
ML1 = 5
ML2 = 4
MR1 = 13
MR2 = 12

EL = 3
ER = 11
state = True

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class PhotoHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("photos.html")