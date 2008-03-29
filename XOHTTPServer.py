import BaseHTTPServer
import SimpleHTTPServer
import thread

class XOHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_POST(self):
        print "Got post!"
        content = self.rfile.read()
        print "Content: (%s)"%content

    def do_GET(self):
        if self.path == "/status.json":
            print "Special JSON!"
            SimpleHTTPServer.SimpleHTTPRequestHandler(self)

class XOHTTPServer:
    def __init__(self):
        self.port = 4080

    def start(self):
        try:
            t = thread.start_new(
                    self._socialcalc_server,
                    ())
        except Exception, e:
            print "EXCEPTION: " + str(e)
        self._server_thread = t
        print "Started thread"

    def _socialcalc_server(self, *args, **keys):
        print "Starting HTTP Server on port: %s"%self.port
        server = BaseHTTPServer.HTTPServer(("", self.port), XOHTTPRequestHandler)
        server.serve_forever()

        

