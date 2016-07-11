from itertools import product

def alphaseq(n, alphabet):
    results = []
    for l in range(1, len(alphabet)+1):
        results.extend([''.join(p) for p in product(alphabet, repeat=l)])
        if len(results) >= n:
            return results[:n]
    return None




alphabet = 'abcdefghijklmnopqrstuvwxyz'

print(alphaseq(10, alphabet))
print(alphaseq(30, alphabet))
print(alphaseq(300, alphabet))
print(alphaseq(3000, alphabet))