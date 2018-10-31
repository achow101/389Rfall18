#!/usr/bin/env python3

import sys
import struct
import argparse

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

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got {}, expected {}".format(hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got {}, expected {}".format(int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: {}".format(hex(magic)))
print("VERSION: {}".format(int(version)))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
