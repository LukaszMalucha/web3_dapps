from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.exceptions import InvalidSignature

message = bytes("Secret Message", encoding="utf-8")

chosen_hash = hashes.SHA256()

def generate_keys():
    private = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public = private.public_key()
    return private, public

def sign(message, private):

    sig = private.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return sig

def verify(message, sig, public_key):
    try:
        public_key.verify(
            sig,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False
    except:
        print("Error executing public key verification")
        return False

if __name__ == "__main__":
    pr, pu = generate_keys()
    sig = sign(message, pr)


    # Attacker tries to mimic user using his own private key
    pr2, pu2 = generate_keys()
    sig2 = sign(message, pr2)

    correct = verify(message, sig2, pu)
    if correct:
        print("ERROR! Attack successful")
    else:
        print("Incorrect signature detected")

    # Original signature + bad message attack
    wrong_message = message = b"XXX"
    correct = verify(wrong_message, sig, pu)
    if correct:
        print("ERROR! Tempering Attack successful")
    else:
        print("Incorrect message detected")