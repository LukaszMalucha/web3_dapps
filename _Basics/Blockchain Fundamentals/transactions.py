import signatures
class Tx:
    inputs = None
    outputs = None
    sigs = None
    reqd = None

    def __init__(self):
        self.inputs = []
        self.outputs = []
        self.sigs = []
        self.reqd = []

    def add_input(self, from_addr, amount):
        self.inputs.append((from_addr, amount))
    def add_output(self, to_addr, amount):
        self.outputs.append((to_addr, amount))
    def add_reqd(self, addr):
        self.reqd.append(addr)
    def sign(self, private):
        message = self.__gather()
        message = bytes(str(message), 'utf-8')
        new_sig = signatures.sign(message, private)
        # self.sigs.append(new_sig)
    def is_valid(self):
        message = self.__gather()
        for addr, amount in self.inputs:
            found = False
            for s in self.sigs:
                message = bytes(str(message), 'utf-8')
                if signatures.verify(message, s, addr):
                    found = True
            if not found:
                return False
            if amount < 0:
                return False
        return True
    def __gather(self):
        data=[]
        data.append(self.inputs)
        data.append(self.outputs)
        data.append(self.reqd)
        return data

if __name__ == '__main__':
    pr1, pu1 = signatures.generate_keys()
    pr2, pu2 = signatures.generate_keys()
    pr3, pu3 = signatures.generate_keys()
    pr4, pu4 = signatures.generate_keys()

    tx1 = Tx()
    tx1.add_input(pu1, 1)
    tx1.add_output(pu2, 1)
    tx1.sign(pr1)


    tx2 = Tx()
    tx2.add_input(pu1, 2)
    tx2.add_output(pu2, 1)
    tx2.add_output(pu3, 1)
    tx2.sign(pr1)

    tx3 = Tx()
    tx3.add_input(pu3, 1.2)
    tx3.add_output(pu1, 1.1)
    tx3.add_reqd(pu4)
    tx3.sign(pr3)
    tx3.sign(pr4)


    for t in [tx1, tx2, tx3]:
        if t.is_valid():
            print("Success - valid transaction")
        else:
            print("Error - invalid transaction")

#   Wrong signature
    tx4 = Tx()
    tx4.add_input(pu1, 1.2)
    tx4.add_output(pu2, 1.1)
    tx4.sign(pr2)

#   Escrow tx not signed by arbiter
    tx5 = Tx()
    tx5.add_input(pu3, 1.2)
    tx5.add_output(pu1, 1.1)
    tx5.add_reqd(pu4)
    tx5.sign(pr3)

#   Two input addrs, signed by one
    tx6 = Tx()
    tx6.add_input(pu3, 1)
    tx6.add_input(pu4, 0.1)
    tx6.add_output(pu1, 1.1)
    tx6.sign(pr3)

# Output exceeds input
    tx7 = Tx()
    tx7.add_input(pu4, 1.2)
    tx7.add_output(pu1, 1)
    tx7.add_output(pu2, 2)
    tx7.sign(pr4)

# Negative Values
    tx8 = Tx()
    tx8.add_input(pu2, -1)
    tx8.add_output(pu1, -1)
    tx8.sign(pr2)


    for t in [tx4, tx5, tx6, tx7, tx8]:
        if t.is_valid():
            print("Error - invalid transaction was successful")
        else:
            print("Success - invalid transaction detected")

