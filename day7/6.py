'''22,21,23,20,24,19'''
a=int(input("enter: "))
odd=24
even=19
for i in range(a):
    if(i%2!=0):
        odd+=1
        print(odd)
    else:
        even-=1
        print(even)

