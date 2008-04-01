from sugar.activity import activity
from sugar.activity.activity import get_bundle_path
from sugar import env
import logging
import sys, os
import gtk
import hulahop
from BaseHTTPServer import HTTPServer
import thread
import from XOHTTPServer import XOHTTPRequestHandler

hulahop.startup(os.path.join(env.get_profile_path(), 'gecko'))
from hulahop.webview import WebView

class HTTPActivity(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        toolbox = activity.ActivityToolbox(self)
        self.set_toolbox(toolbox)
        toolbox.show()

        # Set up the HTTP server thread
        self.port = 4080
        try:
            t = thread.start_new_thread(self._socialcalc_server_thread, ())
        except Exception, e:
            print "EXCEPTION: " + str(e)
        self._server_thread = t
        
        wv = WebView()
        bundle_path = get_bundle_path()
        wv.load_uri('file://' + bundle_path + '/web/index.html')
        wv.show()
        self.set_canvas(wv)

    def _socialcalc_server_thread(self, *args, **keys):
        print "Starting HTTP Server on port: %s"%self.port
        server = HTTPServer(("", self.port), XOHTTPRequestHandler)
        server.serve_forever()

    def write_file(self, filename):
        print "write_file: " + filename
        f = open('web/status.json', 'w')
        f.write('{ "command" : "write" }')
        print "wrote status.json"

    def read_file(self, filename):
        print "read_file: " + filename

