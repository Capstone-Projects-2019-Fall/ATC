#!/usr/bin/env python
# from importlib import import_module
# import os
from flask import Flask, render_template, Response


# Raspberry Pi camera module (requires picamera package)
#from camera_pi import Camera

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


"""
def gen(camera):
    """"""Video streaming generator function.""""""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """"""Video streaming route. Put this in the src attribute of an img tag.""""""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
"""


@app.route('/moveleft/')
def moveleft():
    return "left"


@app.route('/moveright/')
def moveright():
    return "right"


@app.route('/moveforward/')
def moveforward():
    return "forward"


@app.route('/movebackward/')
def movedown():
    return "backwards"


"""@app.route('/takepicture/')
def takepicture():
    Camera.capture('/home/pi/Desktop/image.jpg')
    return "success"
"""
if __name__ == '__main__':
    app.run(host='10.0.0.202', threaded=True)
