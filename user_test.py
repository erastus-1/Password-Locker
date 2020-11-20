import unittest #importing th unittest module
from  user import User #importing the User class
from  credentials import Credentials

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
       
        self.new_user.save_user() # checking the availability of a users for deleting
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

    def test_display_users(self):
        '''
        Method that returns a list af all users saved.
        '''

        self.assertEqual(User.dislpay_user(),User.user_list)


    class TestCredentials(unittest.TestCase):
        '''
        Test class that defines test cases for the users class behaviours.

        Args:
            unittest.TestCase: TestCase class that helps in creating test cases.
        '''

        def setUp(self):
            '''
            setUp method to run each test cases.
            '''
            self.new_credentials = Credentials('Erastus','Ruiru','Facebook','mutwech','5678') #create contact object


        def test_init(self):
            '''
            test_init test case to test if the object is initialized properly.
            '''

            self.assertEqual(self.new_credentials.first_name,'Erastus')
            self.assertEqual(self.new_credentials.second_name,'Ruiru')
            self.assertEqual(self.new_credentials.account,'Facebook')
            self.assertEqual(self.new_credentials.username,'mutwech')
            self.assertEqual(self.new_credentials.password,'5678')


    


if __name__ == "__main__":
    unittest.main()