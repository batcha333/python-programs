s1='America'
s2='Japan'
a=0
for i in range(len(s1)):
    for j in range(len(s2)):
        if(i%3==0)and(j%2==0)and(i-j==a):
            a+=1
            print(s1[i]+s2[j],end="")
        

