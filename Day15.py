def calculate(previous_value, factor, divider):
    next_value = (previous_value * factor) % divider
    gen = bin(next_value)[2:].zfill(32)
    last16 = gen[16:]
    return (next_value, last16)

def generator(factorA, factorB, divider, starting_valueA, starting_valueB, limit):
    previous_valueA = starting_valueA
    previous_valueB = starting_valueB
    
    match = 0
 
    pairA = None
    pairB = None
    pairs = 0
    while pairs < limit:
        if (not pairA):
            (next_valueA, last16a) = calculate(previous_valueA, factorA, divider)
            previous_valueA = next_valueA
        
        if (not pairB):
            (next_valueB, last16b) = calculate(previous_valueB, factorB, divider) 
            previous_valueB = next_valueB
        
        if (next_valueA % 4 == 0):
            pairA = next_valueA
        
        if (next_valueB % 8 == 0):
            pairB = next_valueB
        
        if (pairA and pairB):
            pairs += 1
           
            if (last16a == last16b):               
                match += 1        

            pairA = None
            pairB = None
      
    return match

print(generator(16807, 48271, 2147483647,679, 771, 5000000))

