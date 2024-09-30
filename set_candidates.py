import os

def set_candidates():
    #get the cores of the computuer, works only on 16 >= core amount
    a=b"0000000000000000"
    l=[]
    l.append("{0:032b}".format(int(a,2)))
    #print(a[::-1])
    i=0
    #create the byte object
    while i < os.cpu_count()-1:
        a = bin(int(a,2) + 1)
        l.append(bin(int("{0:032b}".format(int(a,2))[::-1],2)))
        #print(a[::-1])
        i = i+1
    #join the rest of the bits
   
    return l