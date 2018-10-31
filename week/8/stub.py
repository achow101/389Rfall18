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
magic, version, timestamp, author, section_count = struct.unpack("<LLL8sL", data[0:24])

if magic != MAGIC:
    bork("Bad magic! Got {}, expected {}".format(hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got {}, expected {}".format(int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: {}".format(hex(magic)))
print("VERSION: {}".format(int(version)))
print("TIMESTAMP: {} ({} UNIX Timestamp)".format(datetime.datetime.utcfromtimestamp(timestamp), timestamp))
print("AUTHOR: {}".format(author.decode()))
print("SECTION COUNT: {}".format(section_count))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")
