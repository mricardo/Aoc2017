def valid_passphrase(p):
    words = p.split()
    freq = dict()
    for token in words:
        token_s = ",".join(sorted(token))
        
        if token_s in freq:
            return False
        else:
            freq[token_s] = 1

    return True   

counter = 0
with open('input') as f:
    for line in f:
        if (valid_passphrase(line)):
            counter += 1

print(counter)