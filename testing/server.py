#!/usr/bin/env python2 

import zmq, time


port = "5556"
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

while True:
	print "Listening on %s" % port
	message = socket.recv()
	print "Received request: ", message
	#time.sleep (1)  
	socket.send("World from %s" % port)