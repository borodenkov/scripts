# coding: utf-8
# HTTP Сервер. Каждую строку входящего POST запроса.
# засовывает в параметр src тэга img и возвращает. Jmeter такие элементы востпринимает
# как embeded ресурсы и запрашивает их параллельно(если стоит галочка)
#
## Сделан для параллельной загрузки для Jmeter.
#
# 2015 год
#
# Запуск:
# tile_server.py -i IP -p PORT
#
# Зависимости:
# Python 2.7
#

from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse

class GetHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        parsed_path.query

        self.send_response(200)
        headers = {"Content-Type":"text/html"}
        self.end_headers()
        self.wfile.write(message)
        return

    def do_POST(self):
        # Parse the form data posted
        post_data = self.rfile.read(int(self.headers.getheader('Content-Length')))
		#message = '<html><body>{0}</body></html>'.format(''.join(['<img src="{0}">'.format(i) for i in post_data.split('\r\n')]))
        message = '<html><body>{0}</body></html>'.format(''.join(['<img src="{0}">'.format(i) for i in post_data.split('\n')]))

        # Begin the response
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        self.wfile.write(message)
        return        
        
if __name__ == '__main__':
    from optparse import OptionParser

    p = OptionParser()
    p.add_option('-i', '--ip', action="store", dest='socket_host', default='127.0.0.1', type="string", 
                 help="specify socket host ip")
    p.add_option('-p', '--port', action="store", dest='socket_port', default=8089, type="int",
                 help="specify socket host port")

    options, args = p.parse_args()
    
    # Swapping ForkingMixIn for ThreadingMixIn above would achieve similar results, using separate processes instead of threads.
    from SocketServer import ThreadingMixIn
    import threading
    from BaseHTTPServer import HTTPServer
    
    class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
        """Handle requests in a separate thread."""

    
    #server = HTTPServer((options.socket_host, options.socket_port), GetHandler)
    server = ThreadedHTTPServer((options.socket_host, options.socket_port), GetHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()