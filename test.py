from multiprocessing import Process, Pool
from set_candidates import set_candidates
from cpu_mine import cpu_mine

import os,sys,time

"""
#get the cores of the computuer, works only on 16 >= core amount
rest='000000000000'
a=b"0000"
l=[]
l.append("{0:04b}".format(int(a,2)))
print(a[::-1])
i=0
#create the byte object
while i < os.cpu_count()-1:
    a = bin(int(a,2) + 1)
    l.append("{0:04b}".format(int(a,2))[::-1])
    print(a[::-1])
    i = i+1
#join the rest of the bits
c = []
for i in l:
    c.append(i+rest)
#generate the bin list
list = []
for lista in c:
    list.append(bin(int(lista,2)))
"""

def test(param1,param2):
    print(param1+param2)
    return param1+param2

def test2(p):
    print(p)

if __name__ == '__main__':
    file = sys.argv[1]
    outputf = sys.argv[2]
    #time in seconds
    rtime = int(sys.argv[3])
  

    with open(file, "r") as block:
        #read the block
        content = block.read()
        #start timer
        end_time =time.time()+rtime
    lista = set_candidates()
    procesos = []
    """
    for n in lista:
        #print(n)
        proceso =Process(target=cpu_mine,args=(content,time.time()+rtime,n))
        procesos.append(proceso)
    for proceso in procesos:
        proceso.start()
    for proceso in procesos:
        proceso.join()
    """
    args=[]
    runtime = time.time()+rtime
    for bin in lista:
        args.append([content,runtime,bin])
    
    #print(args)
    lhash = ""
    lblock = ""
    hzero = 0
    with Pool(len(lista)) as pool:
        results = pool.map(cpu_mine,args)
        
        for i in results:
            #print(i)
            
            hash,block,zero =i
            if zero > hzero:
                lhash = hash
                lblock = block
                hzero = zero
    print(lhash)
    print(hzero)
    #"""