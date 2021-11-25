a=int(input("enter the marks of MFC"))
b=int(input("enter the marks of DCA"))
c=int(input("enter the marks of ASE"))
d=int(input("enter the marks of ADS"))
e=int(input("enter the marks of PLAB"))
total=a+b+c+d+e
print("total=",total)
avg=total/5
print("average=",avg)
if(avg>70):
 print("GRADE A")
elif(avg>60):
 print("GRADE B")
elif(avg>50):
 print("GRADE C")
else:
 print("FAIL")
