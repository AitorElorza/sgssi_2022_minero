import time
import hashlib
#from nonce_gen import nonce_gen
#from zero_count import zero_count
from numba import jit, cuda
import random

@jit
def get_randbits(amount):
    return random.getrandbits(32)


def nonce_gen():
    hexdata = hex(get_randbits(32))[2:]
    nonce = hexdata + " G25"
    return nonce

@jit(forceobj=True)
def hashing(sig_block):
    hexdigest = sig_block.hexdigest()
    return hexdigest

@jit
def zero_count(tocount):
    counter = 0
    while tocount[counter] == "0":
        counter += 1
    return counter




def gpu_mine(content, end_time):
    zeroaomount = 0
    zeros =0
    bits = b'00000000000000000000000000000000'
    while time.time() < end_time:
            #random nonce
            nonce = nonce_gen()
            nonce =  "{0:0>8X}".format(int(bits,2)).lower() + " G25"
            nonce_block = content + nonce
            sig_block = hashlib.sha256(nonce_block.encode())
            #hexdigest = sig_block.hexdigest()
            hexdigest = hashing(sig_block)
            #print(str(hexdigest))
            zeros = zero_count(hexdigest)
            #print(zeros)
            if zeros > zeroaomount:
                zeroaomount = zeros
                lhash = hexdigest
                lblock = nonce_block
            bits = bin(int(bits,2) + 1)
    return lhash, lblock