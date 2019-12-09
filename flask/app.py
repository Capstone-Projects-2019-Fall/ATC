#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response
import multiprocessing
from time import sleep
# import serial
# ser = serial.Serial('/dev/ttyACM0', 9600)
# all_processes = []

# Raspberry Pi camera module (requires picamera package)
#from camera_pi import Camera

app = Flask(__name__)

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/moveleft/')
def moveleft():
    if len(all_processes) > 0:
        for process in all_processes:
            process.terminate()
            print("Process is alive status: ", process.is_alive())
        all_processes.clear()
    t1 = multiprocessing.Process(target=send_inputs, args=(5,))
    print("starting a new process")
    t1.start()
    all_processes.append(t1)     


@app.route('/moveright/')
def moveright():
    if len(all_processes) > 0:
        for process in all_processes:
            process.terminate()
            print("Process is alive status: ", process.is_alive())
        all_processes.clear()
    t1 = multiprocessing.Process(target=send_inputs, args=(4,))
    print("starting a new process")
    t1.start()
    all_processes.append(t1)    


@app.route('/moveforward/')
def moveforward():
    if len(all_processes) > 0:
        for process in all_processes:
            process.terminate()
            print("Process is alive status: ", process.is_alive())
        all_processes.clear()
    t1 = multiprocessing.Process(target=send_inputs, args=(6,))
    print("starting a new process")
    t1.start()
    all_processes.append(t1)         


@app.route('/movebackward/')
def movedown():
    if len(all_processes) > 0:
        for process in all_processes:
            process.terminate()
            print("Process is alive status: ", process.is_alive())
        all_processes.clear()
    t1 = multiprocessing.Process(target=send_inputs, args=(7,))
    print("starting a new process")
    t1.start()
    all_processes.append(t1)      


@app.route('/stop/')
def stop():
    if len(all_processes) > 0:
        for process in all_processes:
            process.terminate()
            print("Process is alive status: ", process.is_alive())                    
        all_processes.clear()
    t1 = multiprocessing.Process(target=send_inputs, args=(0,))
    print("starting a new process")            
    t1.start()
    all_processes.append(t1)            

@app.route('/takepicture/')
def takepicture():
    # Camera.capture('/home/pi/Desktop/image.jpg')
    return "success"

@app.route('/autopilot/')
def autopilot():
    return "success"

@app.route('/photos/')
def photos():
    return render_template('photos.html')

def send_inputs(number):
    while True:
        if number == 4:
            ser.write(b'4')
            sleep(0.1)
        elif number == 5:
            ser.write(b'5')
            sleep(0.1)            
        elif number == 6:
            ser.write(b'6')
            sleep(0.1)            
        elif number == 7:
            ser.write(b'7')
            sleep(0.1)            
        elif number == 0:
            ser.write(b'0')
            sleep(0.1)            


if __name__ == '__main__':
    app.run(host='127.0.0.1', threaded=True)
