#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer
import _grabbers.fetchBackgroundImg as bg
import os
from urlparse import urlparse, parse_qs

ADDR = '0.0.0.0'
PORT = 8081

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    #error_message_format = codecs.open('404.html','r','utf-8').read()

    def do_GET(self):
        path = self.translate_path(self.path)
        m = SimpleHTTPServer.SimpleHTTPRequestHandler.extensions_map;
        m[''] = 'text/html';
        m.update(dict([(k, v + ';charset=UTF-8') for k, v in m.items()]));

        req = urlparse(self.path)
        if req.path == '/bg':
            params = parse_qs(req.query)
            if 'hash' in params:
                bg.processHashtag(params['hash'][0])
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # Send the html message
            self.wfile.write('')
            return

        if not os.path.exists(path):
            self.path = '404.html'

        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler
server = SocketServer.TCPServer((ADDR, PORT), Handler)
print "Serving love in %s:%s" % (ADDR, PORT)

server.serve_forever()
