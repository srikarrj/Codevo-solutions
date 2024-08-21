import http.server
import socketserver
import pyqrcode
import png
import os
import socket
import webbrowser

# Define port and user name
PORT = 8000
USER_NAME = "sj"

# Function to get IP address
def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Obtain IP address and create QR code
ip_address = get_ip()
url = f"http://{ip_address}:{PORT}"
qr = pyqrcode.create(url)
qr.png("qrcode.png", scale=6)

# Define custom handler
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = f"./{self.path}"
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Display QR code
def display_qr_code():
    webbrowser.open("qrcode.png")

# Start server
def start_server(): 
    handler = MyHttpRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving at port {PORT}")
        display_qr_code()
        httpd.serve_forever()

# Run the server
if __name__ == "__main__":
    start_server()
