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
    def setUp(self):
        '''
        Function to create an account's credentials before each test
        '''
        self.new_credential = Credential('Damaris','Facebook','damachep','pswd100')

    def test_init_(self):
        '''
        Test to if check the initializaton/creation of credential instances is properly done
        '''
        self.assertEqual(self.new_credential.user_name,'Damaris')
        self.assertEqual(self.new_credential.site_name,'Facebook')
        self.assertEqual(self.new_credential.account_name,'damachep')
        self.assertEqual(self.new_credential.password,'pswd100')

    def test_save_credentials(self):
        '''
        Test to check if the new credential info is saved into the credential list
        '''
        self.new_credential.save_credentials()
        twitter = Credential('Jane','Twitter','maryjoe','pswd100') 
        twitter.save_credentials()
        self.assertEqual(len(Credential.credentials_list),2)  





