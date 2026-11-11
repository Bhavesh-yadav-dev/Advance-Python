from http.server import BaseHTTPRequestHandler, HTTPServer

class Myserver(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            messge = "Hello! Message from python Server"
            self.send_response(200)
        elif self.path == '/about':
            messge = "This is a simple HTTP server built using Python's http.server module."
            self.send_response(200)
        elif self.path == '/contact':
            messge = "bhaveshyadavlinkdin19@gmail.com"
            self.send_response(200)
        else:
            messge = "404 Not Found"
            self.send_response(404)

        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(messge.encode())



server = HTTPServer(('localhost', 8000), Myserver)
print("Server started at http://localhost:8000")    
server.serve_forever()