a=int(input())
b=int(input())
c=int(input())
d=a+b
e=b+c
f=c+a
g=a&b
h=b&c
i=c&a
j=a|b
k=b|c
l=c|a
ans = [a,b,c,d,e,f,g,h,i,j,k,l]
'''sort=sorted(ans)'''
ans.sort()
'''print(sort[-1])'''
print(ans[-1])
print(ans)
ans.sort(reverse = True)
print(ans)
