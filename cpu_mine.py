import time

import hashlib
from nonce_gen import nonce_gen
from zero_count import zero_count
"""
def cpu_mine(content, end_time):
    zeroaomount = 0
    while time.time() < end_time:
            nonce = nonce_gen()
            nonce_block = content + nonce
            sig_block = hashlib.sha256(nonce_block.encode())
            hexdigest = sig_block.hexdigest()
            zeros = zero_count(hexdigest)
            if zeros > zeroaomount:
                zeroaomount = zeros
                lhash = hexdigest
                lblock = nonce_block
                print("The zeros: "+ str(zeros) + " the digest " + str(hexdigest))
    return lhash, lblock
"""
#def cpu_mine(content,end_time,ibits):
def cpu_mine(params):
    
    zeroaomount = 0
    zeros =0
    
    #bits = b'00000000000000000000000000000000'
    #bits = ibits
    #recover imput variables
    bits = params[2]
    content = params[0]
    end_time= params[1]
    #initialize return parameters
    #lhash = ""
    #lblock = ""
    while time.time() < end_time:
    #while time.time() < params[1]:       
            #random nonce
            nonce = nonce_gen()
            nonce =  "{0:0>8X}".format(int(bits,2)).lower() + " G25"
            nonce_block = content + nonce
            #nonce_block = params[0] + nonce
            sig_block = hashlib.sha256(nonce_block.encode())
            #hexdigest = sig_block.hexdigest()
            hexdigest = sig_block.hexdigest()
            #print(str(hexdigest))
            zeros = zero_count(hexdigest)
            #print(zeros)
            if zeros > zeroaomount:
                zeroaomount = zeros
                lhash = hexdigest
                lblock = nonce_block
            bits = bin(int(bits,2) + 1)
            #print(bits)
    #print(lhash)
    #print(zeroaomount)
    return lhash,lblock,zeroaomount