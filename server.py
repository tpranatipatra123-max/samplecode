from http.server import SimpleHTTPRequestHandler,HTTPServer
class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':    
            self.path = 'index.html'
            return super().do_GET()
             if__name__ == "__main__":
    server = HTTPServer(('localhost', 8000), MyHandler)
    print("serving on http://localhost:8000")
    server.serve_forever()
