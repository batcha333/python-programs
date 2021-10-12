bill=0
a=input("Pizza type: ")
if(a=="small"):
    bill+=20
elif(a=="medium"):
    bill+=30
else:
    bill+=50
b=input("pepper/onion: ")
if(a=="small" and b=="yes"):
    bill+=10
elif(a=="medium" and b=="yes"):
    bill+=20
elif(a=="large" and b=="yes"):
    bill+=30
else:
    bill+=0    
c=input("cheese: ")
if(c=="yes"):
    bill+=10
else:
    bill+=0
print(bill)
