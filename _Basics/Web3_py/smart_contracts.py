import environ
from web3 import Web3

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()

# TURN ON GANACHE
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Is Connected
print(web3.isConnected())
print(web3.eth.blockNumber)

account_1 = "0xe2C31302F8FC9d9978e509EB90752b94c0E92E55"
account_2 = "0x37c96AFDB892B907E1c7CFF8079819F1a52c7354"

# Sign Transaction
private_key = "571725a11d02405a18136d2f7d0ea5f681dfa95e28c8ecc2ab4473bcdc97380b"

# Get the nonce
nonce = web3.eth.getTransactionCount(account_1)

# Build transaction
tx = {
    "nonce": nonce,
    "to": account_2,
    "value": web3.toWei(1, "ether"),
    "gas": 3000000,
    "gasPrice": web3.toWei('50', 'gwei')
}

# Sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)

# Send transaction
try:
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
except Exception as e:
    error = eval(str(e))
    print(error["message"])


# # Get transaction hash
# print(web3.toHex(tx_hash))













