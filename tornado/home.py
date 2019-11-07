import tornado.ioloop
import tornado.web
import socket 

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



if __name__ == "__main__":
    try: 
        host_name = socket.gethostname() 
        host_ip = socket.gethostbyname(host_name) 
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip) 
    except: 
        print("Unable to get Hostname and IP")

    try:
        port = 8010
        app = make_app()
        app.listen(port)
        print("connect to http://" + host_ip + ":" + str(port))
        print("use CTRL + C to exit")
        tornado.ioloop.IOLoop.current().start()
    # signal : CTRL + BREAK on windows or CTRL + C on linux
    except KeyboardInterrupt:
        print()
        print("stopping loop and closed port")
        tornado.ioloop.IOLoop.current().stop()
        
    