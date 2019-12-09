import tornado.ioloop
import tornado.web
import socket 
import io
import picamera
import logging
import socketserver
from threading import Condition
from http import server


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class PhotoHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("photos.html")

class LeftActionHandler(tornado.web.RequestHandler):
    def get(self):
        print("Left button click")
     
   
class RightActionHandler(tornado.web.RequestHandler):
    def get(self):
        print("Right button click")


class ForwardActionHandler(tornado.web.RequestHandler):
    def get(self):
        print("Up button click")


class BackwardActionHandler(tornado.web.RequestHandler):
    def get(self):
        print("Down button click")