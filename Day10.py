from operator import xor
from functools import reduce

h = [x for x in range(0, 256)]
pos = 0
skip_size = 0

def reverse_h(length, pos):
   i = 0
   size = len(h)

   while (i < length // 2):
       start_pos = (pos + i) % size
       end_pos = (pos + length - 1 - i) % size
      
       v = h[start_pos] 
       h[start_pos] = h[end_pos]
       h[end_pos] = v
       
       i += 1  

def do_hash(lengths):
    global pos
    global skip_size

    for l in lengths:  
        reverse_h(l, pos)
        pos += (l + skip_size)
        skip_size += 1
        
    return h[0] * h[1]

def dense_hash():
    dense = list()
 
    for i in range (0, 16):        
        dense.append(reduce(xor, h[i*16:(i+1)*16]))
    
    print(''.join((format(x, '02x') for x in dense)))

def hash():
    with open('input') as f:
        lengths = []
        for line in f:
          lengths = [ord(l) for l in line]

        lengths.extend([17, 31, 73, 47, 23])
        for i in range(0, 64):
            do_hash(lengths) 

hash()
dense_hash()
