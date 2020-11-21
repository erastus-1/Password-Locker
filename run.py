#!/usr/bin/env python3.9

from user import User
from credentials import Credentials
import random
import getpass

def create_user(fname,lname,username,password):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,username,password)
    return new_user

def save_user(user):
    '''
    function to save new a user to the user_list
    '''
    user.save_user()

def delete_user(user):
    '''
    function to delete user from the user-list
    '''
    user.delete_user()

def find_user(first_name):
    '''
    function to find a user by using first_name
    '''
    return User.find_by_first_name(first_name)

def check_exists_user(first_name):
    '''
    function to check existing user
    '''
    return User.user_exist(first_name)

def display_user(user):
    '''
    function to dispaly user_list
    '''
    return User.display_user()


def create_credentials(fname,lname,account,username,password):
    '''
    function to create a new credential
    '''
    new_credentials = Credentials(fname,lname,account,username,password)
    return new_credentials

def save_credentials(credentials):
    '''
    function to save new credentials
    '''
    credentials.save_credentials()

def delete_credentials(credentials):
    '''
    function to delete credentials from credentials_list
    '''
    credentials.delete_credentials

def find_credentials(first_name):
    '''
    function to find credentials from credentials_list
    '''
    return Credentials.find_by_first_name(first_name)

def check_credentials_exists(first_name):
    '''
    function to check for existing credential
    '''
    return Credentials.credentials_exist(first_name)

def display_credentials(credentials):
    '''
    function to display all the existing credentials from the credentials_list
    '''
    return Credentials.display_credentials()

def generate_password(user):
    """
    Function to generate random password for user
    """
    return user.generate_random_password()

def main():
    print('\n')
    print("Hello Welcome to your password locker account. Whats your name?")
user_name = input()
    
print(f"Hello {user_name}. What would you like to do?")
print('\n')

while True:
    print("Use these short codes : cu - create a new user, du - display users, ex - exit")
    
    short_code = input().lower()

    if short_code == 'cu':
        print("new user")
        print(""*10)

        print ("first name ....")
        f_name = input()

        print ("last name....")
        l_name = input()

        print ("username....")
        username = input()

        create = input (f"{username}, Do you want autogenerated password? yes or no ")

        if create == "no":
            print("Create your password.")
            userpassword = input()
            getpass.getpass()

            save_user(create_user(f_name,l_name,username, 'password')) #create and savenew user.
            print ('\n')
            print(f"Password locker account for {f_name} {l_name} {username} has been successful.")
            print ('\n')

    elif short_code == 'du':
               
               if display_user(User):
                   print("Here is a list of all users")
                   print('\n')
                   
                   for user in display_user(User):
                       print(f"{user.first_name} {user.second_name}.... {user.username}")
                       print('\n')
               else:
                        print('\n')
                        print('We dont seem to find any saved users')
                        print('\n')

    elif short_code == 'ex':
            print("Thank you for your interest in our application...")
            break
    else:
            print("I really didn't get that. Please use the short codes provided")

            
        # elif create == "yes":
        #     print("Password is being generated!")         
        #     print("You have successfully created your password locker account.")

    while True:
        print("use this short codes to create a new credential account: cc - create new credentials, dc - display credentials, fc - find credentials, del - delete credential, rp - generate random password, ex - exit ")
    
        short_code = input().lower() 

        if short_code == 'cc':
            print("new credential")
            print(''*10)

            print ("first name...")
            f_name =input()

            print ("last name...")
            l_name = input()

            print ("username...")
            username = input()

            print ("account name...")
            account = input()

            create = input (f"{username}, Do you want autogenerated password? yes or no ")

            if create == "no":
                print("Create your password.")
                credentialspassword = input()
                getpass.getpass()

                save_credentials(create_credentials(f_name,l_name,username,account, 'password')) #create and save new credential
                print('\n')
                print(f"Credential account for {f_name}, {l_name}, {username}, for account {account}  has successfully been created and saved.")
                print ('\n')
                
             # elif create == "yes":
        #     print("Password is being generated!")         
        #     print("You have successfully created your password locker account.")   
        elif short_code == 'dc':

            if display_credentials(Credentials):
               print("Here is a list of all credentials and their passwords")
               print('\n')
             
            for credentials in display_credentials(Credentials):
                print(f"{credentials.first_name} {credentials.second_name} for {account} account as {credentials.username} the password is {credentials.password}")
                print('\n')

            else:
                print('\n')
                print('We dont seem to find any saved credentials')
                print('\n')

        elif short_code == 'rp':
                print( "Which account you want an autogenerated password for? ")
                account = input('account')

                def random_password(string_length):
                    letters = string_length.ascii_letters
                    return ''.join(random.choice(letters) for p in range(string_length))

                print(f"your {account} password is:", random_password(10))


        elif short_code == 'ex':
            print("Thank you for your interest in our application...")
            break
        else:
            print("I really didn't get that. Please use the short codes provided")


if __name__ == "__main__":
    main()