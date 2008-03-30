#!/usr/bin/python
import BaseHTTPServer
import SimpleHTTPServer
import thread
import httplib
from time import sleep
import os
import gtk
import hulahop
hulahop.startup(os.path.expanduser('~/.test-hulahop'))
from hulahop.webview import WebView

class XORequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def init (self, request, client_address, server):
        SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, request, 
                                                           client_address, server)

class SocialCalcServer:
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
        server = BaseHTTPServer.HTTPServer(("", self.port), XORequestHandler)
        server.serve_forever()


s = SocialCalcServer()
s.start()

def quit(window):
    hulahop.shutdown()
    gtk.main_quit()

window = gtk.Window()
window.set_default_size(600, 400)
window.connect("destroy", quit)

web_view = WebView()
web_view.load_uri("http://localhost:%s/index.html"%s.port)
#web_view.load_uri("/home/olpc/src/pyhttpjs/index.html")
web_view.show()

window.add(web_view)
window.show()

gtk.main()
