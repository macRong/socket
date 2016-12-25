#!/usr/bin/python
# -*- coding:utf-8 -*-

if __name__ == '__main__':
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8010))
    sock.listen(5)
    while True:
        connection,address = sock.accept()
        try:
            connection.settimeout(5)
            buf = connection.recv(1024)
            if buf == '1':
                connection.send('welcome to eqi.cc server!')
            else:
                mess = raw_input()
                connection.send(mess)
        except socket.timeout:
            print 'time out'
        connection.close()
