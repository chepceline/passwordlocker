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
            