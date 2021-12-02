x=int(input("enter the number"))
sum=0
i=0
while(x>0):
    i=x%10
    sum=sum+i
    x=x//10
print(sum)
