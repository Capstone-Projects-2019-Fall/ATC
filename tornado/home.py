import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("template.html", title="My title", items=items)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8008)
    tornado.ioloop.IOLoop.current().start()