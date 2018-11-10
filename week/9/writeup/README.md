Writeup 9 - Crypto I
=====

Name: Andrew CHow
Section: 0101

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Chow

## Assignment 9 Writeup

### Part 1 (60 Pts)

```
Hash: c35eb97205dd1c1a251ad9ea824c384e5d0668899ce7fbf269f99f6457bd06055440fba178593b1f9d4bfbc7e968d48709bc03e7ff57056230a79bc6b85d92c8, salt m, password jordan
Hash: d39d933d91c3e4455beb4add6de0a48dafcf9cb7acd23e3c066542161dcc8a719cbac9ae1eb7c9e71a7530400795f574bd55df17a2d496089cd70f8ae34bf267, salt u, password loveyou
Hash: 9a23df618219099dae46ccb917fbc42ddf1bcf80583ec980d95eaab4ebee49c7a6e1bac13882cf5dd8d3850c137fdff378e53810e98f7e9508ca8516e883458e, salt k, password neptune
Hash: 70a2fc11b142c8974c10a8935b218186e9ecdad4d1c4f28ec2e91553bd60cfff2cc9b5be07e206a2dae3906b75c83062e1afe28ebe0748a214307bcb03ad116f, salt p, password pizza
```

To solve this, I simply iterated through all of the passwords in the wordlist given, and each of the possible salts.
Each combination of `salt + password` was hashed with sha512 using hashlib.
The resulting hash was compared against the list of hashes that were read in from the hashes file.
Those hashes were read into a list and removed from the list after the hash was found.
This was done as a sanity check that all hashes had been cracked.

### Part 2 (40 Pts)

CMSC389R-{H4sh-5l!ngInG-h@sH3r}
