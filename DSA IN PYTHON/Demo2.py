l=[2,3,5,6,7,9,11]
for i in range(len(l)//2+1):
    l[i],l[-1-i]=l[-1-i],l[i]
print(l)