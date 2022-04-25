import pyperclip
import random
import string

#Global Variables
global users_list
class User:
    '''
    Class to create user accounts and save their information
    '''
    # Classs variables
    # global users_list
    users_list = []
    def_init_(self,first_name,last_name,password):
        '''
        Method to define the properties for each user object will hold.
        '''

        #instance variables
        self.first_name =first_name
        self.last_name = last_name
        self.passsword = passsword

        save-user(self):
        '''
        Function to save a newly created user instance
        '''
        User.users_list.append(self)
        