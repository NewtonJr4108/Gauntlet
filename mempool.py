'''
Views all pending tranactions in the blockchain.
'''
import numpy as np
import requests
while True:
    mempool = requests.get("http://localhost:5000/mempool").content
    mat = np.array([[mempool], [len(mempool)]])
    print(mat)
