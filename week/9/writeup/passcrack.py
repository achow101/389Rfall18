#!/usr/bin/env python3

import hashlib
import string

hashes = []
with open("../hashes", 'r') as f:
    for line in f.readlines():
        hashes.append(line.rstrip().lstrip())

salts = string.ascii_lowercase

with open("../probable-v2-top1575.txt", 'r') as passes:
    line = passes.readline();
    while line:
        line = line.rstrip().lstrip()

        for salt in salts:
            to_hash = salt + line
            sha512 = hashlib.sha512()
            sha512.update(to_hash.encode())
            result = sha512.hexdigest()
            if result in hashes:
                print('Hash: {}, salt {}, password {}'.format(result, salt, line))
                hashes.remove(result)

        line = passes.readline();

assert(len(hashes) == 0)
