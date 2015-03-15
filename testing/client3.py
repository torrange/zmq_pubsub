#!/usr/bin/env python2

import zmq

port = "5556"

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:%s" % port)

socket.setsockopt(zmq.SUBSCRIBE, "wub")

while True:
    msg = socket.recv()
    print(msg)




