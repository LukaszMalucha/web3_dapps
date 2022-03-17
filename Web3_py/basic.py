from web3 import Web3
import os
import environ

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

print(web3.eth.blockNumber)

balance = web3.eth.getBalance("zxczxczxc")
print(web3.fromWei(balance, 'ether'))