#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer
import _grabbers.fetchBackgroundImg as bg
from urlparse import urlparse, parse_qs

ADDR = '0.0.0.0'
PORT = 8080

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
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

        m = SimpleHTTPServer.SimpleHTTPRequestHandler.extensions_map;
        m[''] = 'text/html';
        m.update(dict([(k, v + ';charset=UTF-8') for k, v in m.items()]));
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyRequestHandler
server = SocketServer.TCPServer((ADDR, PORT), Handler)
print "Serving love in %s:%s" % (ADDR, PORT)

server.serve_forever()
