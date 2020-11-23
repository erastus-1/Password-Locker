#!/usr/bin/env python3.9

from user import User
from credentials import Credentials
import random, string
import getpass
# import pyperclip


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

def generate_password(credentials):
    """
    Function to generate random password for user
    """
    return credentials.generate_random_password()

# def copy_password(credentials):
#     """
#     function to copy password to the clipboard
#     """
#     return credentials.password,pyperclip.paste()

def main():
    print('\n')
    print("Hello Welcome to your password locker account. Whats your name?")
    user_name = input()
    
    ask = input(f"Hello {user_name}, do you have an account yes or no? ")
    print('\n')

    if ask == "no":
            print('Create your password locker account.')
            print('\n')
            print("new user")
            print(""*10)

            print ("first name ....")
            f_name = input()

            print ("last name....")
            l_name = input()

            print ("username....")
            username = input()
 
            print('\n')
            generate = input(f"{username}, Would you like an autogenerated password yes or no ? ")

            if generate =="yes":
                print('\n')
                print(f"You have successfully created a password locker account for {username}")

            if generate == "no":
                print("Create your password. ")
                getpass.getpass()
                print(f"You have successfully created a password locker account for {username}")
              

            while True:
                      print('\n')
                      print(f"Hello {user_name}. What would you like to do?")
                      print('\n')
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

                              print("Create your password.")
                              password = input()

                              print(f"Credential account for {f_name}, {l_name}, user name as {username}, for {account} account a password of {password} has successfully been created and saved.")
                              print ('\n')
 
         
                      elif short_code == 'dc':

                           if display_credentials(Credentials):
                              print('\n')
                              print("Here is a list of all credentials and their passwords")
                              print('\n')
             
                           for credentials in display_credentials(Credentials):
                              print(f"{credentials.first_name} {credentials.second_name} for {account} account username as {username} the password of this account is {password}")
                              print('\n')

                           else:
                               print('\n')
                               print('We dont seem to find any saved credentials account by that name! check your input')
                               print('\n')


                      elif short_code == 'rp':
                                print('\n')
                                print( "Which account do you want to autogenerate the password for? ")
                                account = input('account ')

                                def random_password(string_length):
                                   letters = string.ascii_letters
                                   return ''.join(random.choice(letters) for p in range(string_length))

                                # print(random_password(int(input("How many characters in your password ?"))))
                                
                                print(f"your {account} password is:", random_password(input))

                      elif short_code == 'fc':
                                print('\n')
                                print("Enter the first name you want to search for..")

                                search_first_name =input()
                                if check_credentials_exists(search_first_name):
                                   search_credentials = find_credentials(search_first_name)
                                   print(f"{search_credentials.account} {search_credentials.first_name}")
                                   print('-'*20)

                                   print(f"{account} password is {password}")

                                else:
                                    print('\n')
                                    print('We dont seem to find any saved credentials account by that name! check your input')
                                    print('\n')


                      elif short_code =='del':
                                 print('\n')
                                 print("Input the user first name of the account you prefer to delete?")
                                 account = input()

                                 credential = find_credentials(account)
                                 Credentials.credentials_list.remove(credential)

                                 print('\n')
                                 print(f"{account}  by the username {username} has successfully been deleted.")
                                 print('\n')

                      elif short_code == 'ex':
                                 print('\n')
                                 print("Thank you for your interest in our application...")
                                 break

                      else:
                          print("I really didn't get that. Please use the short codes provided")


        
    elif ask == "yes":
            print('\n')
            print('Please login using your user first name and password.')
            print("User")
            print(""*10)

            print ("first name ....")
            f_name = input()

            print("Create your password.")
            password = getpass.getpass()
            
            print('\n')
            print(f"You have successfully created a password locker account")
              

            while True:
                  print('\n')
                  print(f"Hello {user_name}. What would you like to do?")
                  print('\n')
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

                          print("Create your password.")
                          password = input()

                          save_credentials(create_credentials(f_name,l_name,username,account, 'password')) #create and save new credential
                          print('\n')
                          print(f"Credential account for {f_name}, {l_name}, user name as {username}, for {account} account a password of {password} has successfully been created and saved.")
                          print ('\n')
 
         
                  elif short_code == 'dc':

                      if display_credentials(Credentials):
                                print('\n')
                                print("Here is a list of all credentials and their passwords")
                                print('\n')
             
                      for credentials in display_credentials(Credentials):
                          print(f"{credentials.first_name} {credentials.second_name} for {account} account username as {username} the password of this account is {password}")
                          print('\n')

                      else:
                          print('\n')
                          print('We dont seem to find any saved credentials account by that name! check your input')
                          print('\n')


                  elif short_code == 'rp':
                            print('\n')
                            print( "Which account do you want to autogenerate the password for? ")
                            account = input('account ')

                            def random_password(string_length):
                                numbers = string.digits
                                return ''.join(random.choice(numbers) for p in range(string_length))
                            
                            print('\n')
                            print(f"your {account} password is:", random_password(6))

                  elif short_code == 'fc':
                             print('\n')
                             print("Enter the first name of the acount you want to search for..")

                             search_first_name =input()
                             if  check_credentials_exists(search_first_name):
                                 search_credentials = find_credentials(search_first_name)
                                 print(f"{search_credentials.account} {search_credentials.first_name}")
                                 print('-'*20)

                                 print(f"{account} password is {password}")

                             else:
                                 print('\n')
                                 print('We dont seem to find any saved credentials account by that name! check your input')
                                 print('\n')


                  elif short_code =='del':
                            print('\n')
                            print("Input the user first name of the account you prefer to delete?")
                            account = input()

                            credential = find_credentials(account)
                            Credentials.credentials_list.remove(credential)

                            print('\n')
                            print(f"{account}  by the username {username} has successfully been deleted.")
                            print('\n')


                  elif short_code == 'ex':
                             print('\n')
                             print("Thank you for your interest in our application...")
                             break
            
                  else:
                        print('\n')
                        print("I really didn't get that. Please use the shorts codes provided")
                        print('\n')
            
    else:
         print('\n')
         print("I really didn't get that. Please use the choices provided")
         print('\n')
         


if __name__ == "__main__":
    main()