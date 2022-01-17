x=int(input("enter the first num:"))
y=int(input("enter the second num:"))
print("prime numbers are:")
while(x<=y):
    c=0
    i=1
    
    while(i<=x):
        if(x%i==0):
           c=c+1
        i=i+1
   
    if(c==2):
        print(x)
    x=x+1
