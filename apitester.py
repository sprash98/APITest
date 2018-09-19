
# API Tester Class
# Author: Prashanth Raghavan
# Description: This class contains a set of pre-defined tests to test the user creation API at
# http://interview.onforce.com/qe/. This also contains methods to obtain user input for user 
# creation and validation

import requests
import argparse
import re
from collections import OrderedDict
from telnetlib import STATUS
from test_list import TestList


class ApiTester(object):
    
    fields= ['firstName', 'lastName', 'username','password','email','phoneNumber']
    
    def __init__(self,url,data):
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
        status = 0
        for data in self.data :
            req = requests.post(self.url,json=data)
            resp_json = req.json()
            if resp_json['success'] == 'True' :
                print("User {} creation successful!\n".format(data['username']))
                status +=1
            else :
                print("User {} creation failed with the following error(s):\n")
                for err in resp_json['errors']:
                    print("{}\n".format(err))
        
        return status
    
    
    def validate(self,test):
        status = 0
        for k in __class__.fields:
            if k not in test :
                print("{} missing in test. Cannot add user\n".format(k))
                return status
        return (status+1)
                        
        
    def file_parse(self,file):
        
        status = 0
        self.tlist = list()
        try:
            with open(file) as f :
                self.data = TestList()
                tc = 1
                failures = list()
                for t in self.tlist :
                    if not self.validate(t):
                        print("Test case {} invalid. User cannot be created\n".format(tc))
                        tc +=1
                        failures.append(tc)
                        continue
        
                            
        except IOError:
            print("Error accessing file {}. Please verify and try again\n".format(f))
            return status       
        
        if failures:
            print("Failed Tests: {}".format(" ".join(map(str,failures))))
        else:
            status += 1
        return status
            
        
        
    def arg_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-f","--file", help="file containing an array of user dictionaries")
        args=parser.parse_args()
        if args.file :
            if not self.file_parse(args.file) :
                print("Unable to parse")
            
        
        
                                
                            
                        
                
            
    
    
                
            
    
        
        
        
        
    

