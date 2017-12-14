from operator import xor
from functools import reduce

def reverse_h(h, length, pos):
   i = 0
   size = len(h)

   while (i < length // 2):
       start_pos = (pos + i) % size
       end_pos = (pos + length - 1 - i) % size
      
       v = h[start_pos] 
       h[start_pos] = h[end_pos]
       h[end_pos] = v
       
       i += 1  

def do_hash(h, lengths, pos, skip_size, ):
    for l in lengths:  
        reverse_h(h, l, pos)
        pos += (l + skip_size)
        skip_size += 1
        
    return (pos, skip_size)

def hash(h, input):
        pos = 0
        skip_size = 0

        lengths = []
        lengths = [ord(l) for l in input]
        lengths.extend([17, 31, 73, 47, 23])
        for i in range(0, 64):
            (pos, skip_size) = do_hash(h, lengths, pos, skip_size) 

def knot_hash(input):
    h = [x for x in range(0, 256)]

    hash(h, input)
    dense = list()
 
    for i in range (0, 16):        
        dense.append(reduce(xor, h[i*16:(i+1)*16]))
    
    return ''.join((format(x, '02x') for x in dense))

def read():
    with open('input') as f:
        return f.readline()

#knot_hash(read())