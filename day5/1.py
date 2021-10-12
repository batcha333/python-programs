a=int(input("Enter the num : "))
fact=1
for i in range(1,a+1):
    fact=fact*i
    print(i,'=',fact)
print("Factorial of the given num: ",fact)
