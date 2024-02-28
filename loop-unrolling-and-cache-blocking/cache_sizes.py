import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt
from numba import jit

NRUNS = 5000

l1size = int(80*1024/8) # 32 KB L1 cache, 8 byte per value in data.
l2size = int(2048*1024/8) # 256 KB L2 cache, 8 byte per value in data.

@jit(nopython=True)
def cachesize(data):
    i = 0
    LIM = data.shape[0]
    while i<NRUNS:
        #print(data.shape[0])
        j = 0
        while j < LIM:
            data[j] = 2.3*data[j]+1.2
            j += 1
        i += 1
       
        
@jit(nopython=True)
def cachesize_blockl1(data):
    b = 0 # block offset
    i = 0
    size = data.shape[0]
    while b<size:
        while i<NRUNS:
            #print(data.shape[0])
            j = 0
            while j < l1size and j+b < size:
                data[b+j] = 2.3*data[b+j]+1.2
                j += 1
            i += 1
        b += l1size


@jit(nopython=True)
def cachesize_blockl2(data):
    b = 0 # block offset
    i = 0
    size = data.shape[0]
    while b<size:
        while i<NRUNS:
            #print(data.shape[0])
            j = 0
            while j < l2size and j+b < size:
                data[b+j] = 2.3*data[b+j]+1.2
                j += 1
            i += 1
        b += l2size

# Execute each function once to force Numba to compile.
data = np.random.random(10)        
cachesize(data)
data = np.random.random(10)        
cachesize_blockl1(data)
data = np.random.random(10)        
cachesize_blockl2(data)


STEP = 128 * 2
K = 1
UL = STEP**2
t_list = []
tbl1_list = []
for asiz in range(STEP,UL,STEP*K):  
    print(asiz/1024*8,' KB')
    data = np.random.random(asiz)        
    start = timer()
    cachesize(data)
    end = timer()
    t_list.append((end-start)/asiz/NRUNS*1e9)
    data = np.random.random(asiz)        
    start = timer()
    cachesize_blockl1(data)
    end = timer()
    tbl1_list.append((end-start)/asiz/NRUNS*1e9)
plt.subplot(121)
plt.plot(np.array(range(STEP,UL,STEP*K))*8/1024,t_list,label='simple')
plt.plot(np.array(range(STEP,UL,STEP*K))*8/1024,tbl1_list,label='blocked by L1 size')
plt.plot([32,32],[0,1],':',label='L1 cache limit (32 KB)')
plt.ylabel('Time per element [ns]')
plt.xlabel('Data size [KB]')
plt.legend()


STEP = 512
K = 12
UL = STEP**2
t_list = []
tbl1_list = []
tbl2_list = []
for asiz in range(STEP,UL,STEP*K):  
    print(asiz/1024*8,' KB')
    data = np.random.random(asiz)        
    start = timer()
    cachesize(data)
    end = timer()
    t_list.append((end-start)/asiz/NRUNS*1e9)
    data = np.random.random(asiz)        
    start = timer()
    cachesize_blockl1(data)
    end = timer()
    tbl1_list.append((end-start)/asiz/NRUNS*1e9)
    data = np.random.random(asiz)        
    start = timer()
    cachesize_blockl2(data)
    end = timer()
    tbl2_list.append((end-start)/asiz/NRUNS*1e9)
plt.subplot(122)
plt.plot(np.array(range(STEP,UL,STEP*K))*8/1024,t_list,label='simple')
plt.plot(np.array(range(STEP,UL,STEP*K))*8/1024,tbl1_list,label='blocked by L1 size')
plt.plot(np.array(range(STEP,UL,STEP*K))*8/1024,tbl2_list,label='blocked by L2 size')
plt.plot([32,32],[0,1],':',label='L1 cache limit (32 KB)')
plt.plot([256,256],[0,1],'-.',label='L2 cache limit (256 KB)')
plt.xlabel('Data size [KB]')
plt.legend()
plt.show()

# Intel core i7-13700H
