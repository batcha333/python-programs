''''''
'''*'''
for i in range(5):
    for j in range(5):
        if((i==0)or(j==0)or(j==4)or((i+j==4)and(i>=2))or((i==j)and(i>=2))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()        
