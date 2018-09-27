Writeup 3 - Pentesting I
======

Name: Andrew Chow
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Andrew Chow

## Assignment 4 Writeup

### Part 1 (45 pts)
The flag is `CMSC389R-{p1ng_as_a_$erv1c3}`.

The input to retrieve the flag is `; cat /home/flag.txt`

To find this flag, first, I used the `nc` command provided to connect to the server.
Then I first tested the expected behavior by providing an IP address.
I used the IP address `127.0.0.1` because that is guaranteed to work with whatever software as that is the loopback address.
The response received was identical to the output of the command `ping -c 2 127.0.0.1`.
Since the IP address I entered was at the end of this command, it seemed reasonable that the command could be terminated and another command given afterwards to execute.
The command terminator in bash is `;` so I tried `127.0.0.1; ls` as input. This gave me the ping output and the output of `ls`.
I could shorten this by removing `127.0.0.1` as `ping` would simply fail, but the next command would still execute.
This cleans up the output.
The `ls` output showed me that the current directory was root.
Since the flag was probably in `/home`, I next did `; ls /home` which gave me all of the files in `/home`.
The only file there was `flag.txt`.
I used `cat` to get the contents of `flag.txt`, so the input was `; cat /home/flag.txt` and that gave me the flag of `CMSC389R-{p1ng_as_a_$erv1c3}`.

To prevent this vulnerability, Fred could sanitize the input strings and remove any suspicious characters such as semicolons.
Fred could also ensure that the input string matches a specific pattern (e.g. `%d.%d.%d.%d` for IPv4 addresses) before passing the input on to the ping command.
If it doesn't match the pattern, then the script would return an error instead of executing the command.

### Part 2 (55 pts)

The interactive shell is implemented in `shell.py` using Python 3.

It uses an infinite while loop to listen for input from the user.
When `shell` is called, the `shell()` function is invoked, `pull()` is used for `pull`, and `exit` breaks out of the loop.
`help`, unknown, and malformed commands will print the help text.

For `shell`, I used another infinite while loop.
For every non-exit command, `send_cmd()` is used to get the output of the command and the current working directory.
`send_cmd()` opens a socket to the server, reads in all of the introduction text, then sends the command `; cd <working-dir>; <command>; echo ' $$$ '; pwd\n`
`cd <working-dir>` has the command go to the correct working directory for the command.
`echo ' $$$ '; pwd` is used to have a unique separator in the output followed by the new current working directory.
When the `exit` command is seen, the shell breaks out of the loop and the function returns.

`pull` also uses `send_cmd()` with a fixed command of `cat <remote-path>` to get the bytes of the file.
Those bytes are written to a new file opened with the `x` mode which only allows for writing to newly created files.
