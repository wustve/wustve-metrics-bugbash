import http.server
import socketserver

PORT = 8000  # You can change the port number here

# this is another change for another CL

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"serving here are changes more changes and another and heres more CL another another workety work at port more changes again, let's see what the average thing is is {PORT}")
    httpd.serve_forever()
