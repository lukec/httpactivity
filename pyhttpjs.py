#!/usr/bin/python
import os
import gtk
import hulahop
hulahop.startup(os.path.expanduser('~/.test-hulahop'))
from hulahop.webview import WebView
from XOHTTPServer import XOHTTPServer

s = XOHTTPServer()
s.start()

def quit(window):
    hulahop.shutdown()
    gtk.main_quit()

def do_keypress(window, key):
    char = key.string
    if (char == 'w'):
        simulate_write_file()
    if (char == 'r'):
        simulate_read_file()

def simulate_read_file():
    write_file('{ "command": "read", "content": "foo" }')

def simulate_write_file():
    write_file('{ "command": "write" }')

def write_file(content):
    fh = open('status.json', 'w')
    fh.write(content)

window = gtk.Window()
window.set_default_size(600, 400)
window.connect("destroy", quit)
window.connect("key_press_event", do_keypress)

web_view = WebView()
web_view.load_uri("http://localhost:%s/index.html"%s.port)
web_view.show()
window.add(web_view)

window.show()
gtk.main()
