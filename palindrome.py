n=int(input("enter the number"))
s=a=0
p=n
while(n>0):
 a=n%10
 s=s*10+a
 n=n//10
if(p==s):
    print("palindrome")
else:
    print("not palindrome")
        
