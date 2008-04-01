from sugar.activity import activity
from sugar.activity.activity import get_bundle_path
from sugar import env
import logging
import sys, os
import gtk
import hulahop
from BaseHTTPServer import HTTPServer
import thread
from XOHTTPServer import XOHTTPRequestHandler
import XOHTTPStatus

hulahop.startup(os.path.join(env.get_profile_path(), 'gecko'))
from hulahop.webview import WebView

class HTTPActivity(activity.Activity):
    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        toolbox = activity.ActivityToolbox(self)
        self.set_toolbox(toolbox)
        toolbox.show()

        # Set up the HTTP server thread
        XOHTTPStatus.initialize()
        self.port = 4080
        try:
            t = thread.start_new_thread(self._socialcalc_server_thread, ())
        except Exception, e:
            print "EXCEPTION: " + str(e)
        self._server_thread = t
        
        wv = WebView()
        bundle_path = get_bundle_path()
        wv.load_uri('http://localhost:%s/index.html'%self.port)
        wv.show()
        self.set_canvas(wv)

    def _socialcalc_server_thread(self, *args, **keys):
        print "Starting HTTP Server on port: %s"%self.port
        server = HTTPServer(("", self.port), XOHTTPRequestHandler)
        server.serve_forever()

    def write_file(self, filename):
        print "write_file: " + filename
        XOHTTPStatus.write_status({ 'command': 'write', 'filename': filename})

    def read_file(self, filename):
        print "read_file: " + filename
        fh = open(filename, 'r')
        content = fh.read()
        XOHTTPStatus.write_status({ 'command': 'read', 'content': content})
        


