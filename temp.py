l=[int(i) for i in input().split()]


for i in range(len(l)):
    if l.count(l[i])>1:
        print(True)
        break
    elif i==len(l)-1:
        print(False)
        break
    
    
    
