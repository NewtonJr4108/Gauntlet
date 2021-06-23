import requests
import sys
import shutil
import time
from termcolor import colored, cprint
from codecarbon.emissions_tracker import EmissionsTracker  
    
    
    
    
    
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
        tracker = EmissionsTracker()
        tracker.start()
        # sending post request and saving response as response object
        r = requests.post(url = API_ENDPOINT)
        print("==============================================")
        print(r.json())
        print("==============================================")
        print("Blocksize: "+str(len(r.content))+" bytes")

        emissions = tracker.stop()
        fltem = ("{:.8f}".format(float(emissions)))
        print("You used "+fltem+" Kilowatt Hours to mine this block.")
        if float(fltem) > 1:
            time.sleep(10)
        
        for i in range(4):
            print("")
            
    
    
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
input()
