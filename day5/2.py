a=int(input())
x=[int(i) for i in str(a)]
print(x)
sum=0
for e in range(len(x)):
    sum+=x[e]
print(sum)
