import socket
from http.server import BaseHTTPRequestHandler, HTTPServer

class IPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # Get the server's IP address
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        
        # Display the IP address
        self.wfile.write(f"<html><body><h1>IP Address: {local_ip}</h1></body></html>".encode("utf-8"))

def run(server_class=HTTPServer, handler_class=IPHandler):
    server_address = ('', 8080)  # Server will listen on all available interfaces on port 8080
    httpd = server_class(server_address, handler_class)
    print("Server started on port 8080...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
