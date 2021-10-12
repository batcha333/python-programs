a=[1,2,3,4,5,6,7,8]
even=[]
odd=[]
for i in a:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print('even is',even)
print('odd is',odd)
even.extend(odd)
print(even)
