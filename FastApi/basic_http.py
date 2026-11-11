from http.server import BaseHTTPRequestHandler, HTTPServer
# basehttprequesthandler is a class


class Myserver(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(
            b"Hello! Message from python Server"
        )
        #bit string bacause in server we are sending data in bytes format
    

server = HTTPServer(('localhost', 8000), Myserver)
print("Server started at http://localhost:8000")    
server.server_forever()