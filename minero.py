#!/bin/python

import sys
import time
from cpu_mine import cpu_mine
from gpu_mine import gpu_mine



if __name__ == '__main__':

    file = sys.argv[1]
    outputf = sys.argv[2]
    #time in seconds
    rtime = int(sys.argv[3])

    #longestfile = "salida2.txt"
    #the longest block
    #lblock =""
    #the longest hash
    #lhash=""
  
    #hashes current 0's
    #zeroaomount = 0    

    with open(file, "r") as block:
        #read the block
        content = block.read()
        #start timer
        end_time =time.time()+rtime
        """
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
        """
        lhash, lblock = cpu_mine(content,end_time)


    with open(outputf, "wb") as bestaptemt:
        bestaptemt.write(lblock.encode("utf-8"))
    print(lhash)