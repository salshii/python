m=int(input("enter the lower string"))
n=int(input("enter the upper string"))
print("prime numbers are ")
while(m<=n):
    c=0
    i=1
    while(i<=m):
         if m%i==0:
             c=c+1
         i=i+1
    if c==2:
       print(m)
    m=m+1
