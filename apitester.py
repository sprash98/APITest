
# API Tester Class
# Author: Prashanth Raghavan
# Description: This class contains a set of pre-defined tests to test the user creation API at
# http://interview.onforce.com/qe/. This also contains methods to obtain user input for user 
# creation and validation

import requests
import argparse
import json
#from collections import OrderedDict
#from telnetlib import STATUS
from test_list import TestList
#from pip._vendor.requests import status_codes


class ApiTester(object):
    
    fields= ['firstName', 'lastName', 'username','password','email','phoneNumber']
    _test_list = [ {
        "firstName"     : "Prash",
        "lastName"      : "Raghavan",
        "email"         : "sprash98@yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "sprash98",
        "password"      : "Password234!"    
        },
        
        {
        "firstName"     : "San",
        "lastName"      : "Bad",
        "email"         : "sprash98#yahoo.com",
        "phoneNumber"   : "111-222-3333",
        "username"      : "Bademail",
        "password"      : "Password234!"    
        },
        ]
    
    def __init__(self,url,data=None):
        self.url = url
        self.data = data
        
                                
    
    def post_req(self):
        test_pass = 0
        test_fail = 0
        test_run = 0
        for data in self.data :
            test_run +=1
            req = requests.post(self.url,json=data)
            resp_json = req.json()
            if resp_json['success'] == True :
                print("User creation for user {} named {} successful!\n".format(test_run,data['username']))
                test_pass +=1
            else :
                test_fail += 1
                print("User creation for user {} failed with the following error(s):\n".format(test_run))
                for err in resp_json['errors']:
                    print("{}\n".format(err))
            
                    
        return (test_run,test_fail,test_pass)
    
    
    def validate(self,test):
        result = 0
        for k in self.fields:
            if k not in test :
                print("{} missing in test data. Cannot add user\n".format(k))
                return result
            
        if len(test) != len(self.fields) :
            print("Incorrect number of entries in user data.\
            Expected {} parameters but got {}. Cannot add user\n".format(len(self.fields),len(test)))
            return result
        
        return (result+1)
                                    
       
        
    def main(self):            
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
                if self.validate(user_data):
                    tc_data.append(user_data)
                    self.data = tc_data
                else:
                    print("Input data validation failed. Aborting...\n")
                    return result    
            except Exception as e:
                print("Test argument in incorrect format. Please supply user data \
                    as dictionary in format <key1>:<value1>,<key2>=<value2> etc\n")
                return result
                
        else :
            self.data = self._test_list
            
        self.test_total = len(self.data)
        (self.run_total,self.fail_total,self.pass_total) = api_test.post_req()
        
        #print("Test Results:\nTotal Tests: {}, Total Tests Run: {}, Pass: {}, Fail: {}\n".format(test_total,run_total,pass_total,fail_total))
        return (result+1)                  
        
        
                                
if __name__ == '__main__':
    api_test = ApiTester("http://interview.onforce.com/qe/")
    if not api_test.main() :
        print("Tests could not be run due to errors. Please try again\n")
    else :
        print("Test Results:\nTotal Tests: {}, Total Tests Run: {}, \
        Pass: {}, Fail: {}\n".format(api_test.test_total,api_test.run_total,api_test.pass_total,api_test.fail_total))                            
                        
                
            
    
    
                
            
    
        
        
        
        
    

