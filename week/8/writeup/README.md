Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: Andrew Chow
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Chow

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. Yes. `csec.umd.edu`

2. `laz0rh4x` and `c0uchpot4doz`

3. `104.248.224.85` and `206.189.113.189`

4. 2749

5. Their plans are happening "tomorrow at 1500"

6. File sent: `https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing`.
This file contains something hidden inside of it which requires a special parser that `laz0rh4x` gave `c0uchpot4doz` last week.

7. Tomorrow, presumably at 1500.

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*
1. 2018-10-25 00:40:07 (1540428007 UNIX Timestamp)

2. laz0rh4x

3. Claims 9 sections. Actually 11 sections

4.

```
-------  Section 1  -------
STYPE: 0x9
TYPE NAME: ASCII
TYPE NAME: None
SLENGTH: 51
Call this number to get your flag: (422) 537 - 7946
-------  Section 2  -------
STYPE: 0x5
TYPE NAME: WORDS
TYPE NAME: None
SLENGTH: 60
3
1
4
1
5
9
2
6
5
3
5
8
9
7
9
-------  Section 3  -------
STYPE: 0x6
TYPE NAME: COORDINATES
TYPE NAME: None
SLENGTH: 16
Latitude 38.99161, Longitude -77.02754
-------  Section 4  -------
STYPE: 0x7
TYPE NAME: REFERENCE
TYPE NAME: None
SLENGTH: 4
Referenced section: 1
-------  Section 5  -------
STYPE: 0x9
TYPE NAME: ASCII
TYPE NAME: None
SLENGTH: 60
The imfamous security pr0s at CMSC389R will never find this!
-------  Section 6  -------
STYPE: 0x9
TYPE NAME: ASCII
TYPE NAME: None
SLENGTH: 991
The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}
-------  Section 7  -------
STYPE: 0x6
TYPE NAME: COORDINATES
TYPE NAME: None
SLENGTH: 16
Latitude 38.9910941, Longitude -76.9328019
-------  Section 8  -------
STYPE: 0x1
TYPE NAME: PNG
TYPE NAME: None
SLENGTH: 245614
PNG written to file sec8.png
-------  Section 9  -------
STYPE: 0x9
TYPE NAME: ASCII
TYPE NAME: None
SLENGTH: 22
AF(saSAdf1AD)Snz**asd1
-------  Section 10  -------
STYPE: 0x9
TYPE NAME: ASCII
TYPE NAME: None
SLENGTH: 45
Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9

-------  Section 11  -------
STYPE: 0x2
TYPE NAME: DWORDS
TYPE NAME: None
SLENGTH: 48
4
8
15
16
23
42
```

5. Flags found:
```
CMSC389R-{c0rn3rst0n3_airlin3s_to_the_m00n}
```
