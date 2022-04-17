d1 = {'First Name': 'Krutik', 'Middle Name': 'Dilipbhai', 'Surname': 'Dadhaniya'}
print('Enter a key :-', end=' ')
val = input()
if d1.get(val):
    print('Already exists')
else:
    print('Does not exist')
    
