from SimpleHTTPServer import SimpleHTTPRequestHandler
from BaseHTTPServer import HTTPServer
import XOHTTPStatus
import cgi

class XOHTTPRequestHandler(SimpleHTTPRequestHandler):
    # The Browser POSTs to save a file
    def do_POST(self):
        body = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ = {'REQUEST_METHOD':'POST'},
                keep_blank_values = 1)
        if self.path == '/write':
            self.write_file(body['save_content'].value)
            self.send_response(200)
        else:
            self.send_response(400)

    # Serve all static files out of the web subdirectory
    def translate_path(self, path):
        if path == '/':
            path = '/index.html'
        return SimpleHTTPRequestHandler.translate_path(self, '/web' + path)

    def write_file(self, content):
        # read the json file to determine where to save the content
        status = XOHTTPStatus.read_status()
        if status['command'] != 'write': 
            return
        fh = open(status['filename'], 'w')
        fh.write(content)
        fh.close()
        print "Saved content to %s"%status['filename']
        XOHTTPStatus.initialize()


def main():
    try:
        server = HTTPServer(('', 4080), XOHTTPRequestHandler)
        print 'Started server at http://localhost:4080'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
