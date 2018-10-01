Writeup 5 - Binaries I
======

Name: Andrew Chow
Section: 0101

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Chow

## Assignment 5 Writeup

When writing the assembly for the memset function, my plan was to copy the byte stored at the 2nd argument address (`rsi`) to the memory location specified by the first argument address (`rdi`).
Then I would increment `rdi` to get the next memory location, and do everything again in a loop.
The loop would use the number provided in the 3rd argument address (`rdx`) and decrement that to zero as loop does.
To achieve this looping part, I had to copy `rdx` to `rcx` as loop uses `rcx`.
I ran into a problem that I could not use the `mov byte ptr [rdi], rsi` syntax as explained in the slides.
I got around this by dropping the `byte ptr` part and changing `rsi` to `sil` so that it would use the implicit 8-bit data length from sil when moving.
Before calling `loop`, I added 1 to `rdi` so that I could write data to the next memory address.

For the strncpy function, I first began by copying my code for memset.
I then thought I could achieve the functionality I needed by doing `mov byte ptr [rdi], byte ptr [rsi]` which in theory would have gotten the byte pointed to by `rsi` and copied it to addres pointed to by `rdi`.
However this failed to assemble. Instead, I had to change this to first move the data at `rsi` to an 8-bit register, `dl`.
Then move from `dl` to the address pointed to by `rsi`.
Since I was using the 8-bit register, the length was implied.
Lastly I added 1 to both `rdi and `rsi` so that the next address after `rdi` could be copied to, and the next address after `rsi` could be copied from.
