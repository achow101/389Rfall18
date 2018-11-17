#!/usr/bin/env python2
# from the git repo
from __future__ import print_function
import md5py
import binascii
import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('142.93.118.186', 1234))

# Get intro
data = s.recv(1024)
# print(data)

# Choose to sign some data
s.send('1\n')

# Get prompt
data = s.recv(1024)
# print(data)

# Send message to sign
message = 'aa'    # original message here
s.send(message)
s.send('\n')

# Get result
data = s.recv(1024)
# print(data)
legit = data.split()[-1]      # a legit hash of secret + message goes here, obtained from signing a message

# Get next prompt
data = s.recv(1024)
# print(data)

# initialize hash object with state of a vulnerable hash
fake_md5 = md5py.new('A' * 64)
fake_md5.A, fake_md5.B, fake_md5.C, fake_md5.D = md5py._bytelist2long(binascii.unhexlify(legit))

malicious = 'pwned'  # put your malicious message here

# update legit hash with malicious message
fake_md5.update(malicious)

# fake_hash is the hash for md5(secret + message + padding + malicious)
fake_hash = fake_md5.hexdigest()

#############################
### STEP 2: Craft payload ###
#############################

# TODO: calculate proper padding based on secret + message
# secret is <redacted> bytes long (48 bits)
# each block in MD5 is 512 bits long
# secret + message is followed by bit 1 then bit 0's (i.e. \x80\x00\x00...)
# after the 0's is a bye with message length in bits, little endian style
# (i.e. 20 char msg = 160 bits = 0xa0 = '\xa0\x00\x00\x00\x00\x00\x00\x00\x00')
# craft padding to align the block as MD5 would do it
# (i.e. len(secret + message + padding) = 64 bytes = 512 bits

for i in range(6, 16):
    padding = b'\x80' + b'\x00' * (55 - i - len(message)) + struct.pack('<Q', (i + len(message)) * 8)
    # payload is the message that corresponds to the hash in `fake_hash`
    # server will calculate md5(secret + payload)
    #                     = md5(secret + message + padding + malicious)
    #                     = fake_hash
    payload = message + padding + malicious
    assert(i + len(message) + len(padding) == 64)

    # send `fake_hash` and `payload` to server (manually or with sockets)
    # REMEMBER: every time you sign new data, you will regenerate a new secret!

    # send command to verify some data
    s.send('2\n')

    # Get prompt
    data = s.recv(1024)
    # print(data)

    # Send hash
    s.send(fake_hash)
    s.send('\n')

    # Get prompt
    data = s.recv(1024)
    # print(data)

    # Send payload
    payload = payload.replace('\n', '\\x0a')
    s.send(payload)
    s.send('\n')

    # Get result
    data = s.recv(1024)
    # print(data)

    # Get result
    data = s.recv(1024)
    if "Wow..." in data:
        break

print("FOUND")
print('Legit hash: {}'.format(legit))
print('Fake hash: {}'.format(fake_hash))
print('Payload: {}'.format(binascii.hexlify(payload)))
print(data)
