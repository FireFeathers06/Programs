num=int(input("Enter a number "))
flag=0
for i in range(2,num):
    if num%i==0:
        flag=1
if flag==1:
    print("no is not prime")
else:
    print("no is prime")