
# API Tester Class
# Author: Prashanth Raghavan
# Description: This class contains a set of pre-defined tests to test the user creation API at
# http://interview.onforce.com/qe/. 

import requests
import argparse
import json



class ApiTester(object):
    
    fields= ['firstName', 'lastName', 'username','password','email','phoneNumber']
    _test_list = [ {
        # Functional Tests that should pass
        "firstName"     : "Prash",
        "lastName"      : "Raghavan",
        "email"         : "sprash98@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "sprash98",
        "password"      : "Password234!"    
        },
        # First Name with spaces and apostrophes
        {
        "firstName"     : "Pr 'ash",
        "lastName"      : "Raghavan",
        "email"         : "sprash98@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "spfirst",
        "password"      : "Password234!"    
        },
        # Last name with spaces and apostrophes
        {
        "firstName"     : "Prash",
        "lastName"      : "N 'ame",
        "email"         : "sprash98@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "splast",
        "password"      : "Password234!"    
        },
        # Two character username
        {
        "firstName"     : "Two",
        "lastName"      : "Char",
        "email"         : "sprash98@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "sp",
        "password"      : "Password234!"    
        },
        #7 character password
        {
        "firstName"     : "7size",
        "lastName"      : "password",
        "email"         : "sprash98@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "7charpwd",
        "password"      : "Pword2!"    
        },
        #19 character password
        {
        "firstName"     : "19char",
        "lastName"      : "password",
        "email"         : "sprash98@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "19charpwd",
        "password"      : "Password2345678!@%#"    
        },
        
        # First and last name with apostrophes and spaces
        {
        "firstName"     : "P 'rash",
        "lastName"      : "Ragh' avan",
        "email"         : "sprash98@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "specialnames",
        "password"      : "Password234!"    
        },
        
        # Negative Tests. The following tests should fail
        
        # First name with invalid characters    
        {
        "firstName"     : "Inv@#",
        "lastName"      : "Last",
        "email"         : "invfirst@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "invalidfirst",
        "password"      : "Password234!"    
        },
        
        # Last name with invalid characters 
         {
        "firstName"     : "badlast",
        "lastName"      : "Inv@#$",
        "email"         : "sprash98@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "invlast",
        "password"      : "Password234!"    
        },
        
        # Username with less than 2 characters
        {
        "firstName"     : "Too short",
        "lastName"      : "Username",
        "email"         : "tooshortuser@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "s",
        "password"      : "Password234!"    
        },
        
        #Password with lesser than 7 characters
        {
        "firstName"     : "Too short",
        "lastName"      : "password",
        "email"         : "tooshortpwd@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "shortpwd",
        "password"      : "P234!"    
        },
        
        #Password with more than 19 characters
        {
        "firstName"     : "Too long",
        "lastName"      : "password",
        "email"         : "toolongpwd@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "toolongpwd",
        "password"      : "Password2345678!@#$%^"    
        },
 
        # Password without an upper case alphabet
        {
        "firstName"     : "Passwd",
        "lastName"      : "No upper",
        "email"         : "pwdnoupper@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "noupperpwd",
        "password"      : "password2345678!@"    
        },
                
        # Password without a lower case alphabet
        {
        "firstName"     : "Passwd",
        "lastName"      : "No lower",
        "email"         : "pwdnolower@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "nolowerpwd",
        "password"      : "PWD2345678!"    
        },
        
        # Password without a number
        {
        "firstName"     : "Passwd",
        "lastName"      : "No number",
        "email"         : "pwdnonumber@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "nonumberpwd",
        "password"      : "Password!"    
        },        

        # Password without a special character
        {
        "firstName"     : "Passwd",
        "lastName"      : "No special",
        "email"         : "pwdnospecial@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "nospecialpwd",
        "password"      : "Password2345678"    
        },
        
        # Invalid email 
        {
        "firstName"     : "Invalid",
        "lastName"      : "Email",
        "email"         : "pw@e",
        "phoneNumber"   : "111-222-3333",
        "username"      : "bademail",
        "password"      : "Pass2345678!"    
        },
        
        # Invalid phone number 1
        {
        "firstName"     : "Bad",
        "lastName"      : "phone 1",
        "email"         : "badphone@yahoo.com",
        "phoneNumber"   : "11@1-222-3333",
        "username"      : "badphone1",
        "password"      : "Password234!"    
        },

        # Invalid phone number 2
        {
        "firstName"     : "Bad",
        "lastName"      : "phone 2",
        "email"         : "badphone2@yahoo.com",
        "phoneNumber"   : "111-22-3333",
        "username"      : "badphone2",
        "password"      : "Password234!"    
        },

        # Invalid phone number 3
        {
        "firstName"     : "Bad",
        "lastName"      : "phone 3",
        "email"         : "badphone@yahoo.com",
        "phoneNumber"   : "111-222-3333@",
        "username"      : "badphone3",
        "password"      : "Password234!"    
        },   
        
        # Invalid first name and username
        {
        "firstName"     : "B@#",
        "lastName"      : "last",
        "email"         : "badfirstuser@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "b",
        "password"      : "Password234!"    
        },     
        
        # Invalid last name and password
        {
        "firstName"     : "Bad",
        "lastName"      : "#$@",
        "email"         : "badlastpwd@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "badphone1",
        "password"      : "P234!"    
        },        
                
        # Invalid email and phone number
        {
        "firstName"     : "Bad",
        "lastName"      : "phone and email",
        "email"         : "badphoneemail",
        "phoneNumber"   : "11@1-222-3333",
        "username"      : "badphoneemail",
        "password"      : "Password234!"    
        },
        
        # Missing first name
        {
        "lastName"      : "phone 1",
        "email"         : "nofirst@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "nofirst",
        "password"      : "Password234!"    
        },
        
        # Missing last name
        {
        "firstName"     : "missing lastname",
        "email"         : "nolast@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "nolast",
        "password"      : "Password234!"    
        },
        
        # Missing email
        {
        "firstName"     : "missing",
        "lastName"      : "email",
        "phoneNumber"   : "111-222-3333",
        "username"      : "badphone1",
        "password"      : "Password234!"    
        },
        
        # Missing phone
        {
        "firstName"     : "Missing",
        "lastName"      : "email",
        "email"         : "nophone@yahoo.com",
        "username"      : "nophone",
        "password"      : "Password234!"    
        },
        
        # Missing user
        {
        "firstName"     : "missing",
        "lastName"      : "user",
        "email"         : "nouser@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "password"      : "Password234!"    
        },
        
        # Missing password
        {
        "firstName"     : "missing",
        "lastName"      : "password",
        "email"         : "nopwd@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "badphone1",    
        },
        
        #Additional fields 
        {
        "firstName"     : "Additional",
        "lastName"      : "field",
        "email"         : "extra@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "extra",
        "password"      : "Pass234!",
        "newfield"      : "new"   
        },                                                
        ]

    
    def __init__(self,url,data=None):
        """ Initialize the API object with the URL and user data"""
        self.url = url
        self.data = data
        self.run_total = 0
        self.pass_total = 0
        self.fail_total = 0
        self.test_total = 0        
                                
    
    def post_req(self):
        """ Perform the POST request for all test cases """
        test_pass = 0
        test_fail = 0
        test_run = 0
        for data in self.data :
            test_run +=1
            print("Running test case {}".format(test_run))
            req = requests.post(self.url,json=data)
            resp_json = req.json()
            if resp_json['success'] == True :
                print("Test Case {}: User {} created successfully !\n".format(test_run,data['username']))
                test_pass +=1
            else :
                test_fail += 1
                print("Test Case {}:User creation failed with the following error(s):\n".format(test_run))
                for err in resp_json['errors']:
                    print("{}\n".format(err))
            
                    
        return (test_run,test_fail,test_pass)                                    
       
        
    def main(self):            
        """Main function that adds parsing capabilities for test arguments """
        result= 0
        parser = argparse.ArgumentParser()
        parser.add_argument('-tc', '--test', type=str)
        args=parser.parse_args()
        if args.test :
            try :
                tc_data = list()
                user_data = dict()
                for (k,v) in list(map(lambda x:x.split(':'),args.test.split(','))) :
                    user_data[k] = v
                tc_data.append(user_data)
                self.data = tc_data  
            except Exception as e:
                print("Test argument in incorrect format. Please supply user data "
                    "as dictionary in format firstName:<name>,lastName=<name>"
                    " email:<email>, phoneNumber:<phone no>, username:<username>, "
                    "password:<password>\n")
                return result
                
        else :
            self.data = self._test_list
            
        self.test_total = len(self.data)
        (self.run_total,self.fail_total,self.pass_total) = api_test.post_req() 
        return (result+1)                  
        
        
                                
if __name__ == '__main__':
    api_test = ApiTester("http://interview.onforce.com/qe/")
    if not api_test.main() :
        print("Tests could not be run due to errors. Please try again\n")
    else :
        print("Test Results:\nTotal Tests: {}, Total Tests Run: {}, "
        "Pass: {}, Fail: {}\n".format(api_test.test_total,api_test.run_total,api_test.pass_total,api_test.fail_total))                            
                        
                
            
    
    
                
            
    
        
        
        
        
    

