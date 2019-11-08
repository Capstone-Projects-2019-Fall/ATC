import tornado.ioloop
import tornado.web
import socket 
import io
#import picamera
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


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/photos/", PhotoHandler),
        (r"/moveleft/", LeftActionHandler),
        (r"/moveright/", RightActionHandler),
        (r"/moveforward/", ForwardActionHandler),
        (r"/movebackward/", BackwardActionHandler),

    ])


class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)


class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length' , len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()

class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


if __name__ == "__main__":
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip) 
    except: 
        print("Unable to get Hostname and IP")
    # with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
    #     output = StreamingOutput()
    # #Uncomment the next line to change your Pi's Camera rotation (in degrees)
    #     camera.rotation = 180
    #     camera.start_recording(output, format='mjpeg')
    try:
        port = 8000
        address = ('', port)
        # server = StreamingServer(address, StreamingHandler)
        # server.serve_forever()
        app = make_app()
        app.listen(port)
        print("connect to http://" + host_ip + ":" + str(port))
        print("use CTRL + C to exit")
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        print()
        print("stopping loop and closed port")
        tornado.ioloop.IOLoop.current().stop()
    # finally:
    #     camera.stop_recording()
    
        
    
