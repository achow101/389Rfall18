Writeup 10 - Crypto II
=====

Name: Andrew Chow
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Chow

## Assignment 10 Writeup

### Part 1 (70 Pts)

For my attack, I used the legitimate hash of `5335b4d449c2b5946bad099faa4a0743` and a fake hash of `66cd9a8f04997c53ac5f230a848f24ed`.
The fake hash was the legit hash set as the intermediate state and then updated with the word `pwned`.
The resulting payload was `\x61\x61\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x00\x00\x00\x00\x00\x00\x00\x70\x77\x6e\x65\x64`.
By submitting this payload, I was able to get the flag `CMSC389R-{i_still_put_the_M_between_the_DV}` from the notary server.

To do this, I modified the provided stub code to connect to the server and send and receive data.
First it would connect, send a fixed message of `aa` and get back the legitimate hash.
Then it would extend this hash with malicious payload `pwned` in order to get the fake hash.
In order to figure out the payload, I then had to figure out the padding.
Since there are 10 possible paddings, I tried each possible padding and submitted the full payload to the server.
If I got a response that indicated success, the loop exited and told me what the hashes were, what the payload was, and what the server's response was.

### Part 2 (30 Pts)

To generate a key, one would do the following:

```
$ gpg --gen-key
<follow the prompts>
```

To import someone else's private key if it were named `pgpassignment.key`, you do

```
$ gpg --import-key pgpassignment.key
```

To encrypt a message to the ID `C140F7019C5FCF20E12A454F9665C74E448C470E` and write it to a file named `message.private`, you would do:
```
$ gpg -aer C140F7019C5FCF20E12A454F9665C74E448C470E > message.private
<type message at prompt>
```
