def valid_passphrase(p):
    words = p.split()
    freq = dict()
    for token in words:
        if token in freq:
            return False
        else:
            freq[token] = 1

    return True   

counter = 0
with open('input') as f:
    for line in f:
        if (valid_passphrase(line)):
            counter += 1

print(counter)