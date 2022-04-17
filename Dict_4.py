d6 = {0: 10, 1: 24}
print('New key : ')
k = input()      #k=Key
v = input()      #v=Value
d6.update({int(k): int(v)})
print('Updated :\n', d6)
