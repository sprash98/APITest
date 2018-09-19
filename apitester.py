
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
        ]
    
    def __init__(self,url,data=None):
        self.url = url
        self.data = data
        
        
        
        #self.val_functions = OrderedDict([
        #                        ('firstName', self.val_name), 
        #                        ('lastName', self.val_name),
        #                        ('username', self.val_user),
        #                        ('password', self.val_pass),
        #                        ('email'   , self.val_email),
        #                        ('phoneNumber', self.val_phone)
        #                        ])
                                
    
    def post_req(self):
        test_pass = 0
        test_fail = 0
        test_run = 0
        for data in self.data :
            req = requests.post(self.url,json=data)
            resp_json = req.json()
            if resp_json['success'] == True :
                print("User {} creation successful!\n".format(data['username']))
                test_pass +=1
            else :
                test_fail += 1
                print("User {} creation failed with the following error(s):\n")
                for err in resp_json['errors']:
                    print("{}\n".format(err))
            test_run +=1
                    
        return (test_run,test_fail,test_pass)
    
    
    def validate(self,test):
        result = 0
        for k in self.fields:
            if k not in test :
                print("{} missing in test. Cannot add user\n".format(k))
                return result
        return (result+1)
                        
    
    def file_parse(self,file):
        
        result = 0
        try:
            with open(file) as f :
                tests=TestList()
                tlist = tests.get_cfg()
                tc = 1
                failures = list()
                for t in tlist :
                    if not self.validate(t):
                        print("Test case {} invalid. User cannot be created\n".format(tc))
                        tc +=1
                        failures.append(tc)
                        continue
        
                            
        except IOError:
            print("Error accessing file {}. Please verify and try again\n".format(f))
            return result       
        
        if failures:
            print("Testcases that failed parsing in file {}: {}".format(" ".join(map(str,failures))),file)
        else:
            result += 1
        return result
            
        
    def main(self):
        #if __name__ == '__main__':
        result= 0
        api_test = ApiTester("http://interview.onforce.com/qe/")
        #fields= ['firstName', 'lastName', 'username','password','email','phoneNumber']
        parser = argparse.ArgumentParser()
        #parser.add_argument("-f","--file", help="file containing an array of user dictionaries")
        
        args=parser.parse_args()
        if args.testcase :
            api_test.data = args.testcase
                
        else :
            api_test.data = api_test._test_list
            
        test_total = len(api_test.data)
        (run_total,fail_total,pass_total) = self.post_req()
        
        print("Test Results:\nTotal Tests: {}, Total Tests Run: {}, Pass: {}, Fail: {}\n".format(test_total,run_total,pass_total,fail_total))
        return (result+1)    
        
                
if __name__ == '__main__' :
        #status= 0
        api_test = ApiTester("http://interview.onforce.com/qe/")
        #fields= ['firstName', 'lastName', 'username','password','email','phoneNumber']
        parser = argparse.ArgumentParser()
        #parser.add_argument("-f","--file", help="file containing an array of user dictionaries")
        parser.add_argument('-tc', '--testcase', type=json.loads)
        args=parser.parse_args()
        if args.testcase :
            api_test.data = json.loads(args.testcase)
        else :
            api_test.data = api_test._test_list
            
        test_total = len(api_test.data)
        (run_total,fail_total,pass_total) = api_test.post_req()
        
        print("Test Results:\nTotal Tests: {}, Total Tests Run: {}, Pass: {}, Fail: {}\n".format(test_total,run_total,pass_total,fail_total))
        #return (status+1)                  
        
        
                                
                            
                        
                
            
    
    
                
            
    
        
        
        
        
    

