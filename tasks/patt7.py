for i in range(5):
    for j in range(5):
        if((i==j)or(j==0)or(i==4)or((j==1)and(i>=1))or((i==3)and(j==2))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
