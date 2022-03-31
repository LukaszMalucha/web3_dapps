from web3 import Web3
import os
import environ

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

web3 = Web3(Web3.HTTPProvider(env("INFURA_URL")))

# Is Connected
print(web3.isConnected())

# Current Block Number
print(web3.eth.blockNumber)

balance = web3.eth.getBalance(env("ETHEREUM_WALLET"))
print(web3.fromWei(balance, 'ether'))