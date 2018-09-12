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
  - Email is `kruegster1990@tutanota.com`: Listed on his website
  - Is flying from BWI to SFO on December 9, 2018  (or September 12, 2018 if European style. It is unclear what style should be used for this). From Instagram.

3. `142.92.118.186`. I found this by using the `dig` command to get the DNS records.

4. The page `http://www.cornerstoneairlines.co/secret/` was listed in the robots.txt. It contains a flag in the source code of the page: `CMSC389R-{fly_th3_sk1es_w1th_u5}`

5. The admin page is hosted on `142.93.117.193` which is directly linked on his website.

6. The associated servers are hosted with Digital Ocean. This was found with a reverse DNS search using the site https://who.is. Using a IP gelocation webiste https://www.iplocation.net/, I found the server to be located in New Jersey or New York, near New York City.

7. The server is running Ubuntu. Visiting a non-existent page on the server gives a 404 error stating that the server software is Apache 2.4.18 running Ubuntu.

8. 
  - `CMSC389R-{h1dden_fl4g_in_s0urce}` Found in the source code of the main page of the website.

### Part 2 (55 pts)

*REPLACE THIS TEXT WITH A BRIEF EXPLANATION OF YOUR APPROACH TO SOLVING THIS CHALLENGE, AND THE OUTCOME*
