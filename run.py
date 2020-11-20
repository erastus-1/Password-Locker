#!/usr/bin/env python3.9

from user import User
from credentials import Credentials

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


    

