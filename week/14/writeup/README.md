Writeup 10 - Crypto II
=====

Name: Andrew Chow
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *PUT YOUR NAME HERE*

## Assignment 10 Writeup

### Part 1 (70 Pts)

Based on the instructions, I determined that the appropriate attack is a SQL Injection.
Clicking on the links on the webiste, I noticed that the page each item linked to had an `id` paramter with it's value set to a number.
It seemed likely that the id number was being passed to a SQL query and so the injection could be done by modifying the value of `id`.
I tried various things, including `' OR '1'='1'`, `' union select ...'`, and various other statements in order to try to get a response.
Some queries resulting in a 500 internal server error.
Other queries just returned the item for id 0.
My primary angle of attack was to use an additional select statement so that I could get the table names, and from there dump the tables.

However, this did not work.
After talking to Mike who mentioned that the site was behind a Web Application Firewall, I tried `' || '1'='1' -- -`.
This query is like the earlier `OR` I tried, but using a logical or and has a comment indicator at the end to ensure that the SQL statement is correct.
This resulted in all of the records in the table to be dumped to the page, revealing the flag.

The flag is `CMSC38R-{y0U-are_the_5ql_n1nja}`.

### Part 2 (30 Pts)

For the first challenge of the XSS game, I first did a test search and noticed the URL changed to include my search.
So I searched for `<script>alert(1)</script>` to trigger the XSS.

For the second challenge, I first tried putting a script tag in a post but that did not work.
After looking at the second hint, I searched for how to add a Javascript attribute to HTML elements.
From doing this, I found that the `onerror` for things like `img` tags can execute JavaScript.
So I added an image tag with an invalid image an the alert as `onerror`: `<img src=blah.jpg onerror="alert(1)"/>`

For the third challenge, I viewed the source code and noticed that the tab number was both in the URL and used to set the image `src` attribute.
Using a similar construction as in challenge 2, I was able to trigger an XSS by appending `#6.jpg' onerror="alert(1)"/>;` to the URL.

For the fourth challenge, I viewed the timer.html source code.
I saw that the code would do a string replacement in an `onload` attribute to set the timer.
So I input `1'); alert('1` in order to start the timer and execute the alert function when the page for the timer loads.

For the fifth challenge, I tried viewing the source code but was unable to determine what to do.
After seeing what the website did, I figured out that the way to trigger the XSS was to target the `next` parameter in the URL.
I tried various things such as `onclick`, closing the `a` tag and adding `script` tags, but nothing worked.
Eventually, after viewing the four hints, I read the mentioned IETF draft which indicated that I could set the `href` attribute to `javascript:alert(1)` by setting that as the `next` parameter.
Clicking the `next` link triggered the XSS.

For the sixth challenge, I viewed the code and saw that it was loading the JavaScript at the URL following the hash (`#`) sign.
I also noticed that it was checking for `http://` and `https://` in the URL, but only the lowercase versions.
So I created a malicious JavaScript script on pastebin and used that as the URL.
The URL was `htTps://pastebin.com/raw/nv18UY0t` and this triggered the XSS.
