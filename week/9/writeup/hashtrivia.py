#!/usr/bin/env python3

import socket
import hashlib

host = "142.93.117.193"   # IP address or URL
port = 7331     # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
while True:
    data = s.recv(1024)
    print(data)
    if b"CMSC389R" in data:
        break

    instruction = data.split(b'\n')[-2]
    hash_type = instruction.split()[3].decode()
    to_hash = instruction.split()[-1]

    hash_func = hashlib.new(hash_type)
    hash_func.update(to_hash)
    hash_res = hash_func.hexdigest()
    s.send(hash_res.encode())
    s.send(b'\n')

# close the connection
s.close()
