class User:
    '''
    Class that generates new instances of users.
    '''
     
    user_list =[] #empty user list

    def __init__(self,first_name,second_name,username,password):

       self.first_name = first_name
       self.second_name = second_name
       self.username = username
       self.password = password

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):
        '''
        Delete_user deletes user object from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_first_name(cls,first_name):
        '''
        Method that takes in first name and returns a user that matches that first name.
        
        Args:
             first_name First_name to search for
        Returns:
             Account of the user that matches the name
        '''

        for user in cls.user_list:
            if user.first_name == first_name:
                return user

    @classmethod
    def user_exist(cls,first_name):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for User in cls.user_list:
            if User.first_name == first_name:
                    return True

        return False

    @classmethod
    def user_display(cls):
        '''
        Method that displays all the users saved.
        '''
        return cls.user_list


