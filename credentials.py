import pyperclip

class Credentials:
    '''
    Class that generates new instances of credentials.
    '''
     
    credentials_list =[] #empty credential list

    def __init__(self,first_name,second_name,account,username,password):

       self.first_name = first_name
       self.second_name = second_name
       self.account = account
       self.username = username
       self.password = password

    
    def save_credentials(self):
        '''
        save_credentials method saves objects to credentials list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method deletes objects to credentials list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_first_name(cls,first_name):
        '''
        Method that takes in first name and returns a user that matches that first name.
        
        Args:
             credentials: First_name to search for a credential
        Returns:
             Account of the user that matches the name
        '''

        for credentials in cls.credentials_list:
            if credentials.first_name == first_name:
                return credentials

    @classmethod
    def credentials_exist(cls,first_name):
        '''
        Method that checks if a contact exists from the user list.
        Args:
            credentials: first name to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for Credentials in cls.credentials_list:
            if Credentials.first_name == first_name:
                    return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        display_credentials is a method that dispalys all the available credential accounts
        '''
        return cls.credentials_list

    @classmethod
    def copy_password(cls,credentials):
        '''
        copy_password is a method that enables a user to copy and paste in the application
        '''
        credentials_found = credentials.find_by_first_name(credentials)
        pyperclip.copy(credentials_found.password)
            