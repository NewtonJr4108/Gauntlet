# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:46:52 2021

@author: Coding
"""

# importing the requests library
import requests
import sys
import shutil
import time

    
    
    
    
    
    
    
    
def loadwallet():
    print("Wallet loaded:")
    API_ENDPOINT = "http://127.0.0.1:5000/wallet"
    r = requests.get(url = API_ENDPOINT)
    print(r.content)
    print(r)

def generatewallet():
    API_ENDPOINT = "http://127.0.0.1:5000/wallet"
    r = requests.post(url = API_ENDPOINT)
    print(r.content)
    print(r)

    
           




def mine():
    while True:
    # defining the api-endpoint
        API_ENDPOINT = "http://127.0.0.1:5000/mine"
        
        # your API key here
        # your source code here
        
        # sending post request and saving response as response object
        r = requests.post(url = API_ENDPOINT)
        print("==============================================")
        print(r.json())
        print("Blocksize: "+str(sys.getsizeof(r))+" bytes")
        print("==============================================")
        
    
        for i in range(4):
            print("")
        time.sleep(10)
        continue
    
    
def welcomemsg():
    columns = shutil.get_terminal_size().columns
    print("==================================================".center(columns))
    print("Welcome to the Gauntlet terminal client.".center(columns))
    print("==================================================".center(columns))
    for i in range(5):
        print("")
    selection = input("Select what you would like to do:\n1:mine\n2:Generate new wallet\n3:Load Existing Wallet\n".center(columns))
    if selection == "1":
        mine()
    if selection == "2":
        generatewallet()
    if selection == "3":
        loadwallet()
welcomemsg()
