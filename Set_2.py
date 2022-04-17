s2 =  {1,2,3,4,5}
print('Which element you want to remove : ')
e = input()
if int(e) in s2:  
    s2.discard(int(e))
    print('Removed')
    print(s2) 
else:
    print('Does not exist')
