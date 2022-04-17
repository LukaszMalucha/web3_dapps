from cryptography.hazmat.primitives import hashes

class someClass:
    string = None
    num = 323442
    def __init__(self, mystring):
        self.string = mystring
    def __repr__(self):
        return self.string + "-" + str(self.num)


class CBlock:
    data = None
    previousHash = None
    previousBlock = None
    def __init__(self, data, previousBlock):
        self.data = data
        self.previousBlock = previousBlock
        if previousBlock != None:
            self.previousHash = previousBlock.computeHash()

    def computeHash(self):
        digest = hashes.Hash(hashes.SHA256())
        digest.update(bytes(str(self.data), 'utf-8'))
        digest.update(bytes(str(self.previousHash), 'utf-8'))
        return digest.finalize()


if __name__ == '__main__':
    root = CBlock('Root Block', None)
    B1 = CBlock('Child Block', root)

    B2 = CBlock("Second Block", root)
    B3 = CBlock(1234, B1)
    B4 = CBlock(someClass("Hi"), B3)
    B5 = CBlock("top block", B4)

    for b in [B1, B2, B3, B4, B5]:
        if b.previousBlock.computeHash() == b.previousHash:
            print("Success - good hash")
        else:
            print("Error - wrong hash")

    B3.data = 12345
    if B4.previousBlock.computeHash() == B4.previousHash:
        print("Error - tampering not detected")
    else:
        print("Success - Tampering detected")

    print(B4.data)
    B4.data.num = 9999
    print(B4.data)
    if B5.previousBlock.computeHash() == B5.previousHash:
        print("Error - tampering not detected")
    else:
        print("Success - Tampering detected")