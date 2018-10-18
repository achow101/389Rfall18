Writeup 7 - Forensics I
======

Name: Andrew Chow
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Chow

## Assignment 7 writeup

### Part 1 (40 pts)

1. JPEG

2. John Hancock Center in Chicago, Illinois

3. Taken August 22nd, 108 at 11:33:24 CDT. Timestamp is 2018:08:22 16:33:24Z

4. iPhone 8

5. 539.5 m above sea level

6. `CMSC389R-{look_I_f0und_a_str1ng}``

### Part 2 (55 pts)

To find the flag, first I loaded the binary into Cutter.
I went to the main function and started looking at what the program was doing.
The first thing I noticed was that it was opening a file at `/tmp/.stego`, reversing some data of length `0x2677`, and writing that data to the file, and printing the string `Where is your flag?`.
I then executed the binary and retrieved the file from `/tmp/.stego`.
Opening this file in a hex editor, I found that it was a JPEG file as the string `JFIF` could be seen in the file and it contained the header and footer for a JPEG.
To make it actually openable, I removed the byte preceding the header.
Because the file was named `.stego`, I thought that it was highly likely that something was hidden with `steghide`.
However `steghide` requires a password.
To get a hint, I opened the image in a image viewer. I also looked further in the binary.
I then tried several passwords, some related to the class, and others related to dinosaurs.
Thinking back to previous excersises in this course, I also contemplated writing a script to brute force the password using the rockyou wordlist.
Eventually I found the password to be `stegosaurus`.
With this password, I was able to get the flag: `CMSC389R-{dropping_files_is_fun}`.
