import random
def nonce_gen():
    hexdata = hex(random.getrandbits(32))[2:]
    nonce = hexdata + "G232425"
    return nonce