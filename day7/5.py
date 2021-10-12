a=int(input())
odd=27
even=27
for i in range(a):
    if(i%2!=0):
        odd-=13
        print(odd)
    else:
        even-=13
        print(even)
