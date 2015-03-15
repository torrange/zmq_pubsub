#!/usr/bin/env python2 

from json import loads, dumps
import zmq


context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5556")

count = 0

while True:
    print("About to broadcast message: %d" % count)
    message = dumps({"Message":str(count)})
    socket.send(message)
    print("Message %d sent" % count)
    count += 1
