import os                                                                
import base64                                                            
from getpass import getpass                                              

FILENAME = "passwords.txt"                                               

def add_password(passwords):                                             
    account = input("Enter account name: ").strip()                       
    if account in passwords:                                             
        print("Account already exists!")
        return                                                           
    password = getpass("Enter password: ")                              
    enc_pass = base64.b64encode(password.encode()).decode()              
    passwords[account] = enc_pass                                        
    print(f"Account for {account} saved.")
    
def load_passwords():                                                   
    passwords = {}                                                       
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:                                   
            for line in f:                                               
                account, enc_pass = line.strip().split(":")              
                passwords[account] = enc_pass
    return passwords                                                     

def save_password(passwords):                                           
    with open(FILENAME, "w") as f:                                       
        for account, enc_pass in passwords.items():                      
            f.write(f"{account}: {enc_pass}\n")                          

def view_passwords(passwords):   
    if not passwords:                                                    
        print("No passwords in system!")
        return
    for account, enc_pass in passwords.items():                          
        dec_pass = base64.b64decode(enc_pass.encode()).decode()          
        print(f"{account}: {dec_pass}")
        
def search_password(passwords):                                          
    account = input("Enter account name: ").strip()
    if account in passwords:                                             
        dec_pass = base64.b64decode(passwords[account].encode()).decode() 
        print(f"{account}: {dec_pass}")
    else:
        print("Password not found!") 
        
def delete_password(passwords):                                          
    account = input("Enter account name: ")
    if account in passwords:
        del passwords[account]                                           
        print("Password deleted!")
    else:
        print("Account not found!")

def main():                                                              
    passwords = load_passwords()                                         
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
                add_password(passwords)                                  
            case 2:
                view_passwords(passwords)
            case 3: 
                search_password(passwords)
            case 4:
                delete_password(passwords)
            case 5:
                print("Thank you for using CyberSeverance Password Manager!")
                save_password(passwords)                                 
                break
            case _:
                print("Option unavailabvle.")
                
            
        
    
if __name__ == "__main__":                                               
    main()
        
        