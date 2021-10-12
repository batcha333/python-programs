for i in range(5):
    for j in range(7):
        if((i+j==3)or((j-i)==3)or((i==3)and(j==4))or((i==3)and(j%2==0))):
            print("*",end=" ")
    print()
