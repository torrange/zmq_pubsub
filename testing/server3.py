#!/usr/bin/env python2

import  zmq
import  time
import sys

port = "5556"

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

count = 1

while True:
    socket.send("wub")
    if count % 2:
        socket.send("wubston")
    time.sleep(1)
