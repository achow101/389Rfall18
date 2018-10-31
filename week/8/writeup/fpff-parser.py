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
sec = 1
while offset < len(data):
    # Unpack section
    print('-------  Section {}  -------'.format(sec))
    stype, slen = struct.unpack('<LL', data[offset:offset + 8])
    offset += 8
    print('STYPE: {}'.format(hex(stype)))
    print('TYPE NAME: {}'.format(section_name(stype)))
    print('SLENGTH: {}'.format(slen))
    if slen == 0:
        continue

    if stype == 1:
        with open('sec{}.png'.format(sec), 'wb') as f:
            f.write(b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a')
            f.write(data[offset:offset + slen])
        print('PNG written to file sec{}.png'.format(sec))
    elif stype == 2:
        if slen % 8 != 0:
            print('Section {}, invalid DWORDS length {}. Skipping.'.format(sec, slen))
            offset += slen
            continue
        num_dwords = slen // 8
        for j in range(0, num_dwords):
            begin = offset + j * 8
            end = offset + (j + 1) * 8
            dword = struct.unpack('<Q', data[begin:end])[0]
            print(dword)
    elif stype == 3:
        text = data[offset:offset + slen]
        print(text.decode('utf-8'))
    elif stype == 4:
        if slen % 8 != 0:
            print('Section {}, invalid DOUBLES length {}. Skipping.'.format(sec, slen))
            offset += slen
            continue
        num_doubles = slen // 8
        for j in range(0, num_doubles):
            begin = offset + j * 8
            end = offset + (j + 1) * 8
            double = struct.unpack('<d', data[begin:end])[0]
            print(double)
    elif stype == 5:
        if slen % 4 != 0:
            print('Section {}, invalid WORDS length {}. Skipping.'.format(sec, slen))
            offset += slen
            continue
        num_words = slen // 4
        for j in range(0, num_words):
            begin = offset + j * 4
            end = offset + (j + 1) * 4
            word = struct.unpack('<L', data[begin:end])[0]
            print(word)
    elif stype == 6:
        if slen != 16:
            print('Section {}, invalid COORDINATES length {}. Skipping.'.format(sec, slen))
            offset += slen
            continue
        coord1, coord2 = struct.unpack('<dd', data[offset:offset + 16])
        print('Latitude {}, Longitude {}'.format(coord1, coord2))
    elif stype == 7:
        if slen != 4:
            print('Section {}, invalid REFERENCE length {}. Skipping.'.format(sec, slen))
            offset += slen
            continue
        section = struct.unpack('<L', data[offset:offset + 4])[0]
        print('Referenced section: {}'.format(section))
    elif stype == 9:
        text = data[offset:offset + slen]
        print(text.decode('ascii'))
    else:
        bork('Unknown type {} for section {}'.format(stype, i))
    offset += slen
    sec += 1
print('------- DONE --------')
