Writeup 3 - OSINT II, OpSec and RE
======

Name: Andrew Chow
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Chow

## Assignment 3 Writeup

### Part 1 (100 pts)

#### Weak Password

Fred used a pretty weak password.
It was one that was found in the rockyou list and was a common single word that was clearly linked to his interests.
Instead of using such a simple password, Fred should have instead used a password manager to generate a password for him.
Password managers can generate securely random strings of text that can be used as a passphrase.
These strings would likely not appear in wordlists and they can take multiple times the lifetime of the universe to brute force.

Furthermore, Fred could have also checked whether his password was in [Have I Been Pwned's Pwned Passwords List](https://haveibeenpwned.com/passwords).
That list contains the SHA-1 hashes of hundreds of millions of plaintext passwords from many data breaches,
By hashing his password with SHA-1 and checking if it is in the list, Fred can check whether the password he is using has already been leaked to the world.
Using a password manager such as 1password would allow him to be able to do this quickly, automatically, and securely as that has built in functionality for checking the Pwned Passwords list.

#### Exposed Admin Server

Fred's admin server for his website was very easy to find.
Because that server is different from the webserver and contains information about flights themselves, it really should not have been publicly available.
It's IP address was on Cornerstone Airlines' website publicly.
It instead should not have been linked to from the Cornerstone Airline's website and the IP address should have been kept as something internal to the airline.

### Exposed Login Port

Fred's admin server should not have had the port to login to the server to be exposed publicly.
Instead of having anyone be able to connect to that port, Fred should have configure the server so that only users connecting from a hardcoded IP address (e.g. his IP address) can access the server.
All other connections from other IP addresses should have been dropped and not be allowed to attempt to login.
[Amazon Web Services recommends](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-recommended-nacl-rules.html) that their customers limit connections to the SSH port to specific IP addresses of the customers' home or office.
Fred should have done the same too for the login port on his admin server.
