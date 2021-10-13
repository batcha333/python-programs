l1=[10,20,30,40]
l2=[100,200,300,400]
for i in range(len(l1)):
    for j in range(len(l2)):
        if(i+j==3):
            print(l1[i],l2[j])
