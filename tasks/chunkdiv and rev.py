l=[11,45,8,23,14,12,78,45,89]
l1,l2,l3=[],[],[]
a=len(l)//3
for i in range(len(l)):
    if(i<3):
        l1.append(l[i])
    elif i>2 and i<6:
        l2.append(l[i])
    else:
        l3.append(l[i])

print('chunk 1',l1)
print('After Reversing',l1[::-1])
print('chunk 2',l2)
print('After Reversing',l2[::-1])
print('chunk 3',l3)
print('After Reversing',l3[::-1])
