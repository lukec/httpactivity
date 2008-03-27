#!/usr/bin/python
import SimpleHTTPServer
import BaseHTTPServer

class SocialcalcRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def init (self, request, client_address, server):
        SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, request, 
                                                           client_address, server)

    def do_GET(self):
        print "do_GET\n";

# server = SimpleHTTPServer(("", 4080), SocialcalcRequestHandler)
port = 4080
print "Port: %s"%port
server = BaseHTTPServer.HTTPServer(("", port), SocialcalcRequestHandler)
server.serve_forever()

