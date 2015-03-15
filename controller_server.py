#!/usr/bin/env python2
#PUBLISHING SERVER 
import zmq
import time


def start_server(port, ip_addr, uid):
    port = port
    ip_addr = ip_addr
    uid = uid
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://%s:%s" % (ip_addr, port))
    
    while True:
        packet = "%d:wub" % uid
        socket.send(packet)
        print("sent %s" % packet)
        time.sleep(1)

if __name__ == "__main__":
    #start_server("5556", "*", 00000001)
    start_server("5556", "192.168.0.2", 00000001) 
