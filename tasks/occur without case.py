str1="welcome to USA. usa is awesome, isn't it?".split(" ")
count=0
for i in range(len(str1)):
    print(str1[i])
    if("usa" in str1[i]):
        count=count+1
    elif("USA" in str1[i]):
        count=count+1
print(count)
   
       
           
