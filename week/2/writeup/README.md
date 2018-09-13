Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Andrew Chow
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Chow

## Assignment 2 writeup

### Part 1 (45 pts)

1. Fred Krueger

2. 
  - Born in 1990. From his twitter profile
  - Lives in Silver Spring, Maryland. From his twitter profile
  - Social Media accounts. Found in a google search of the name `kruegster1990`
    - Twitter: https://twitter.com/kruegster1990
    - Reddit: https://www.reddit.com/user/kruegster1990
  - Has a website `cornerstoneairlines.co`. Presumably is the owner of the company `Conerstone Airlines`. From twitter profile
  - Email is `kruegster@tutanota.com`: Listed on his website
  - Is flying from BWI to SFO on December 9, 2018  (or September 12, 2018 if European style. It is unclear what style should be used for this). From Instagram.

3. `142.92.118.186`. I found this by using the `dig` command to get the DNS records.

4. The page `http://www.cornerstoneairlines.co/secret/` was listed in the robots.txt. It contains a flag in the source code of the page: `CMSC389R-{fly_th3_sk1es_w1th_u5}`

5. The admin page is hosted on `142.93.117.193` which is directly linked on his website.

6. The associated servers are hosted with Digital Ocean. This was found with a reverse DNS search using the site https://who.is. Using a IP gelocation webiste https://www.iplocation.net/, I found the server to be located in New Jersey or New York, near New York City.

7. The server is running Ubuntu. Visiting a non-existent page on the server gives a 404 error stating that the server software is Apache 2.4.18 running Ubuntu.

8. 
  - `CMSC389R-{h1dden_fl4g_in_s0urce}` Found in the source code of the main page of the website.
  - `CMSC389R-{dns-txt-rec0rd-ftw}` Found in a TXT DNS record.

### Part 2 (55 pts)

The flag I found was `CMSC389R-{c0rn3rstone-air-27670}`.

This flag was found on the administration server located at `142.93.117.193`.
To find the port to connect to, I first used nmap to scan for all ports at that IP address.
The command was `nmap -p1-65535 142.93.117.193`.
When nmap finished, the resulting ports were 80, 2222, 1337, 10010.
I then connected to each port with `nc` to see if any returned a login prompt.
Port 1337 returned a login prompt.

To get the login, I used a brute force python script.
This script connected to `142.93.117.193` at port `1337`.
It fetched the username prompt, then submitted the username.
Then it fetches the password prompt and submits a password.

For the username, I tried a few different usernames. I tried kruegster1990, admin, administrator, and kruegster.
`kruegster` was the correct username.

For the password, I used the rockyou wordlist.
I copied the wordlist to my working directory and then opened it and read it line by line.
Each line is a password, so after stripping the whitespace, I submitted each line as a password attempt.
Failures resulted in a `Fail` string.
If a failure was observed, the socket was closed.
The next attempt then opened the socket again, handled the username prompt, submitted the username, handled the password prompt, and submitted the password.
This went in a loop until either something other than `Fail` was received or until 500 passwords had been attempted.
Eventually this resulted in correct password.

Once I had the password, I could login to the server.
I connected to the server using the nc command.
The full command was `nc 142.93.117.193 1337`.
The username was `kruegster` and the password was `pokenmon`.
After logging in, I looked in `/home` which had a folder named `flight_records`.
In `/home/flight_records`, there were `.txt` files for several different flight numbers.
From looking at `kruegster1990`'s instagram, I knew that he had a boarding pass for a flight with the number AAC27670.
Doing `cat AAC27670.txt` gave me the flag `CMSC389R-{c0rn3rstone-air-27670}`.
Some further investigation also showed that all of the flight record files have a flag of the format `CMSC389R-{c0rn3rstone-air-<flight number>}` where `<flight number>` is the number of the flight the record refers to.
