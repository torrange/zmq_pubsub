#!/usr/bin/env python2

import zmq

context = zmq.Context()
socket  = context.socket(zmq.PAIR)
socket.bind("tcp://*:5556")

while True:
	print("listening..")
	message = socket.recv()
	socket.send("rahh")
	print(message)