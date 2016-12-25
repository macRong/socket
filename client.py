#!/usr/bin/python
#-*- coding: UTF-8 -*-

if __name__ == '__main__':
    import socket
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', 8010))
#        import time
#        time.sleep(2)
        sock.send('2')
        print sock.recv(1024)
        sock.close()
