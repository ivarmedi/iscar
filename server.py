#!/usr/bin/python3

import socket
import json
import base64
from subprocess import Popen, PIPE
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import detector
import numpy
import matplotlib.pyplot as plt

hostName = ""
hostPort = 8000
det = detector.CarDetector()

class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.integer):
            return int(obj)
        elif isinstance(obj, numpy.floating):
            return float(obj)
        elif isinstance(obj, numpy.ndarray):
            return obj.tolist()
        else:
            return super(JsonEncoder, self).default(obj)

class MyServer(BaseHTTPRequestHandler):
    def _send_json(self, code, json):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", len(json))
        self.end_headers()
        self.wfile.write(json.encode("utf8"))

    def do_POST(self):
        global det
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        if self.headers['Content-Type'] == 'application/json':
            post_data = json.loads(post_data)

        filename = post_data['image']['filename']

        if filename:
            image = plt.imread(filename)
            detection = det.get_localization(image)

            self._send_json(200, json.dumps(detection, cls=JsonEncoder))

myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), f"Server Stops - {hostName}:{hostPort}")
