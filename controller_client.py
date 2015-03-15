#!/usr/bin/env python2
#SUBSCRIBER CLIENT
import zmq
import time


def start_client(port, ip_addr):
    port = port
    ip_addr = ip_addr
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://%s:%s" % (ip_addr, port))
    socket.setsockopt(zmq.SUBSCRIBE, "1")
    
    while True:
        msg = socket.recv()
        print(msg)

if __name__ == "__main__":
    #start_client("5556", "127.0.0.1")
    start_client("5556", "192.168.0.2")
