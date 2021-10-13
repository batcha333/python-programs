s1='Abc'
s2='Xyz'
for i in range(0,len(s1),1):
    for j in range(len(s2)-1,-1,-1):
        if(i+j==2):
            print(s1[i]+s2[j],end="")
