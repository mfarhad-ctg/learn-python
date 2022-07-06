for i in range(10):
    for i in range(5):
        print(i,end=" ")
    print(' ')

for i in range(5):
    for j in range(5):
        print(i,end='\t')
    print('')

for i in range(5):
    for j in range(i):
        print(i,end='\t')
    print('')