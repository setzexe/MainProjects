import os                                                                # Allows for Python to talk to the computer's OS, or operating system
import base64                                                            # Base64 is a simple text encoding module that is not real encryption but converts text to random characters.
from getpass import getpass                                              # Allows for more "authentic" password experience. Essentially blanks the input when imputting a password

FILENAME = "passwords.txt"                                               # Python will automatically create this file in the same folder we run this program 

def add_password(passwords):                                             # Adds a password. We need to have passwords as the parameters because it would not know we are referring to otherwise
    account = input("Enter account name: ").strip()                      # Strip removes the new space / white space that exists at the end of each line. 
    if account in passwords:                                             # If any instance of account is in passwords...
        print("Account already exists!")
        return                                                           # return to main()
    password = getpass("Enter password: ")                               # getpass is practically just input, except user can not see what they are typing
    enc_pass = base64.b64encode(password.encode()).decode()              # base64 turns bytes rather into random chars (b64encode) or from random chars to bytes (b64decode). Encode turns a variable into bytes. Decode turns it into a string
    passwords[account] = enc_pass                                        # Whatever account we enter gets its own specific line
    print(f"Account for {account} saved.")
    
def load_passwords():                                                    # Loads our passwords
    passwords = {}                                                       # Create our list
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:                                   # With .. as .. means With (a condition) as (a representation). Basically, FILENAME in read mode ("r") is represented by f.
            for line in f:                                               # for every line (the loop sees it for data rather than the variable) in the file read mode (f)
                account, enc_pass = line.strip().split(":")              # account and enc_pass become that line, stripped of its new space & split at :
                passwords[account] = enc_pass
    return passwords                                                     # Return password list

def save_password(passwords):                                            # save a password into a file
    with open(FILENAME, "w") as f:                                       # F is represented by file's write mode
        for account, enc_pass in passwords.items():                      # For any time that account & enc_pass exists in passwords. items() returns tuples
            f.write(f"{account}: {enc_pass}\n")                           # because we need one row of info per line, we use \n and is why we use strip() so often


def view_passwords(passwords):                                           # View passwords   
    if not passwords:                                                    # if not is essentially the same as if len(passwords) == 0. Just checks if its empty
        print("No passwords in system!")
        return
    for account, enc_pass in passwords.items():                          # Items() checks tuples.
        dec_pass = base64.b64decode(enc_pass.encode()).decode()          # Encodes enc_pass to bytes, which is then decoded from base64, and then decoded to a string
        print(f"{account}: {dec_pass}")
        
def search_password(passwords):                                          # Search for a specific password
    account = input("Enter account name: ").strip()
    if account in passwords:                                             
        dec_pass = base64.b64decode(passwords[account].encode()).decode()  # Encodes whatever space in passwords has account, b64 decodes it, decode() turns back into string
        print(f"{account}: {dec_pass}")
    else:
        print("Password not found!") 
        
def delete_password(passwords):                                          # Delete a password
    account = input("Enter account name: ")
    if account in passwords:
        del passwords[account]                                           # deletes the password at account slot. Del deletes objects, variables. etc. x = 10, del x would cause print(f"{x}") to yield error
        print("Password deleted!")
    else:
        print("Account not found!")

def main():                                                              # We form the main() function for larger scale projects that might imported. Main() only runs if its from this specific file (code for that below this function)
    passwords = load_passwords()                                         # Runs right when main starts. Loads all the passwords / file info into a list (passwords)
    while True: 
        print("\nCyberSeverance Password Manager")
        print("Passwords are saved to file upon exiting")
        print("1. Add Password")
        print("2. View all Passwords")
        print("3. Search for a Password")
        print("4. Delete a Password")
        print("5. Exit")
        
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Incorrect input type! Please input a number 1-5.")
        
        match choice:
            case 1:
                add_password(passwords)                                  # IF THE FUNCTION NEEDS TO USE IT!!! MAKE SURE ITS A PARAMETER!!! A PARAMETER IN THE DEFINITION BUT NOT THE CALL LEADS TO ERROR
            case 2:
                view_passwords(passwords)
            case 3: 
                search_password(passwords)
            case 4:
                delete_password(passwords)
            case 5:
                print("Thank you for using CyberSeverance Password Manager!")
                save_password(passwords)                                 # Passwords saved to file before we exit
                break
            case _:
                print("Option unavailabvle.")
                
            
        
    
if __name__ == "__main__":                                               # Only runs main() if This file specifically is opened, not if its imported
    main()
        
        