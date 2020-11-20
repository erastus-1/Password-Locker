import unittest #importing the unittest module
from  user import User #importing the User class
from  credentials import Credentials #importing the Credentials class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the users class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    '''

    def setUp(self):
        '''
        setUp method to run each test cases.
        '''
        self.new_user = User('Erastus','Ruiru','mutwech','1234') #create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly.
        '''

        self.assertEqual(self.new_user.first_name,'Erastus')
        self.assertEqual(self.new_user.second_name,'Ruiru')
        self.assertEqual(self.new_user.username,'mutwech')
        self.assertEqual(self.new_user.password,'1234')

    def test_save_user(self):
        '''
        test_save_user test case to test if the object is saved into the user list.
        '''
        
        self.new_user.save_user() # saving new user.
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list=[]

    def test_save_multiple_user(self):
        '''
        test case to test if the application can save multiple users.
        '''

        self.new_user.save_user()  #saving multiple users
        test_user = User('Erastus','Ruiru','mutwech','1234')
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test case to test if the application can delete a user.
        '''
       
        self.new_user.save_user() # checking the availability of a user for deleting
        test_user = User('Erastus','Ruiru','mutwech','1234')
        test_user.save_user()
       
        self.new_user.delete_user()# deleting a user from the application
        self.assertEqual(len(User.user_list),1)

    def test_find_user(self):
        '''
        find_user case is to test if a user can check an existing user by searching their name and display their information.
        '''

        self.new_user.save_user() # checking the availability of a users for deleting
        test_user = User('Erastus','Ruiru','mutwech','1234')
        test_user.save_user()

        found_user = User.find_by_first_name('Erastus')

        self.assertEqual(found_user.second_name,test_user.second_name) 


    def test_user_exists(self):
        '''
        Test to check if we can return a boolean if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User('Erastus','Ruiru','mutwech','1234')
        test_user.save_user()

        user_exists = User.user_exist('Erastus')

        self.assertTrue(user_exists)    

    def test_display_user(self):
        '''
        Method that returns a list af all users saved.
        '''

        self.assertEqual(User.display_user(),User.user_list)
        


    class TestCredentials(unittest.TestCase):
        '''
        Test class that defines test cases for the credentials class behaviours.

        Args:
            unittest.TestCase: TestCase class that helps in creating test cases.
        '''

        def setUp(self):
            '''
            setUp method to run each test cases.
            '''
            self.new_credentials = Credentials('Erastus','Ruiru','Facebook','mutwech','5678') #create credentials object


        def test_init(self):
            '''
            test_init test case to test if the object is initialized properly.
            '''

            self.assertEqual(self.new_credentials.first_name,'Erastus')
            self.assertEqual(self.new_credentials.second_name,'Ruiru')
            self.assertEqual(self.new_credentials.account,'Facebook')
            self.assertEqual(self.new_credentials.username,'mutwech')
            self.assertEqual(self.new_credentials.password,'5678')


        def test_save(self):
            '''
            test case to test if the objects are save to the credentials list
            '''

            self.new_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),1)

        def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list=[]

        def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials is a method to save multiple credentials
            '''

            self.new_credentials.save_credentials()
            test_credentials = Credentials('Erastus','Ruiru','Facebook','mutwech','5678') # new credentials
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)
        
        def test_delete_credentials(self):
            '''
            test_delete is a method that delete's a credential from the credentials list
            '''

            self.new_credentials.save_credentials()
            test_credentials = Credentials('Erastus','Ruiru','Facebook','mutwech','5678') #new credentials
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials() #delete credentials from credentials list
            self.assertEqual(len(Credentials.credentials_list),1)
        
        def find_credentials(self):
            '''
            find_credentials is a method that you can search a credential by using credentails account name
            '''
            
            self.new_credentials.save_credentials()
            test_credentials = Credentials('Erastus','Ruiru','Facebook','mutwech','5678') #new credentials
            test_credentials.save_credentials()

            found_credentials = Credentials.find_by_first_name('Erastus')
            self.assertEqual(found_credentials.second_name,test_credentials.second_name) 

        def test_credentials_exists(self):
            '''
            credentials_exists is method that you can check the existence of a credential in the credentials list
            '''

            self.new_credentials.save_credentials()
            test_credentials = Credentials('Erastus','Ruiru','Facebook','mutwech','5678') #new credentials
            test_credentials.save_credentials()

            credentials_exists = Credentials.credentials_exist('Erastus')
            self.assertTrue(credentials_exists)   

        def test_display_credentials(self):
            '''
            display_credentials is a method that you can display all cretials available
            '''

            self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)              

if __name__ == "__main__":
    unittest.main()