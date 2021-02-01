import sys # provides getsizeof function

data = []
n = 26
prev = sys.getsizeof(data) # stores bytes of previous list size
for k in range(n+1): # range of n+1 ensures last k is included if it's exhaustive
    a = len(data) # number of elements
    b = sys.getsizeof(data) # actual size in bytes
    # compares current size to previous size and prints only if there's a change
    if b != prev:
        print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a-1, prev))
    prev = b # stores byte size for comparison in next loop iteration
    data.append(None) # increase length by one
