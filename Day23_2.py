def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2,x):
            if x % n == 0:
               return False
        return True

def algo_from_instructions():
    b= 79
    b = b * 100 + 100000
    c = b + 17000
    h = 0
    for b in range(b, c + 1, 17):
        if not is_prime(b):
            h+=1
    
    print(h)
    
algo_from_instructions()