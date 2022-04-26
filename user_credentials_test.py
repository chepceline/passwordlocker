import unittest
import pyperclip
from user_credentials import User, Credential

class TestUser(unittest.TestCase):
    '''
    Test class that definesbtest cases for the userclass behaviours.

    Args:
        unittest.TestCase: helps in creating test cases
    '''
    def setUp(self):
        '''
        Function to create a user account before each test
        '''
        self.new_user = User('Damaris','Chepchirchir','pswd100')

    def test_init_(self):
        '''
        Test to if check initialization/creation of user instances is properly done
        '''
        self.assertEqual(self.new_user.first_name,'Damaris')
        self.assertEqual(self.new_user.last_name,'Chepchirchir')
        self.assertEqual(self.new_user.password,'psw100')

    def test_save_user(self):
        '''
        Test to check if the new users info is saved into the users list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours

    Args:
        unittest.Testcase: helps in creating test cases
    '''
    def test_check_user(self):
        '''
        Function to test whether the login in function check_user
        '''
        self.new_user = User('Damaris','Chepchirchir','pswd100')
        self.new_user.save_user()
        user2 = User('Ken','Gikaru','pswd100')
        user2.save_user()

        for user in Users.users_list:
            if user.first_name == user2.first_name and user.password == user2.password:
                current_user = user.first_name
            return current_user

            self.assertEqual(current_user,Credential.check_user(user2.password,user2.first_name))    
               


