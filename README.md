# SSH Bruteforcer

## Overview:
An SSH brute-forcing tool that uses a wordlist is a security tool designed to test the strength of SSH login credentials. It works by systematically trying out different username and password combinations from a provided list to see if it can gain access to an SSH server.

Key Features:

- Wordlist: The tool uses a list of possible usernames and passwords trying each combination to find the correct credentials.

- Targeting: You can specify the target SSH server by entering its IP address or hostname via the script.

- Logging: It keeps track of successful login attempts and any relevant details by providing a summary report at the end of its run.

## How to Use:

 - Download ssh-bruteforce.py.
   
 - Install External Modules:
   `pip install pwntools paramiko`.

 - Change the IP Address of the victim aswell, wordlist to use aswell the username to attack.
   
 - Run ssh-bruteforce.py on the attacker machine:
   `python ssh-bruteforce.py`.

 - Run server.py on the attacker Machine:
   `python3 server.py`.
   
 - Wait for the script to conduct the brute-forcing.

Important: While these tools are valuable for security testing, they can also be misused. Always ensure you have permission before running such tests on any system.
