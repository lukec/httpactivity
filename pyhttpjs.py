#!/usr/bin/python
import BaseHTTPServer
import thread
import httplib
from time import sleep
import os
import gtk
import hulahop
hulahop.startup(os.path.expanduser('~/.test-hulahop'))
from hulahop.webview import WebView

class SocialcalcRequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def init (self, request, client_address, server):
        BaseHTTPServer.BaseHTTPRequestHandler.__init__(self, request, 
                                                           client_address, server)

    def do_GET(self):
        self.send_response(200, "Awesome")

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
        server = BaseHTTPServer.HTTPServer(("", self.port), SocialcalcRequestHandler)
        server.serve_forever()


s = SocialCalcServer()
s.start()


def quit(window):
    hulahop.shutdown()
    gtk.main_quit()

def keypress(window, key):
    print "pressed: " + key.string

window = gtk.Window()
window.set_default_size(600, 400)
window.connect("destroy", quit)
window.connect("key_press_event", keypress)

web_view = WebView()
web_view.load_uri('file:///home/olpc/src/pyhttpjs/index.html')
web_view.show()

window.add(web_view)
window.show()

gtk.main()
