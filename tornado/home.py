import tornado.ioloop
import tornado.web
import socket 

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class PhotoHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("photos.html")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/", PhotoHandler),
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
        port = 8009
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
        
    