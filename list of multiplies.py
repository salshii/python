i=1
n=int(input("enter the range"))
for i in range(1,n):
    if(i%3==0):
        print("A")
    elif(1%5==0):
        print("B")
    elif(i%3==0 & i%5==0):
        print("C")
    else:
        print(i)
