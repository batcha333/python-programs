a=int(input("enter: "))
sum=0
for i in range(1,a):
    if(a%i==0):
        print(i,end=" ")
        sum+=i
if(sum==a):
    print(a,"is a p num")
else:
    print(a,"is not p num")
