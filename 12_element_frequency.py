lst=['A','E','B','D','A','B','E','C','B','A','D']
freq={} #freq is a dictionary

for i in lst:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1

print(freq)

