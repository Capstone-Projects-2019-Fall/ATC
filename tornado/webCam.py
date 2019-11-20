# Web streaming example
# Source code from the official PiCamera package
# http://picamera.readthedocs.io/en/latest/recipes2.html#web-streaming

import io
import picamera
import logging
import socketserver
from threading import Condition
from http import server

PAGE="""\

<html lang="en">
<head>
  <title>ATC</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>

<style>
    .center {
      margin-top: 100px;
      text-align: center;
    }
	
    .center_2 {
      text-align: center;
    }
</style>
 
</head>

<!--start of navbar code-->
<body>  
<nav class="navbar navbar-default navbar-fixed-top">
  <div class="container-fluid">
    <ul class="nav navbar-nav">
      <li><a href="index.html">Home</a></li>
      <li><a href="photos.html" id = 'photos'>Your Photos and Videos</a></li>
    </ul>
  </div>
</nav>
</body>

<body>
    <!--below makes sure ATC Car View is always center above video-->
    <div class="row"> <!--row-->
        <div class="col-xs-4 col-sm-4 col-md-4"></div> <!--column-->
            <div class="col-4 col-sm-4 col-md-4  center"> <!--column-->
                <h1>ATC Car View</h1>
            </div>
        </div>
    </div>
    <div class="row"> <!--Random buttons to show having elements next to the video.-->
        <div class="col-xs-1 col-sm-1"></div>
        <div class="col-xs-1 col-sm-1 col-md-1 center_2"></div>
        <div class="btn-group">
          <button type="button" class="btn btn-primary" id = 'record'>Record</button>
          <button type="button" class="btn btn-primary" id = 'pause'>Pause</button>
          <button type="button" class="btn btn-primary" id = 'stop'>Stop</button>
          <button type="button" class="btn btn-primary" id = 'camera'>Camera</button>
        </div>
        <div class="col-xs-1 col-sm-1 col-md-2 "></div>
        <div class="col col-sm-4 col-md-4 center_2">
            
            <img src="stream.mjpg" width="380" height="280">
        </div>
    </div>
	<div class="col-1 col-sm-1 col-md-1 "></div>
        <div class="col-3 col-sm-3 col-md-3 "> <!--column-->

		<div class="row">
		<div class="col-xs-4 col-sm-4 col-md-1"></div>
		<div class="col-xs-1 col-sm-1 col-md-1 center_2"></div>
			<button type="button" class="btn" id = 'forward'>Forward</button>

		<div class="row">
		<div class="col-xs-4 col-sm-4 col-md-1"></div>
		<div class="col-xs-2 col-sm-1 col-md-4 center_2">
		<button type="button" class="btn btn-outline-success" id = "left">Left</button></div>
		<div class="col-xs-2 col-sm-1 col-md-4 ">
		<button type="button" class="btn btn-outline-success" id = "right">Right</button></div></div>
		
		<div class="row">
		<div class="col-xs-4 col-sm-4 col-md-4 "></div>
		<div class="col-xs-1 col-sm-1 col-md-4 "></div>
		<button type="button" class="btn btn-outline-warning" id = 'backward'>Backward</button>
		</div>
		</div>
    </div>
        

</body>
<script>
  $("#left").click(function () {
      $.ajax({
          type: 'GET',
          url: "/moveleft/",
          success: function (data) {
              alert("Moved left successfully")
          }
      });
  });
  $("#right").click(function () {
      $.ajax({
          type: 'GET',
          url: "/moveright/",
          success: function (data) {
              alert("Moved right successfully")
          }
      });
  });
  $("#forward").click(function () {
      $.ajax({
          type: 'GET',
          url: "/moveforward/",
          success: function (data) {
              alert("Moved forward successfully")
          }
      });
  });
  $("#backward").click(function () {
      $.ajax({
          type: 'GET',
          url: "/movebackward/",
          success: function (data) {
              alert("Moved backwards successfully")
          }
      });
  });
  $("#photos").click(function () {
      $.ajax({
          type: 'GET',
          url: "/photos/",
          success: function (data) {
          }
      });
  });
</script>

</html>
"""

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
                    self.send_header('Content-Length', len(frame))
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

with picamera.PiCamera(resolution='640x480', framerate=24) as camera:
    output = StreamingOutput()
    #Uncomment the next line to change your Pi's Camera rotation (in degrees)
    #camera.rotation = 90
    camera.start_recording(output, format='mjpeg')
    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        camera.stop_recording()
