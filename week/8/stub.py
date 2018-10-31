#!/usr/bin/env python3

import sys
import struct
import argparse
import datetime

parser = argparse.ArgumentParser(description='Parses FPFF files')
parser.add_argument('file', help='Filename of FPFF file to parse')
args = parser.parse_args()

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(args.file, 'rb') as fpff:
    data = fpff.read()

# Unpack header
offset = 0
magic, version, timestamp, author, section_count = struct.unpack('<LLL8sL', data[0:24])
offset = 24

if magic != MAGIC:
    bork('Bad magic! Got {}, expected {}'.format(hex(magic), hex(MAGIC)))

if version != VERSION:
    bork('Bad version! Got {}, expected {}'.format(int(version), int(VERSION)))

print('------- HEADER -------')
print('MAGIC: {}'.format(hex(magic)))
print('VERSION: {}'.format(int(version)))
print('TIMESTAMP: {} ({} UNIX Timestamp)'.format(datetime.datetime.utcfromtimestamp(timestamp), timestamp))
print('AUTHOR: {}'.format(author.decode()))
print('SECTION COUNT: {}'.format(section_count))

print('-------  BODY  -------')

def section_name(stype):
    if stype == 1:
        print('TYPE NAME: PNG')
    elif stype == 2:
        print('TYPE NAME: DWORDS')
    elif stype == 3:
        print('TYPE NAME: UTF-8')
    elif stype == 4:
        print('TYPE NAME: DOUBLES')
    elif stype == 5:
        print('TYPE NAME: WORDS')
    elif stype == 6:
        print('TYPE NAME: COORDINATES')
    elif stype == 7:
        print('TYPE NAME: REFERENCE')
    elif stype == 9:
        print('TYPE NAME: ASCII')

# Unpack body
for i in range(0, section_count):
    # Unpack section
    print('-------  Section {}  -------'.format(i + 1))
    stype, slen = struct.unpack('<LL', data[offset:offset + 8])
    offset += 8
    print('STYPE: {}'.format(hex(stype)))
    print('TYPE NAME: {}'.format(section_name(stype)))
    print('SLENGTH: {}'.format(slen))
    if slen == 0:
        continue

    if stype == 1:
        pass
    elif stype == 2:
        pass
    elif stype == 3:
        pass
    elif stype == 4
        pass
    elif stype == 5:
        pass
    elif stype == 6:
        pass
    elif stype == 7:
        pass
    elif stype == 9:
        pass
    else:
        bork('Unknown type {} for section {}'.format(stype, i + 1))
